#!/usr/bin/python3
""" Cleanup function """
from fabric.api import *


env.hosts = ['100.26.135.224', '3.235.226.56']


def do_clean(number=0):
    """ Deletes out of date archives """

    number = 2 if int(number) == 0 else (int(number) + 1)

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
