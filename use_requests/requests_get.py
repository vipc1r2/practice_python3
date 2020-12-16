import requests

# 无参数例子
# url = 'http://baidu.com'
# response = requests.get(url)
# print(response)

# 带参数的例子
url = 'https://www.baidu.com/s?'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
params = {"ie":"utf-8","mod":"1","isbd":"1",\
          "isid":"e2e01a2b0002b62c","ie":"utf-8",\
          "f":"3","rsv_bp":"1","rsv_idx":"2","tn":"baiduhome_pg",\
          "wd":"git%E6%95%99%E7%A8%8B","rsv_spt":"1","oq":"git","rsv_pq":"e2e01a2b0002b62c",\
          "rsv_t":"bd12H7iHt%2B1L9ZjnuMlB3%2BixYe9ESDnHaJvOQt06xUXMUD2J1GRHNA7SUt1Rl7K7QP0v",\
          "rqlang":"cn","rsv_enter":"0","rsv_dl":"ts_1","rsv_btype":"t","rsv_sug3":"55",\
          "rsv_sug1":"39","rsv_sug7":"100","rsv_sug2":"1","prefixsug":"git","rsp":"1",\
          "rsv_sug4":"4783","bs":"git","rsv_sid":"undefined","_ss":"1",\
          "clist":"fa07dc2c116bddf0%09fa07dc2c116bddf0%09fa07dc2c116bddf0","hsug":"","f4s":"1","csor":"5","_cr1":"39867"
          }
# get有参数，使用params
res = requests.get(url=url, params=params, headers=headers, verify=False)
res.encoding = 'utf-8'
print(res.text)


