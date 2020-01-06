#!/usr/bin/python3
""" distributes an archive to your web servers, using the function """

from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['35.237.139.137', '35.231.85.74']
env.user = "ubuntu"


def do_clean(number=0):
    """ Remove older files """
    if number == 0 or number == 1:
        keep = 1
    elif number == 2:
        keep = 2

    pathlocal = './versions/'
    pathhosts = '/data/web_static/releases'
    op1 = 'find {} -type f -printf "%T@ %p\n" | sort -n | '.format(pathlocal)
    op2 = 'cut -d' ' -f 2- | head -n -{} > list.txt'.format(keep)

    local(op1 + op2)
    local('xargs rm < list.txt')
    local('rm list.txt')

    op3 = 'find {} -type f -printf "%T@ %p\n" | sort -n | '.format(pathhosts)

    run('sudo ' + op3 + op2)
    run('xargs rm < list.txt')
    run('rm list.txt')
