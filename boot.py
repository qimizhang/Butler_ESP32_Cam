# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
webrepl.start()
nid = 'Qiming.Z'
passw = 'zhangqiming'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(nid, passw)  #输入用户名和密码
    while not wlan.isconnected():
         pass
print('网络配置:', wlan.ifconfig())