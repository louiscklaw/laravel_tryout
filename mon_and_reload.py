#!/usr/bin/env python3

import os,sys
import pyinotify
from xdo import Xdo
from pprint import pprint
from time import sleep

from datetime import datetime

wm = pyinotify.WatchManager()  # Watch Manager
mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE # watched events

PROJ_HOME = '/home/logic/_workspace/laravel_tryout/app/blog/'
incl_fileext_list=['php','htm']
incl_dir_list=[
    PROJ_HOME+'routes',
    PROJ_HOME+'resources/views'
]

xdo = Xdo()
# win_id = xdo.search_windows('.+Chromium.+')

print('click chrome window to get win_id_vscode')
win_id_vscode = xdo.select_window_with_click()
# win_id_vscode = xdo.get_active_window()
print('click chrome window to get win_id_chrome')
win_id_chrome = xdo.select_window_with_click()

CWD = os.path.dirname(os.path.abspath(__file__))
# CWD = '/home/logic/_workspace/laravel_tryout/app/blog'

def get_target_log_line(string_input):
    return string_input.replace(PROJ_HOME,'$HOME/')

def get_utf8_string(string):
    # return string
    return string.encode('utf-8')

def reload_browser(win_id_chrome):
    xdo.activate_window(win_id_chrome)

    sleep(0.1)
    for i in range(0,3):
        xdo.send_keysequence_window(win_id_chrome, get_utf8_string('Escape'))

    sleep(0.1)
    xdo.send_keysequence_window_down(win_id_chrome, get_utf8_string('Control_L+r'))
    xdo.send_keysequence_window_up(win_id_chrome, get_utf8_string('Control_L+r'))
    # xdo.send_keysequence_window_up(win_id_chrome, get_utf8_string('Control_L+r'))

def back_to_original(win_id_to_back):
    xdo.activate_window(win_id_to_back)

def clear_holding_key(win_id_browser, win_id_editor):
    for i in range(0,5):
        xdo.send_keysequence_window(win_id_browser, get_utf8_string('Escape'))
        xdo.send_keysequence_window_up(win_id_browser, get_utf8_string('Control_L'))
        xdo.send_keysequence_window_up(win_id_editor, get_utf8_string('r'))

def perform_reload(win_id_browser, win_id_editor):
    reload_browser(win_id_browser)
    back_to_original(win_id_editor)
    # clear_holding_key(win_id_browser, win_id_editor)

        # pass

class Reload (Exception):
    pass


class EventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        # target = os.path.join(event.path, event.name)
        # if os.path.isdir(target):
        #     raise Reload()
        pass

    def process_IN_DELETE(self, event):
        # raise Reload()
        pass

    def process_IN_CLOSE_WRITE(self, event):
        sleep(0.5)
        target = os.path.join(event.path, event.name)
        for incl_dir in incl_dir_list:
            if target.find(incl_dir) >= 0:
                for incl_fileext in incl_fileext_list:
                    if target.find(incl_fileext)>= 0:
                        logline = 'reload triggered for {} reloading {} ... '.format(target, datetime.now().strftime('%s'))
                        print(get_target_log_line(logline), end='')
                        perform_reload(win_id_chrome, win_id_vscode)
                        print(', reload done')

                        break
                    else:
                        logline='ignore file change for {}'.format(target)
                        print(get_target_log_line(log_line))
                break
            else:
                pass

# excl_lst = ['']
# excl = pyinotify.ExcludeFilter(excl_lst)


print('start monitoring...')
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler, read_freq=2)
wdd = wm.add_watch(CWD, mask, rec=True, auto_add=True)

notifier.loop()
