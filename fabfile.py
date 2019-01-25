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

def monAndReload():
    import pyinotify
    from xdo import Xdo
    from pprint import pprint
    from time import sleep

    wm = pyinotify.WatchManager()  # Watch Manager
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE # watched events


    xdo = Xdo()
    # win_id = xdo.search_windows('.+Chromium.+')

    win_id_vscode = xdo.get_active_window()
    print('click chrome window to get win_id_chrome')
    win_id_chrome = xdo.select_window_with_click()

    CWD = os.path.dirname(os.path.abspath(__file__))
    # CWD = '/home/logic/_workspace/laravel_tryout/app/blog'

    def reload_browser(win_id_chrome):
        xdo.activate_window(win_id_chrome)
        xdo.send_keysequence_window(win_id_chrome, "ctrl+r")
        sleep(0.1)
        xdo.send_keysequence_window_up(win_id_chrome, "ctrl+r")

    def back_to_origional(win_id_to_back):
        xdo.activate_window(win_id_to_back)

    def perform_reload(win_id_browser, win_id_editor):
        from datetime import datetime

        print('reloading %s' % datetime.now().strftime('%s'))
        reload_browser(win_id_browser)
        back_to_origional(win_id_editor)
        for i in range(0,3):
            xdo.send_keysequence_window(win_id_chrome, "Escape")
            xdo.send_keysequence_window(win_id_vscode, "Escape")

    class Reload (Exception):
        pass


    class EventHandler(pyinotify.ProcessEvent):

        def process_IN_CREATE(self, event):
            target = os.path.join(event.path, event.name)
            if os.path.isdir(target):
                raise Reload()

        def process_IN_DELETE(self, event):
            raise Reload()

        def process_IN_CLOSE_WRITE(self, event):
            target = os.path.join(event.path, event.name)
            if target.find('php')> 0:
                perform_reload(win_id_chrome, win_id_vscode)

    excl_lst = ['']
    excl = pyinotify.ExcludeFilter(excl_lst)

    print('start monitoring')
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler, read_freq=2)
    wdd = wm.add_watch(CWD, mask, rec=True, auto_add=True)

    notifier.loop()
