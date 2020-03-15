# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:24:19 2020

@author: user
"""
from pyfcm import FCMNotification
 
push_service = FCMNotification(api_key="AIzaSyAVY7bvJJPgSigp3pTs_rR_bP__j2KuGYA")
 
# OR initialize with proxies
 
proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "https://127.0.0.1",
        }
push_service = FCMNotification(api_key="AIzaSyAVY7bvJJPgSigp3pTs_rR_bP__j2KuGYA", proxy_dict=proxy_dict)
 
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
 
registration_id = "dz58Yid-SmuoKhbowTZ5zj:APA91bGDBemSA1-_YnjmOBm1PiuPpZ1A5-dYMvUTNckHUpPrElRtEDJBu1ZipV0rBmBn1msbHbSH-OkV_Vwz03Myfez0EInuFrySHF3Vx_qOeGXV4gbG0qtQ8M_c0pzVVkLUkJN0434j"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
 
print(result) 
 
# Send to multiple devices by passing a list of ids.
registration_ids = ["dz58Yid-SmuoKhbowTZ5zj:APA91bGDBemSA1-_YnjmOBm1PiuPpZ1A5-dYMvUTNckHUpPrElRtEDJBu1ZipV0rBmBn1msbHbSH-OkV_Vwz03Myfez0EInuFrySHF3Vx_qOeGXV4gbG0qtQ8M_c0pzVVkLUkJN0434j"]
message_title = "Uber update"
message_body = "Hope you're having fun this weekend, don't forget to check today's news"
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
print(result) 
