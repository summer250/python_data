# coding:utf-8
import requests
import json
import re


def Mian(iii):
    index_Url = "https://m.douban.com/movie/"
    headers = {
        'Referer': 'https://m.douban.com/movie/',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }
    params = {
        'os': 'ios',
        'start': '0',
        'count': '8',
        'loc_id': '108288'
    }
    type = requests.get(index_Url).text
    # print(type) #获取整个html页面
    reg = r'<section id="(.*?)">'
    section = re.findall(reg, type, re.S | re.M)
    print(section)
    # ['movie_showing"', 'movie_free_stream"', 'movie_latest"']
    # 数据Url
    # https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&callback=jsonp1&start=0&count=8&loc_id=108288&_=1544928329165
    # https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?os=ios&callback=jsonp1&start=0&count=8&loc_id=108288&_=1544928329165
    # https://m.douban.com/rexxar/api/v2/subject_collection/movie_latest/items?os=ios&callback=jsonp3&start=0&count=8&loc_id=108288&_=1544928329179
    print("正在爬取" + section[iii] + "的电影，请稍候...")
    data_url = "https://m.douban.com/rexxar/api/v2/subject_collection/" + section[iii] + "/items?"
    list_data = requests.get(data_url, headers=headers, params=params).json()
    # print(list_data) #得出数据

    with  open("./豆瓣.txt", "a", encoding="utf-8") as  f:
        for i in range(0, int(len(list_data["subject_collection_items"]))):
            try:
                data_write = "\n所属分类：" \
                             + str(list_data["subject_collection"]["name"]) + \
                             "\n电影名字:" + \
                             str(list_data["subject_collection_items"][i]["title"]) + \
                             "\n主角" + str(list_data["subject_collection_items"][i]["actors"][0]) + \
                             "\n电影出产处：" + str(list_data["subject_collection_items"][i]["info"]) + \
                             "\n电影观看地址：" + str(list_data["subject_collection_items"][i]["url"]) + \
                             "\n----------结束-------------"
                '''  后面都差不多是这样子  
                '''
                f.write(
                    data_write
                )
            except Exception as eee:
                return eee
        # 这里会有一个错误  -->list index out of range
    # print(eee)

    print("爬取完毕")


for  iii  in   range (0,3):
    Mian(iii)