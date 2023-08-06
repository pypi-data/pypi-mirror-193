#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    LLMApi
    
    OpenAPI for Large Language Models

    :date:      02/22/2023
    :author:    llmapi <llmapi@163.com>
    :homepage:  https://github.com/llmapi/
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2023 llmapi. All rights reserved
"""
from __future__ import unicode_literals
import sys
import json
import re
import argparse as ap
import getpass

__name__ = 'llmapi'
__version__ = '1.0.2'
__description__ = 'LLMs API'
__keywords__ = 'LLM OpenAPI LargeLanguageModel'
__author__ = 'llmapi'
__contact__ = 'llmapi@163.com'
__url__ = 'https://github.com/llmapi/'
__license__ = 'MIT'

import requests
import time
import json

def _is_json(jstr:str)->bool:
    try:
        jsobj = json.loads(jstr)
    except ValueError:
        return False
    return True

def _make_post(url,content):
    res = requests.post(url, data = json.dumps(content))
    try:
        rep = res.json()
        return rep
    except Exception:
        return {'code':-1,'msg':'request failed'}

def _get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

class LLMApi():
    def __init__(self, host='https://api.llmapi.online', bot_type:str = 'mock'):
        self.host = host
        self.token = ''
        self.session = ''
        self.chat_stub = ''
        self.bot_type = bot_type

    def __del__(self):
        if self.token != '':
            self.logout(self.token)
 
    def _start_session(self)->dict:
        url = self.host + '/v1/chat/start'
        timestamp = _get_time()
        content = {'token':self.token, 'bot_type':self.bot_type, 'timestamp':timestamp}
        return _make_post(url,content)
 
    def _end_session(self)->dict:
        url = self.host + '/v1/chat/end'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp}
        return _make_post(url,content)

    def login(self, email:str, password:str)->bool:
        url = self.host + '/v1/login'
        content = {'email':email, 'password':password}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            self.token = rep['token']
            rep = self._start_session()
            if rep['code'] == 0:
                self.session = rep['session']
                return True

        print(rep['msg'])
        return False
 
    def logout(self)->bool:
        self._end_session()
        url = self.host + '/v1/logout'
        content = {'token':self.token}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            return True
        print(rep['msg'])
        return False

    def chat_send(self, prompt:str)->bool:
        url = self.host + '/v1/chat/send'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp, 'content':prompt}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            self.chat_stub = rep['stub']
            return True
        print(rep['msg'])
        return False
 
    def chat_recv(self):
        url = self.host + '/v1/chat/recv'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp, 'stub':self.chat_stub}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            if _is_json(rep['reply']):
                return json.loads(rep['reply'])
            else:
                return rep['reply']
        print(rep['msg'])
        return False
                       
    def chat_sync(self, prompt:str):
        url = self.host + '/v1/chat/sync'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp, 'content':prompt}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            if _is_json(rep['reply']):
                return json.loads(rep['reply'])
            else:
                return rep['reply']
        print(rep['msg'])
        return False
    def __str__(self):
        print(f"| [host]:{self.host}")
        print(f"| [token]:{self.token}")
        print(f"| [session]:{self.session}")
        print(f"| [stub]:{self.chat_stub}")
        print(f"| [bot_type]:{self.bot_type}")
        return ""
   
                                       
def _parse_arg():
    parse = ap.ArgumentParser(description="OpenApi for Large Language Models.")
    parse.add_argument('--host', type=str, default = 'https://api.llmapi.online', help='LLMApi server host.')
    parse.add_argument('--bot', type=str, default = 'mock', help='Choose which type of LLM bot you want to talk with.')
    arg = parse.parse_args()
    return arg

def main():
    arg = _parse_arg()

    print("Input your account email:")
    email = input()
    pd = getpass.getpass("Input your account password:")

    client = LLMApi(arg.host, arg.bot)
    ret = client.login(email,pd)
    if ret == False:
        exit()

    print("---------------------------------")
    print(f" Start talking with {arg.bot}.")
    print("  Press 'Ctrl+C' to quit.")
    print("---------------------------------")
    while True:
        print("Input your word (press 'Enter' key to send):")
        while True:
            prompt = input()
            if prompt != "":
                break

        print(f"Bot [{arg.bot}]:")
        rep = client.chat_sync(prompt=prompt)
        print(rep)

if __name__ == '__main__':
    main()
