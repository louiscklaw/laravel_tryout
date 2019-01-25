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


XDOTOOL_RELOAD_SH='''WID=`xdotool search --name "Material Design - Mozilla Firefox" | head -1`; xdotool windowactivate $WID; xdotool key F5'''


def docker_compose_cmd(cmd_body):
    local('docker-compose {}'.format(cmd_body) )

def docker_compose_exec(cmd_body):
    docker_compose_cmd(' exec {}'.format(cmd_body) )

def docker_compose_php_composer_install():
    docker_compose_exec("web /bin/sh -c 'cd /app/blog; composer install'")


def laravel_artisan_migrate():
    docker_compose_exec("web /bin/sh -c 'cd /app/blog; php artisan migrate'")

def docker_compose_restart():
    with lcd(DOCKER_DIR):
        local('docker cp ./_settings/000-default.conf laravel-php7:/etc/apache2/sites-available/000-default.conf')
        # local('docker cp ./_settings/apache2.conf laravel-tryout:/etc/apache2/sites-available/000-default.conf')
        local('docker-compose restart')
        print('restart done')

def laravel_rebuild():
    with lcd(DOCKER_DIR):
        docker_compose_php_composer_install()
        laravel_artisan_migrate()

def rebuild_docker():
    with lcd(DOCKER_DIR):
            local('docker-compose kill')
            local('docker-compose down')

            local('docker-compose build')

            local('docker-compose up')

@hosts('logic@localhost')
def helloworld():
    from xdo import Xdo
    xdo = Xdo()
    win_id = xdo.select_window_with_click()

    from pprint import pprint
    # pprint(win_id)
    pprint(xdo.get_window_name(win_id))

    win_id = xdo.search_windows('.+Chromium')
    pprint(win_id)

    # xdo.activate_window(win_id)
    # xdo.send_keysequence_window(win_id, "ctrl+l")
    # xdo.enter_text_window(win_id, 'Python rocks!')

def pyinotifyHelloworld():
    import pyinotify
    from xdo import Xdo
    from pprint import pprint

    wm = pyinotify.WatchManager()  # Watch Manager
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # watched events


    xdo = Xdo()
    # win_id = xdo.search_windows('.+Chromium.+')

    win_id_vscode = xdo.get_active_window()
    print('click chrome window to get win_id_chrome')
    win_id_chrome = xdo.select_window_with_click()

    CWD = os.path.dirname(os.path.abspath(__file__))

    def reload_browser(win_id_chrome):
        print('reloading')
        xdo.activate_window(win_id_chrome)
        xdo.send_keysequence_window(win_id_chrome, "Esc")
        xdo.send_keysequence_window(win_id_chrome, "ctrl+r")

    def back_to_origional(win_id_to_back):
        xdo.activate_window(win_id_to_back)

    class EventHandler(pyinotify.ProcessEvent):

        def process_IN_CREATE(self, event):

            print "Creating:", event.pathname
            reload_browser(win_id_chrome)
            back_to_origional(win_id_vscode)

        def process_IN_DELETE(self, event):
            print "Removing:", event.pathname

    print('start monitoring')
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)
    wdd = wm.add_watch(CWD, mask, rec=True, auto_add=True)

    notifier.loop()
