这些是已经烧进esp 32 cam的代码

必要的文件有lib是micropython的package, boot.py, label_upload.py, test_weight.py

boot.py是esp32是上电之后会运行的，相当于setup函数进行初始化，功能相当于连接wifi

label_upload.py包含和google api通信获得label的函数，上传Onenet的函数

test_weight.py是检测重量变化函数，应该作为我们的主循环函数，还未完善，调用hx711时候有一些错误

