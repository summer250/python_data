# coding:utf-8

import re
import requests
from lxml import etree
from scrapy import Selector

url = 'https://maoyan.com/board/4?offset=0'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
print(response)
response.encoding = 'utf-8'
html_selector = Selector(response)

href_list = html_selector.xpath('//*[@class="board-wrapper"]/dd/a/@href').getall()
print(href_list)
headers_detail = {

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__mta=256613684.1591601583785.1591607939529.1591608081007.9; uuid_n_v=v1; uuid=9636DE50A85B11EA8DBBB14E32910CB60065AC7E2E2B4A76BB4A8FFB8C43D40F; _lxsdk_cuid=1728c53a700c8-0529e96e666bfc-f7d1d38-1fa400-1728c53a700c8; _lxsdk=9636DE50A85B11EA8DBBB14E32910CB60065AC7E2E2B4A76BB4A8FFB8C43D40F; mojo-uuid=dae794df5d2e70e25a0a963a970df702; _csrf=78be7313c20991f0bc4ce6a986a4c25010d2afbeb8388958055dae69dc6a6ff6; mojo-session-id={"id":"a47479a25dad2d019bc0b205911a0532","time":1591607011046}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; lt=ZCJQ5fTeRO-kBn5J5E8HvoKtE_sAAAAAywoAAG39vgYj1TV2YYTS0Go66uxJRZC3StUsMTHFTRjnmSQsnPdqLYpSR0N90AoE20F-CA; lt.sig=H3XlcDDGyGLtF8iv1k8T2qFuB80; mojo-trace-id=14; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1591601705,1591607011,1591607061,1591608081; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1591608081; _lxsdk_s=172932ba785-38e-d2b-28c%7C%7C23',
    'Host': 'maoyan.com',
    'Referer': 'https://passport.meituan.com/account/secondverify?response_code=a00de3474bdc4f9a82ee4059ad255d21&request_code=69576c0635084586a29448388cf0262f',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',



}
for href in href_list:
    href = 'https://maoyan.com' + href

    response_detail = requests.get(url=href, headers=headers_detail)
    print(response_detail.url)
    html_detail_selector = Selector(response_detail)
    # print(html_detail_selector)

    Title = html_detail_selector.xpath('//*[@class="movie-brief-container"]/h1')
    print(Title)
























