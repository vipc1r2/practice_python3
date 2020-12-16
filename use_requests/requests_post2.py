import unittest
import requests
import urllib3
# 抓接口，请求的Content-Type: application/x-www-form-urlencoded，利用unittest框架实现例子

class TestMe(unittest.TestCase):

# 文章详情页
    def setUp(self):

        self.headers = {'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'MZDailyNewspaper/14757.2.0 (iPhone; iOS 13.5.1; Scale/3.00)',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-Hans-US;q=1, en-US;q=0.9',
                        # 'Cookie': 'xxx'

                        }

    def test__1_me_myfavorites(self):  #详情页
        url = 'https://app.xxx'

        # 请求报文数据，格式为name1=value1&name2=value2
        requestJSONdata='article_id=6050440&channel=app&version=7.2.0'
        requestJSONdata = str(requestJSONdata).replace("+", "%2B")
        requestdata = requestJSONdata.encode("utf-8")

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # 解决Python3 控制台输出InsecureRequestWarning的问题
        res = requests.post(url=url, data=requestdata, headers=self.headers, verify=False)
        res.encoding = 'utf-8'
        self.assertIn('"errorCode":"0"', res.text)  # 断言
        print(res.json())



if __name__ == '__main__':
    unittest.main()