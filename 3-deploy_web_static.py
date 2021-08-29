#!/usr/bin/python3
""" deploying the web_static work using Fabric (for Python3)."""

from fabric.api import env
from fabric.context_managers import cd
from fabric.api import run, put, local, settings
from os.path import isfile


env.hosts = ['35.243.253.93', '34.138.216.198']


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder
    """

    import tarfile
    import os.path
    from datetime import datetime
    from fabric.api import local

    folder_to_save = 'versions'
    time_format = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_file = 'web_static_{}.tgz'.format(time_format)

    if not os.path.exists(folder_to_save):
        os.mkdir(folder_to_save)

    with tarfile.open(folder_to_save + '/' + tar_file, "w:gz") as tar:
        tar.add('web_static', arcname=os.path.basename('web_static'))

    if os.path.exists(folder_to_save + '/' + tar_file):
        return folder_to_save + '/' + tar_file
    else:
        return None


def do_deploy(archive_path):
    """script that distributes an archive to your web servers,
    using the function do_deploy
    """
    file_name = str(archive_path.replace('versions/', ''))

    just_name = file_name.replace('.tgz', '')
    path_releases = "/data/web_static/releases"
    path_current = "/data/web_static/current"
    full_path = path_releases + "/" + just_name
    wb_st = "/web_static"

    if not isfile(archive_path):
        return (False)

    try:
        put(archive_path, "/tmp/" + file_name)
        run("mkdir -p " + path_releases + "/" + just_name + "/")
        run("tar -xzf /tmp/" + file_name + " -C " + full_path + "/")
        run("rm /tmp/" + file_name)
        run("mv " + full_path + wb_st + "/* " + full_path + "/")
        run("rm -rf " + full_path + wb_st)
        run("rm -rf /data/web_static/current")
        run("ln -s " + full_path + "/ /data/web_static/current")
        return(True)
    except:
        return (False)


def deploy():
    """distributes an archive to your web servers,
    """
    file_path = do_pack()
    if file_path is None:
        return (False)

    deploy_return = do_deploy(file_path)
    return (deploy_return)
