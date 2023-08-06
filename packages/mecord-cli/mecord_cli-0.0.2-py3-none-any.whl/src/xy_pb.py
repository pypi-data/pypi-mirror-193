import json
import hashlib
import time
import requests

from uauth_common_pb2 import *
from uauth_ext_pb2 import *
from aigc_ext_pb2 import *
from rpcinput_pb2 import *
from store import *
from utils import *

uuid = generate_unique_id()

def _aigc_post(request, function):
    return _post(url="https://mecord-beta.2tianxin.com/proxymsg", 
                 objStr="mecord.aigc.AigcExtObj", 
                 request=request, 
                 function=function)
    
def _common_post(request, function):
    return _post(url="https://mecord-beta.2tianxin.com/proxymsg", 
                 objStr="mizacommon.uauth.AuthExtObj", 
                 request=request, 
                 function=function)
    
def _post(url, objStr, request, function):
    req = request.SerializeToString()
    opt = {
        "lang": "zh-Hans",
        "region": "CN",
        "appid": "80",
        "application": "mecord",
        "version": "1.0",
        "X-Token": "1.0",
    }
    input_req = RPCInput(obj=objStr, func=function, req=req, opt=opt)
    res = requests.post(url=url, data=input_req.SerializeToString())
    pb_rsp = RPCOutput()
    pb_rsp.ParseFromString(res.content)
    if pb_rsp.ret == 0:
        return pb_rsp.rsp
    else:
        print(pb_rsp)
        return ""
    

def GetQrcodeLoginCode():
    req = GetQrcodeLoginCodeReq()
    req.login_type = UauthLoginType.LT_QRCODE_SCAN
    req.device_type = UauthDeviceType.DT_WINDOWS_PC
    req.device_id = uuid
    req.u_meng_device_id = ""

    rsp = GetQrcodeLoginCodeRes()
    rsp.ParseFromString(_common_post(req, "GetQrcodeLoginCode"))
    s = rsp.login_code
    return s

def CheckLoginLoop(code):
    req = GetQrcodeLoginStatusReq()
    req.login_code = code
    req.device_id = uuid
    req.u_meng_device_id = ""

    rsp = GetQrcodeLoginStatusRes()
    rsp.ParseFromString(_post("mizacommon.uauth.AuthExtObj", req, "GetQrcodeLoginStatus"))
    if rsp.status == GetQrcodeLoginStatus.SUCCESS:
        store = Store()
        data = store.read()
        data["uid"] = rsp.commonSignInRes.user_id
        data["token"] = rsp.commonSignInRes.login_token
        data["nickname"] = rsp.userNickname
        data["icon"] = rsp.userIconUrl
        store.write(data)
        return 1
    elif rsp.status == GetQrcodeLoginStatus.EXPIRED or rsp.status == GetQrcodeLoginStatus.CANCEL:
        return 0
    else:
        return -1
    
    
def GetTask():
    req = GetTaskReq()
    req.DeviceKey = uuid
    req.limit = 1

    rsp = GetTaskRes()
    rsp.ParseFromString(_aigc_post(req, "GetTask"))
    datas = []
    for it in rsp.list:
        datas.append({
            "taskId": it.taskId,
            "taskUUID": it.taskUUID,
            "config": it.config,
            "data": it.data,
        })
    return datas

def TaskNotify(taskUUID, status, msg, data):
    req = TaskNotifyReq()
    req.taskUUID = taskUUID
    if status:
        req.taskStatus = TaskStatus.TS_Success
    else:
        req.taskStatus = TaskStatus.TS_Failure
    req.failReason = msg
    req.data = data

    rsp = TaskNotifyRes()
    rsp.ParseFromString(_post("mizacommon.aigc.AigcExtObj", req, "TaskNotify"))
    return True

# def RegisterDevice():
#     req = RegisterDeviceReq()
#     req.deviceKey = uuid
#     req.deviceInfo = ""
#     req.groupId = 0

#     rsp = RegisterDeviceRes()
#     rsp.ParseFromString(_post("mecord.aigc.AigcExtObj", req, "RegisterDevice"))
#     return True

def UploadWidget():
    req = UploadWidgetReq()
    req.login_type = UauthLoginType.LT_QRCODE_SCAN
    req.device_type = UauthDeviceType.DT_WINDOWS_PC
    req.device_id = uuid
    req.u_meng_device_id = ""

    rsp = UploadWidgetRes()
    rsp.ParseFromString(_post("mizacommon.aigc.AigcExtObj", req, "GetTask"))
    s = rsp.login_code
    return s