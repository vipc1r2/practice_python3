# coding:utf-8
import json

import requests
# 抓接口，请求中的Content-Type: application/json

url = "https://app.xxx/list"  # 接口地址

# 消息头数据
headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'User-Agent': 'xxx',
    'Referer': 'xxx',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-cn',
    # 'Cookie': '省略',

    }

data= {"userId" : "",
      "minitorFlag" : "0",
      "lastUpdateTime" : "1603272159122",
      "tokenId" : "8b57913903ae46218f15a88429c77b6d"
           }

# verify = False 忽略SSH 验证
# 字典转换为字符串
# r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
r = requests.post(url, json=data, headers=headers, verify=False) # 直接json=来代替
r.encoding = 'utf-8'
print(r.json())
