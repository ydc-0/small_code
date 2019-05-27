import inspect

from urllib import request
import chardet


def open_url(url):
    req = request.Request(url)
    response = request.urlopen(req)
    # response = request.urlopen(url)

    # print(type(response))
    # for m in inspect.getmembers(type(response)):
    #     print(m)

    # here is html source
    data = response.read()
    charset = chardet.detect(data)
    # print(charset)
    # data = data.decode("utf-8")
    data = data.decode(charset.get('encoding'))
    print(data)

    print('**********************************************')
    print("info打印信息：%s" % (response.info()))
    print('**********************************************')
    print("geturl打印信息：%s" % (response.geturl()))
    print('**********************************************')
    print("getcode打印信息：%s" % (response.getcode()))

open_url("http://www.baidu.com")

