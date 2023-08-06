import requests
import time

def _make_post(url,content):
    res = requests.post(url, data = content,timeout=10)
    try:
        rep = res.json()
        return rep
    except Exception:
        return {'code':-1,'msg':'request failed'}

def _get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

class LLMApi():
    def __init__(self, host='127.0.0.1:5050', bot_type:str = 'mock'):
        self.host = host
        self.token = ''
        self.session = ''
        self.chat_stub = ''
        self.bot_type = bot_type

    def __del__(self):
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
        url = host + '/v1/logout'
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
 
    def chat_recv(self)->dict:
        url = self.host + '/v1/chat/recv'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp, 'stub':self.chat_stub}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            return rep['reply']
        print(rep['msg'])
        return False
                       
    def chat_sync(self, prompt:str)->dict:
        url = self.host + '/v1/chat/sync'
        timestamp = _get_time()
        content = {'token':self.token, 'session':self.session, 'timestamp':timestamp, 'content':prompt}
        rep = _make_post(url,content)
        if rep['code'] == 0:
            return rep['reply']
        print(rep['msg'])
        return False
                       
                                       
