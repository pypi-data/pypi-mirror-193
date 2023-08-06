#!/usr/bin/env python
# -*- coding:utf8 -*-

import requests
import json


def iris(k1, k2, k3, k4):
    '''
    本函数用于调用serverless服务器的iris数据集预测功能
    '''
    data = {
            'k1': k1,
            'k2': k2,
            'k3': k3,
            'k4': k4,
            }
    r = requests.post('https://skl-mllesson-idtydidifk.cn-beijing.fcapp.run', json=data)
    if r.status_code == 200:
        result_raw = json.loads(r.text)
        result = result_raw['result']

        return result
    else:
        return 'ERROR: {}'.format(r.status_code)
