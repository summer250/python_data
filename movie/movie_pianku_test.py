import time
import requests
import re
from scrapy import Selector
from lxml import etree
import json
import csv



url = 'https://www.pianku.tv/mv/------2.html'
headers = {

    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'Hm_lvt_5a21a69d1b034aed24dcda25771e8135=1591450572,1591491865,1591575840,1591587930; PHPSESSID=ri8b4ipgq4rejjhsfl4ntjdq25; Hm_lpvt_5a21a69d1b034aed24dcda25771e8135=1591592845',
    'if-none-match': 'W/"e8e333c5"',
    'referer': 'https://www.pianku.tv/s/_E5_8F_98_E8_89_B2_E9_BE_99.html',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',

}
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    html = response.text
    # print(html)
    items = re.findall('<a href="(.*?)" title=', html)
    for item in items:
        # new_list = []
        href = 'https://www.pianku.tv' + item

        response_detail = requests.get(url=href, headers=headers)
        print(response_detail.apparent_encoding)
        response_detail.encoding = response_detail.apparent_encoding













        html_detail_etree = etree.HTML(response_detail.text)
        html_detail_selector = Selector(response_detail)
        # print(html_detail_etree)
        # print(html_detail_selector)

        title = html_detail_etree.xpath('//*[@class="main-ui-meta"]/h1/text()')[0]
        print('影片名：' + title)
        # new_list.append(title)

        author = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[2]/a/text()')[0]
        print('导演：' + author)
        # new_list.append(author)
        # list.append(author)
        #
        # # screenwriter = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[3]/a/text()')[0]
        # # # print('编剧：'+str(screenwriter))
        # # list.append(screenwriter)
        # #
        # # starring = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[4]/a/text()')[0]
        # # # print('主演：'+str(starring))
        # # list.append(starring)
        # #
        # # types_of = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[5]/a/text()')[0]
        # # # print('类型：'+str(types_of))
        # # list.append(types_of)
        # #
        # # area = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[6]/a/text()')[0]
        # # # print('地区'+str(area))
        # # list.append(area)
        # # language = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[7]/a/text()')[0]
        # # print('语言'+str(language))
        # # list.append(str(language))
        # #
        # # release_time = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[8]/text()')[0]
        # # print('上映时间'+str(release_time))
        # # list.append(str(release_time))
        #
        # # length = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[9]/text()')
        # # print('片长'+str(length))
        # # aka = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[10]/text()')
        # # print('又名'+str(aka))
        # # score = html_detail_etree.xpath('//*[@class="main-ui-meta"]/div[11]/div/a/text()')
        # # print('评分'+str(score))
        # # list.append(str(score))
        # # print(list)
        # with open('moive1.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(list)
        # print('*******************保存结束*************************')
else:
    print('状态码解析错误')

with  open('moive1.csv', 'a', encoding='gb18030') as f:
    writer = csv.writer(f)
    writer.writerow(["影片名", "导演"])
    for a in list:
        writer.writerow(a)

    #     self.CsvData=[]
    #     a = [author,author]
    #     self.CsvData.append(a)
# with open('PanKu_movie.csv','w',encoding='utf-8',newline='') as csvfile:
#     spamwriter =csv.writer(csvfile,dialect='excel')
#
#     spamwriter.writerow(["影片名","导演","编剧","主演","类型","地区","语言","上映时间","片长","又名","评分"])
#
#     for item in self.CsvData:
#     spamwriter.writerow(item)
#     print(screenwriter)


# try:
#
# except:
#     print('访问错误')


# def write_to_file(data):
#     with open('片库电影', 'w', encoding='utf-8') as csvfile:
#         csvfile.writer = csv.writer((data, csvfile) + '\n')
# def write_to_file(data):
#     with open('result1.txt', 'a', encoding='utf-8') as f:
#         f.write(json.dumps(data, ensure_ascii=False) + '\n')
