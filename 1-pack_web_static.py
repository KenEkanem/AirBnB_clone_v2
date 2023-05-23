#!/usr/bin/python3
"""This is a fabric script to create an archiveed file"""
from fabric.api import local
from datetime import datetime

# Do pack Function


def do_pack():
    """Saving the current timestamp and creatinf filename"""
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    filePath = "versions/web_static_{}.tgz".format(current_time)
    try:
        """create a directory called versions"""
        local("mkdir -p versions")
        """create an archived file"""
        local("tar -cvzf {} web_static/".format(filePath))
        """return the path to the archive file created"""
        return "{}".format(filePath)

        """return none if an error occurs"""
    except Exception as e:
        return None
