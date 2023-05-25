#!/usr/bin/python3
"""
    This script distributes an archive file to remote servers
    and decompresses it
"""

from fabric.api import run, env, put
from fabric.api import *
import os.path

env.hosts = ['34.227.93.91', '52.73.25.125']
env.key_filename = "~/.ssh/id_rsa"
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    This function deploys the code and decompresses it
    """
    if not os.path.isfile(archive_path):
        return False

    compressed_files = archive_path.split("/")[-1]
    without_extension = compressed_files.split(".")[0]

    try:
        remote_path = "/data/web_static/releases/{}/".format(without_extension)
        sym_link = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(remote_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_files, remote_path))
        run("sudo rm /tmp/{}".format(compressed_files))
        run("sudo mv {}/web_static/* {}".format(remote_path, remote_path))
        run("sudo rm -rf {}/web_static".format(remote_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} {}".format(remote_path, sym_link))
        return True
    except Exception as e:
        return False

