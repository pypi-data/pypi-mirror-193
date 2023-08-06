# -*- coding: utf-8 -*-

import os
import time
import requests


def request_api(local_sql, action, data, timeout=120):
    try:
        res = requests.post(local_sql, dict({'action': action}, **data), timeout=timeout)
        # print('ok request_api', action, res.text)
        print('ok request_api', action)
        return res
    except Exception as get_err:
        print('err request_api', local_sql, action, get_err)
        time.sleep(1)
        return request_api(local_sql, action, data, timeout)


change_ip_time = 0


def change_ip(call_func=None):
    global change_ip_time
    # todo 切换 ip
    # return True
    change_ip_interval = 15
    change_ip_diff = int(time.time()) - change_ip_time
    if change_ip_diff < change_ip_interval:
        print('切换 ip 间隔过小', change_ip_diff)
        time.sleep(change_ip_interval - change_ip_diff)

    try:
        if os.name == "nt":
            if os.path.exists('宽带连接.txt'):
                with open('宽带连接.txt', 'r', encoding='utf-8') as kd_f:
                    kd_str = kd_f.read().strip()
                    if kd_str:
                        vps_username, vps_password = kd_str.split('|')

            os.system("rasdial %s /d" % ('宽带连接'))
            os.system("rasdial %s %s %s" % ('宽带连接', vps_username, vps_password))
        else:
            os.system('pppoe-stop')
            os.system('pppoe-start')

        change_ip_time = int(time.time())

        if call_func != None:
            if call_func():
                print('更換ip成功')
                return True
        else:
            print('更換ip成功')
            return True

    except Exception as e:
        print('更换ip失败: ', e)

    time.sleep(1)
    return change_ip()
