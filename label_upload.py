
import ure
import urequests
import ubinascii
import usocket
import socket
import camera
import network
import os


# 和Google vision api 建立通信
URL = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBj8PHdWEB0XI0B99CpjMcPtu9GIPcgLak'
headers = {'Content-Type': "application/json"}


# make api call
def image_request(image_path):
    a = ubinascii.b2a_base64(image_path)
    payload = '{\"requests\":[{\"image\":{\"content\":\"' + a.decode \
        ('utf-8') + '"},\"features\":[{\"type\":\"OBJECT_LOCALIZATION\" }      ]    }  ]}'
    response = urequests.request("POST", URL, data=payload, headers=headers)
    return response.text

# 识别结果的函数
def reco_result(img_dir):
    strr = image_request(img_dir)
    print(type(strr))
    print(strr)
    return strr

# 进行相机初始化和拍照
camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
img = camera.capture()
camera.deinit()

print(len(img))

# 发给google得到识别结果
ress = reco_result(img)


# 识别结果传到Onenet
# upload result to onenet
url = "http://api.heclouds.com/devices/983835035/datapoints"
APIKEY = "YOo6Lq7ZTxpdIR5lsvl4I=7AtI8="

dict = {"datastreams":[{"id":"item_tag","datapoints":[{"value":50}]}]}
dict['datastreams'][0]['id'] = "item_tag"
dict['datastreams'][0]['datapoints'][0]['value'] = ress

s = json.dumps(dict)
headers = {
                "api-key":APIKEY,
           }
r = urequests.post(url,headers=headers,data = s)
print(r.content)
