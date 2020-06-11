# coding:utf-8
import requests
import re
from scrapy import Selector

url = 'https://book.douban.com/subject/1449351/'

headers = {
    'Cookie': 'bid=_KHFG-WCJbA; douban-fav-remind=1; ll="118226"; __gads=ID=492520f31122d9a0:T=1580559240:S=ALNI_Maj6ymXdwMik-J-HobB9hgHva3clg; _vwo_uuid_v2=D7AC19594013DE5488BDA18375DF42F21|57f1fc2f1c3102934c37ef376ca78a0b; push_doumail_num=0; push_noty_num=0; __utmv=30149280.4746; ct=y; __utmz=81379588.1591690293.1.1.utmcsr=link.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; gr_user_id=25bb053b-201d-499a-8c8a-cff85264d0d8; __yadk_uid=iBYWmIaUhYdRBK74RzJ2rJQUW7Xd2fQN; dbcl2="47464892:FaTRAKfw80A"; ck=MCT3; __utma=30149280.1657616189.1571035832.1591790234.1591836623.46; __utmc=30149280; __utmz=30149280.1591836623.46.38.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1591836626%2C%22https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fbook.douban.com%2Ftop250%22%5D; _pk_ses.100001.3ac3=*; __utma=81379588.1278044896.1591690293.1591790255.1591836626.8; __utmc=81379588; gr_cs1_aafae99b-4a29-492a-9fb0-792925e8ee7c=user_id%3A1; Hm_lvt_cfafef0aa0076ffb1a7838fd772f844d=1591748478,1591838096; Hm_lpvt_cfafef0aa0076ffb1a7838fd772f844d=1591838096; ap_v=0,6.0; __utmt_douban=1; __utmt=1; _pk_id.100001.3ac3=ef224cf0e004e840.1591690294.8.1591838554.1591790356.; __utmb=30149280.18.10.1591836623; __utmb=81379588.16.10.1591836626',
    'Host': 'book.douban.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',

}


response = requests.get(url=url, headers=headers)
selector_detail = Selector(response)


ISBN = re.findall('<span class="pl">ISBN:</span>(.*?)<br/>', response.text)
print(ISBN)

Content = selector_detail.xpath('//*[@id="link-report"]/span[2]/div/div/p/text()').extract_first()
print(Content)
if Content == None:
    Content = selector_detail.xpath('//*[@id="link-report"]/div[1]/div/p/text()').extract()
    print('*****************')
    print(Content)
    print('*****************')
    print(Content[0])
    print('*****************')
    print(Content[-1])

else:
    print(Content)

# Series = re.findall('<span class="pl">丛书:</span>&nbsp;<a href=".*?">(.*?)</a><br>', response.text)
# # print("丛书：" + "".join(Series))
# print(Series)
# # book_list.append(Series)
