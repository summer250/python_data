# coding:utf-8
import csv
import time
import requests
from scrapy import Selector
import re
import pymysql

data_books = []
for i in range(0, 11):
    start = i * 25

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
    urls = 'https://book.douban.com/top250?start=' + str(start)
    response = requests.get(url=urls, headers=headers, allow_redirects=False)
    print(response)
    if response.status_code == 200:
        print('第' + str(i + 1) + "页正常访问")

    html_selector = Selector(response)
    # print(html_selector)
    html_List = html_selector.xpath('//*[@class="item"]/td[2]/div[1]/a/@href').getall()
    # print(html_List)

    for href in html_List:
        book_list = []

        response_detail = requests.get(url=href, headers=headers)
        # print(response_detail)
        # print(response_detail.url)
        response_detail.encoding = 'utf-8'
        # print(response_detail.encoding)
        selector_detail = Selector(response_detail)
        # print("******************")
        # print(response_detail.url)

        Name = re.findall('''<span property="v:itemreviewed">(.*?)</span>''', response_detail.text)[0]
        print("书名：" + "".join(Name))
        book_list.append(Name)

        Author = re.findall('<meta name="keywords" content=".*?,(.*?),.*?">', response_detail.text, re.S)
        # print("作者：" + "".join(Author))
        if Author == []:
            Author = 'None'
            book_list.append(Author)
        else:
            book_list.append(Author[0])

        Publishing_house = re.findall(' <span class="pl">出版社:</span> (.*?)<br/>', response_detail.text)
        # print('出版社：' + "".join(Publishing_house))
        if Publishing_house == []:
            Publishing_houser = 'None'
            book_list.append(Publishing_house)
        else:
            book_list.append(Publishing_house[0])

        Year_of_publication = re.findall('<span class="pl">出版年:</span>(.*?)<br/>', response_detail.text)
        # print('出版年：' + "".join(Year_of_publication))
        if Year_of_publication == []:
            Year_of_publication = 'None'
            book_list.append(Year_of_publication)
        else:
            book_list.append(Year_of_publication[0])

        Pages = re.findall('<span class="pl">页数:</span>(.*?)<br/>', response_detail.text)
        # print('页数：' + "".join(Pages))
        if Pages == []:
            Pages = 'None'
            book_list.append(Pages)
        else:
            book_list.append(Pages[0])

        Pricing = re.findall('<span class="pl">定价:</span>(.*?)<br/>', response_detail.text)
        # print("定价：" + "".join(Pricing))
        if Pricing == []:
            Pricing = 'None'
            book_list.append(Pricing)
        else:
            book_list.append(Pricing[0])

        Binding = re.findall('<span class="pl">装帧:</span>(.*?)<br/>', response_detail.text)
        # print("装帧：" + "".join(Binding))
        if Binding == []:
            Binding = 'None'
            book_list.append(Binding)
        else:
            book_list.append(Binding[0])

        Series = re.findall('<span class="pl">丛书:</span>&nbsp;<a href=".*?">(.*?)</a><br>', response_detail.text)
        if Series == []:
            Series = 'None'
            book_list.append(Series)
        else:
            book_list.append(Series[0])

        # print("丛书：" + "".join(Series))

        ISBN = re.findall('<span class="pl">ISBN:</span>(.*?)<br/>', response_detail.text)
        # print("ISBN:" + "".join(ISBN))
        if ISBN == []:
            ISBN = 'None'
            book_list.append(ISBN)
        else:
            book_list.append(ISBN[0])

        Content = selector_detail.xpath('//*[@id="link-report"]/span[2]/div/div/p/text()').extract_first()
        if Content == None:
            Content = selector_detail.xpath('//*[@id="link-report"]/div[1]/div/p/text()').extract()
            if Content == []:
                Content = 'None'
                book_list.append(Content)
            else:
                if len(Content) == 2:
                    book_list.append(Content[0] + Content[-1])
                elif len(Content) == 3:
                    book_list.append(Content[0] + Content[1] + Content[-1])
                elif len(Content) == 4:
                    book_list.append(Content[0] + Content[1] + Content[2] + Content[-1])
                elif len(Content) == 5:
                    book_list.append(Content[0] + Content[1] + Content[2] + Content[3] + Content[-1])
                elif len(Content) == 6:
                    book_list.append(Content[0] + Content[1] + Content[2] + Content[3] + Content[4] + Content[-1])
                elif len(Content) == 7:
                    book_list.append(
                        Content[0] + Content[1] + Content[2] + Content[3] + Content[4] + Content[5] + Content[-1])
                else:
                    book_list.append(Content[0])
        else:
            book_list.append(Content)

        Score = re.findall('<strong class="ll rating_num " property="v:average">(.*?)</strong>', response_detail.text)
        # print("评分：" + "".join(Score) + "分")
        if Score == []:
            Score = 'None'
            book_list.append(Score)
        else:
            book_list.append(Score[0])

        Number_of_people = re.findall(
            '<a href="collections" class="rating_people"><span property="v:votes">(.*?)</span>', response_detail.text)
        # print("".join(Number_of_people) + "人评价")
        if Number_of_people == []:
            Number_of_people = 'None'
            book_list.append(Number_of_people)
        else:
            book_list.append(Number_of_people[0])

        print(book_list)

        # tuple_books=tuple(book_list)

        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, charset='utf8',
                             database='python'
                             , use_unicode=True)
        cursor = db.cursor()
        sql = "INSERT INTO doubanbooks(book_Name, Author, Publishing_house, Year_of_publication, Pages, Pricing, Binding, Series, ISBN,Content, Score, Number_of_people) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql, book_list)
        db.commit()
        print("*******************" + f'{Name}' + "写入数据库成功!***********************")

    time.sleep(5)
