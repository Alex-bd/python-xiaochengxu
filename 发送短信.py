#!D:/CODE/python
# -*- coding: utf-8 -*-
# @Time : 2020/5/8 16:21
# @Author : Alexdong
# @Site : 
# @File : 发送短信.py
# @Software: PyCharm
# Functional description: 通过互亿无线的API，实现发送短信功能
#
import urllib.parse
import http.client
import json


def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号APIID和对应的APIKEY
    params = urllib.parse.urlencode({'account': 'C14698927', 'password': 'APIKEY', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '18668959765', 'format':'json' })
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    # 请求示例：http://106.ihuyi.com/webservice/sms.php?method=Submit&account=APIID&password=APIKEY&mobile=手机号码&content=您的验证码是:1234。请不要把验证码泄露给其他人。
    conn.request('POST', sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    jsonstr = response_str.decode('utf-8')
    # 打印发送回执
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()