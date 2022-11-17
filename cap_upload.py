import usocket
import socket
import camera
import network

id = 'Qiming.Z'
passw = 'zhangqiming'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(id, passw)  #输入用户名和密码
    while not wlan.isconnected():
         pass
print('网络配置:', wlan.ifconfig())

# 连接Onenet
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("api.heclouds.com",80))

# 初始化摄像头
camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)
# 拍照
img = camera.capture()
# 关闭初始化
camera.deinit()
# 拍照成功会返回img字节数，失败则会报错
print(len(img))

# 发送图片数据给Onenet
head = f'''
POST /bindata?device_id=983835035&datastream_id=img HTTP/1.1
HOST: api.heclouds.com
api-key:y8CKgPcEm1y5HST3uPuA5eZld9I=
Content-length:{len(img)}

'''

client.send(head.encode())
client.send(img)
res = client.recv(1024)

client.close()
print(res)
