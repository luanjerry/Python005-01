# 使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件

import requests
from lxml import etree
import json
from time import sleep
from fake_useragent import UserAgent


def getInfoWithUrl(film_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent':user_agent}
    try:
        response = requests.get(film_url, headers=header)
        selector = etree.HTML(response.text)
        print(response.text)

        user_name = selector.xpath('//div[@class="AuthorInfo-head"]/span/div/div/a')

        print(user_name)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/383494692'
    getInfoWithUrl(url)
