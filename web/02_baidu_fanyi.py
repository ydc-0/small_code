import inspect
import json
import re

from urllib import request
from urllib import parse
import chardet


def fanyi(words):
    # detect the language type
    req_url = 'https://fanyi.baidu.com/langdetect'
    data_dict = {'query': words}
    req_data = parse.urlencode(data_dict).encode('utf-8')
    response = request.urlopen(req_url, req_data)

    result = json.load(response)
    # result -> {'error': 0, 'msg': 'success', 'lan': 'en'}
    language_type = result['lan']
    print(language_type)

    # do translate
    req_url = 'https://fanyi.baidu.com/v2transapi'
    data_dict = {}
    data_dict['from'] = language_type
    data_dict['to'] = 'zh'
    data_dict['query'] = words
    data_dict['transtype'] = 'translang'
    data_dict['simple_means_flag'] = '3'
    data_dict['sign'] = '54706.276099'
    data_dict['token'] = '69cc3db9cdb045f2261f4470127eb036'

    req_data = parse.urlencode(data_dict).encode('utf-8')
    response = request.urlopen(req_url, req_data)

    print(response.read())
    # response -> b'{"error":997,"from":"en","to":"zh","query":"hello"}'

    # 解决办法：
    # 修改url为手机版的地址：http://fanyi.baidu.com/basetrans
    # User - Agent也用手机版的

    # so
    req_url = "https://fanyi.baidu.com/basetrans"
    data_dict = {
        "query": words,
        "from": language_type,
        "to": "zh",
    }
    req_header = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
    }
    req_data = parse.urlencode(data_dict).encode('utf-8')
    req = request.Request(req_url, data=req_data, headers=req_header)
    response = request.urlopen(req)
    print(response.read())
    # not work......
    # 网站反爬， sign 是 js 加密的。。。之后再研究

    # try Youdao Fanyi
    req_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data_dict = {
        "i": words,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15581011842430',
        # 'sign': '9be96f06aaf3c8d6b207901f7ce37408',
        # 'ts': '1558101184243',
        # 'bv': '327689fccf65d35fd25955c1807f5d2d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    req_header = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36",
    }
    req_data = parse.urlencode(data_dict).encode('utf-8')
    req = request.Request(req_url, data=req_data, headers=req_header)
    response = request.urlopen(req)
    print(response.read())
    # (╯‵□′)╯︵┻━┻  还是不能用


fanyi("hello")

