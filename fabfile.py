"""
Starter fabfile for deploying the mainapp project.

Change all the things marked CHANGEME. Other things can be left at their
defaults if you are happy with the default layout.
"""

import posixpath

from fabric.api import run, local, env, settings, cd, task
from fabric.contrib.files import exists
from fabric.operations import _prefix_commands, _prefix_env_vars
#from fabric.decorators import runs_once
#from fabric.context_managers import cd, lcd, settings, hide

# CHANGEME
env.hosts = ['user@mainapp.example.com']
env.code_dir = '/srv/www/mainapp'
env.project_dir = '/srv/www/mainapp/mainapp'
env.static_root = '/srv/www/mainapp/static/'
env.virtualenv = '/srv/www/mainapp/.virtualenv'
env.code_repo = 'git@github.com:user/mainapp.git'
env.uwsgi_ini = '/etc/uwsgi/vassals/mainapp_uwsgi.ini'
env.django_settings_module = 'mainapp.settings'

# Python version
PYTHON_BIN = "python2.7"
PYTHON_PREFIX = ""  # e.g. /usr/local  Use "" for automatic
PYTHON_FULL_PATH = "%s/bin/%s" % (PYTHON_PREFIX, PYTHON_BIN) if PYTHON_PREFIX else PYTHON_BIN

# Set to true if you can restart your webserver (via wsgi.py), false to stop/start your webserver
# CHANGEME
DJANGO_SERVER_RESTART = False


def virtualenv(venv_dir):
    """
    Context manager that establishes a virtualenv to use.
    """
    return settings(venv=venv_dir)


def run_venv(command, **kwargs):
    """
    Runs a command in a virtualenv (which has been specified using
    the virtualenv context manager
    """
    run("source %s/bin/activate" % env.virtualenv + " && " + command, **kwargs)


def install_dependencies():
    ensure_virtualenv()
    with virtualenv(env.virtualenv):
        with cd(env.code_dir):
            run_venv("pip install -r requirements/production.txt")


def ensure_virtualenv():
    if exists(env.virtualenv):
        return

    with cd(env.code_dir):
        run("virtualenv --no-site-packages --python=%s %s" %
            (PYTHON_BIN, env.virtualenv))
        run("echo %s > %s/lib/%s/site-packages/projectsource.pth" %
            (env.project_dir, env.virtualenv, PYTHON_BIN))


def ensure_src_dir():
    if not exists(env.code_dir):
        run("mkdir -p %s" % env.code_dir)
    with cd(env.code_dir):
        if not exists(posixpath.join(env.code_dir, '.git')):
            run('git clone %s .' % (env.code_repo))




def push_sources():
    """
    Push source code to server
    """
    #ensure_src_dir()
    local('git push origin master')
    with cd(env.code_dir):
        run('git pull origin master')


@task
def reload():
    """ Reload uswgi ini """
    run('touch %s' , env.uwsgi_ini)


@task
def run_tests():
    """ Runs the Django test suite as is.  """
    local("./manage.py test")


@task
def pull(app):
    "git pull per app"
    with cd(env.project_dir+'/'+ app ):
        run('git pull')
    reload()


@task
def collectstatic():
    "collect static files"
    with cd(env.project_dir):
        run_venv("./manage.py collectstatic -v 0 --clear --noinput")
        run("chown -R www-data:www-data static")


@task
def version():
    """ Show last commit to the deployed repo. """
    with cd(env.code_dir):
        run('git log -1')


@task
def uname():
    """ Prints information about the host. """
    run("uname -a")


@task
def sshagent_run(cmd):
    """
    Helper function.
    Runs a command with SSH agent forwarding enabled.

    Note:: Fabric (and paramiko) can't forward your SSH agent.
    This helper uses your system's ssh to do so.
    """
    # Handle context manager modifications
    wrapped_cmd = _prefix_commands(_prefix_env_vars(cmd), 'remote')
    try:
        host, port = env.host_string.split(':')
        return local(
            "ssh -p %s -A %s@%s '%s'" % (port, env.user, host, wrapped_cmd)
        )
    except ValueError:
        return local(
            "ssh -A %s@%s '%s'" % (env.user, env.host_string, wrapped_cmd)
        )


