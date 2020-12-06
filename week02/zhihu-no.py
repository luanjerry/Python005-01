# 使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件

import requests
from lxml import etree
import json
from time import sleep
from fake_useragent import UserAgent
import pandas as pd


def smzdm_get():
    ua = UserAgent(verify_ssl=False)
    header = {'user-agent': ua.random,
              'Referer': 'https://www.smzdm.com/'}

    url = 'https://www.smzdm.com/fenlei/diannaozhengji/'
    r = requests.get(url, headers=header)

    selector = etree.HTML(r.text)
    name_type = selector.xpath('//div[@class="z-feed-content "]/h5/a/text()')
    money = selector.xpath('//div[@class="z-highlight"]/a/text()')
    link = selector.xpath('//div[@class="z-feed-content "]/h5/a/@href')

    data = pd.DataFrame(index=[i for i in range(30)])
    data['商品名称'] = ''
    data['价格'] = ''
    data['连接'] = ''

    path = './html_get/'
    for i in range(30):
        data['商品名称'].loc[i] = name_type[i]
        data['价格'].loc[i] = money[i].strip().lstrip()
        data['连接'].loc[i] = link[i]
        if data['价格'].loc[i] == '':
            data['价格'].loc[i] = "商品下架过期"

    data.to_excel(path+'什么值得买_电脑类.xlsx')


if __name__ == '__main__':
    smzdm_get()



# 知乎 ，反爬太牛了。

"""
def getInfoWithUrl(film_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent':user_agent}
    try:
        response = requests.get(film_url, headers=header)
        selector = etree.HTML(response.text)
        #print(response.text)
        # 用户名
        
        #a=[]
        #b=[]
        #for i in range()
        
        #user_name = selector.xpath('//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div/div/div/div/div/div/span/div/div')
        #  --一直没有成功，
        user_name = selector.xpath('//div[@class="AuthorInfo-head"]/span/div/div/a')
        #//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[3]/div
        print(user_name)
        #print(type(user_name[0]))
        #["authorName"]
        #user_name = selector.xpath('//a[@class="a_underline user_name"]/span[1]/text()')
        #//*[@id="QuestionAnswers-answers"]/div/div/div/div[2]/div/div[2]/div
        #//*[@id="Popover37-toggle"]/a
        #//*[@id="Popover39-toggle"]/a
        #/html/body/div[1]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/div[1]/div/div[1]/span/div/div/a

        # 获取用户评论
        #user_comment = selector.xpath('//p/span[@itemprop="description"]/text()')

        # zip方法 将两个列表进行一对一的关联  dict-将结果强制转换为字典类型
        #film_info = dict(zip(user_name, user_comment))
        #filename='comments.json'
        #with open(filename,'w', encoding='utf-8') as file_obj:
          #  json.dump(film_info,file_obj)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/383494692'
    
    getInfoWithUrl(url)  """
 
    