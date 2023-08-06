import base64
import time
import signal
import threading

from store import *
from xy_pb import *
from utils import *

def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner

@singleton
class User(object):
    logined = False
    store = Store()
    login_data = None

    def __init__(self):
        self.logined = False

    def checkLoginStatus(self):
        self.login_data = self.store.read()
        if "uid" in self.login_data and "token" in self.login_data:
            uid = self.login_data["uid"]
            token = self.login_data["token"]
            if uid and token:
                self.logined = True
                return True
            
        self.logined = False        
        
    def isLogin(self):
        return self.logined

    def loginIfNeed(self):
        self.checkLoginStatus()
            
        if self.isLogin() == False:
            #need login
            uuid = generate_unique_id()
            logincode = GetQrcodeLoginCode(uuid)
            if logincode:
                logincode_encoded = base64.b64encode(bytes(logincode, 'utf-8')).decode('utf-8').replace("==","fuckEqual")
                qrcode = f"https://main_page.html?action=scan&code={logincode_encoded}&deviceCode=143383612&deviceId={uuid}"
                displayQrcode(qrcode)
                self.checkLoginComplate(logincode, uuid)


    def checkLoginComplate(self, qrcode, uuid):
        print("loop check login~~~")
        rst = CheckLoginLoop(qrcode, uuid)
        if rst == 1: #success
            print("login success")
            self.logined = True
        elif rst == -1:
            threading.Timer(1, self.checkLoginComplate, (qrcode, uuid, )).start()
        else: #fail
            print("login fail !!!")