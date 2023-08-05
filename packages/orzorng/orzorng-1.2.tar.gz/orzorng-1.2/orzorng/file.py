# -*- coding: utf-8 -*-

import os


def file_exists(file_name, default=''):
    if not os.path.exists(file_name) or not os.path.getsize(file_name):
        file_write(file_name, default)
        return False

    return True


def file_write(file_name, data='', method='w'):
    with open(file_name, method, encoding='utf-8') as f:
        f.write(data)


def file_read(file_name, default=''):
    data = ''
    if file_exists(file_name, default):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read()

    return data


def file_get_line(file_name):
    return file_read(file_name).splitlines()


def file_set_line(file_name, data):
    file_write(file_name, '\n'.join(data), 'w+')
