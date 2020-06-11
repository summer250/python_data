# coding:utf-8
import time

import pymysql
import requests
import re

from scrapy import Selector

for i in range(1,51):
    headers = {
        'Cookie': 'uuid=2ae837e5-98e1-46a3-8cbc-7050948c3780; ganji_uuid=7569292754772069277869; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1589628583; track_id=86782284437303296; antipas=Bc95nz2792403725H3s911E; clueSourceCode=%2A%2300; sessionid=078ea3fe-9d60-44bb-fcea-4fad43927670; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%2286782284437303296%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%222ae837e5-98e1-46a3-8cbc-7050948c3780%22%2C%22ca_city%22%3A%22nj%22%2C%22sessionid%22%3A%22078ea3fe-9d60-44bb-fcea-4fad43927670%22%7D; close_finance_popup=2020-06-11; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A40937873226%7D; cityDomain=www; user_city_id=-1; preTime=%7B%22last%22%3A1591851012%2C%22this%22%3A1591845709%2C%22pre%22%3A1591845709%7D',
        'Host': 'www.guazi.com',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

    }
    urls = 'https://www.guazi.com/www/bmw/o' + str(i)
    response = requests.get(url=urls, headers=headers)
    if response.status_code == 200:
        print('第'+str(i)+'页正常访问')

    html_selector = Selector(response)
    html_List = html_selector.xpath('//*[@class="carlist clearfix js-top"]/li/a/@href').getall()
    for b in html_List:
        html_Lists = 'https://www.guazi.com'+str(b)

        car_list=[]
        # print(html_Lists)
        car_list.append(html_Lists)

        response_detail = requests.get(url=html_Lists, headers=headers)
        response_detail.encoding = 'utf-8'
        selector_detail = Selector(response_detail)

        Name =re.findall('<meta name="keywords" content="(.*?)" />',response_detail.text)
        # Name = Name.strip()
        if Name == []:
            Name=selector_detail.xpath('/html/body/div[4]/div[3]/div[2]/h2/text()').extract_first()
            print("型号："+"".join(Name).strip())
            car_list.append(Name.strip())
        else:
            print('型号：'+"".join(Name))  #去空
            Name = Name[0]
            car_list.append(Name.strip())

        Price =selector_detail.xpath('//*[@class="price-num"]/text()').extract_first()
        print('价格：'+"".join(Price))
        car_list.append(Price)

        City =re.findall('<meta name="renderer" content="webkit">\n<title>(.*?)</title>',response_detail.text)[0]
        print("城市："+"".join(City))
        car_list.append(City)

        # print(car_list)

        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, charset='utf8',
                             database='python'
                             , use_unicode=True)
        cursor = db.cursor()
        sql = "INSERT INTO guazicars(URL,car_name,price,city) VALUES (%s,%s,%s,%s)"

        cursor.execute(sql, car_list)
        db.commit()
        print("***************" + f'{Name}' + "写入数据库成功!" + "*****************************************")
        # print( )

    # time.sleep(5)