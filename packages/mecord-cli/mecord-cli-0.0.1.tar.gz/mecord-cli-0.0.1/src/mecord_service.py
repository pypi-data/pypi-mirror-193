import os
import sys
import time
import signal
import subprocess

from xy_socket import *
from store import *
from xy_pb import *
from xy_user import *
from utils import *

class BaseService:
    def __init__(self, name, pid_file=None):
        self.name = name
        self.pid_file = pid_file
        self.running = False
        self.halt = False

    def start(self):
        self.halt = False
        if self.pid_file:
            with open(self.pid_file, 'w') as f:
                f.write(str(os.getpid()))
        self.running = True
        signal.signal(signal.SIGTERM, self.stop)
        self.run()

    def run(self):
        pass

    def stop(self, signum=None, frame=None):
        self.running = False
        if self.pid_file and os.path.exists(self.pid_file):
            os.remove(self.pid_file)

    def restart(self):
        self.stop()
        time.sleep(1)
        self.start()

    def is_running(self):
        if self.pid_file and os.path.exists(self.pid_file):
            with open(self.pid_file, 'r') as f:
                pid = int(f.read())
                try:
                    os.kill(pid, 0)
                except OSError:
                    return False
                else:
                    return True
        else:
            return self.running

class MecordService(BaseService):
    def __init__(self):
        pid_file = '/var/run/MecordService.pid' if sys.platform != 'win32' else None
        super().__init__("MecordService", pid_file)
        # self.socket = MecordSocket(self.receiveData)
        # self.socket.start()

    def receiveData(self, s):
        print(s)

    def executeLocalPython(self, cmd, params):
        params_str = json.dumps(params, separators=(',', ':')).replace('"', r'\"')
        command = f'"{sys.executable}" "{cmd}" --run "{params_str}"'
        result = subprocess.run(command, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        return result.stdout.decode(encoding="utf8", errors="ignore")

    def run(self):
        while self.running:
            cmd = "E:\\aigc\mecord_python\module_sd\main.py"
            params = {
                "taskid": "t42342354",
                "group_id": 12345,
                "h5_task_info": {
                    "widget_id": 111,
                    "fn_name": "txt2img",
                    "param": {
                        "prompt":"adog",
                        "steps": 20,
                        "wdith": 512,
                        "height": 512,
                    }
                },
                "widget": {
                    "version": "1.0",
                    "name": "SD1.5widget",
                    "cmd": "",
                    "group_id": "",
                    "widget_id": 1111
                }
            }
            result_json = self.executeLocalPython(cmd,params)
            result_obj = json.load(result_json)
            TaskNotify("1111", 
                        result_obj.status, 
                        result_obj.message, 
                        result_obj.result)
            # datas = GetTask()
            # for it in datas:
            #     result_json = executeLocalPython(cmd,params)
            #     result_obj = json.load(result_json)
            #     TaskNotify(it.taskUUID, 
            #                 result_obj.status, 
            #                 result_obj.message, 
            #                 result_obj.result)
            
            time.sleep(10)

    def status_ok(self):
        service_running = super()._is_running()
        socket_running = True #self.socket.isRunning()
        is_login = User().isLogin()
        return socket_running and service_running and is_login