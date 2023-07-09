#!/usr/bin/python3
""" Fabfile to generates a .tgz archive from the contents of web_static."""

import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a .tgz archive from the contents of the web_static folder."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path))
    if result.failed:
        return None
    return archive_path

