#!/usr/bin/env python3

import os,sys
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

def get_utf8_string(string):
    # return string
    return string.encode('utf-8')

def reload_browser(win_id_chrome):
    xdo.activate_window(win_id_chrome)

    sleep(0.1)
    for i in range(0,3):
        xdo.send_keysequence_window(win_id_chrome, get_utf8_string('Escape'))

    sleep(0.1)
    for i in range(0,3):
        xdo.send_keysequence_window(win_id_chrome, get_utf8_string('Control_L+r'))
        xdo.send_keysequence_window_up(win_id_chrome, get_utf8_string('Control_L+r'))

def back_to_original(win_id_to_back):
    xdo.activate_window(win_id_to_back)

def clear_holding_key(win_id_browser, win_id_editor):
    for i in range(0,5):
        xdo.send_keysequence_window(win_id_browser, get_utf8_string('Escape'))
        xdo.send_keysequence_window_up(win_id_browser, get_utf8_string('Control_L'))
        xdo.send_keysequence_window_up(win_id_editor, get_utf8_string('r'))

def perform_reload(win_id_browser, win_id_editor):
    from datetime import datetime

    print('reloading %s' % datetime.now().strftime('%s'))
    reload_browser(win_id_browser)
    back_to_original(win_id_editor)
    clear_holding_key(win_id_browser, win_id_editor)
    print('reload done')
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
        target = os.path.join(event.path, event.name)
        for incl_fileext in incl_fileext_list:
            if target.find(incl_fileext)> 0:
                perform_reload(win_id_chrome, win_id_vscode)
                break
            else:
                print('ignore file change for {}'.format(event.path))

# excl_lst = ['']
# excl = pyinotify.ExcludeFilter(excl_lst)

incl_fileext_list=['php','htm']


print('start monitoring...')
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler, read_freq=1)
wdd = wm.add_watch(CWD, mask, rec=True, auto_add=True)

notifier.loop()
