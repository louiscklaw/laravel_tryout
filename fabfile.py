#!/usr/bin/env python
# init_py_dont_write_bytecode

#init_boilerplate

import os,sys
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from fabric.contrib.project import *

CWD = os.path.dirname(__file__)
DOCKER_DIR = os.path.join(CWD,'_docker')

def docker_compose_restart():
    with lcd(DOCKER_DIR):
        local('docker cp ./_settings/000-default.conf laravel-php7:/etc/apache2/sites-available/000-default.conf')
        # local('docker cp ./_settings/apache2.conf laravel-tryout:/etc/apache2/sites-available/000-default.conf')
        local('docker-compose restart')
        print('restart done')


def rebuild_docker():
    with lcd(DOCKER_DIR):
            local('docker-compose kill')
            local('docker-compose down')

            local('docker-compose build')

            local('docker-compose up')
