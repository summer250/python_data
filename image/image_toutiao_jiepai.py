# coding:utf-8
import os
from hashlib import md5
from multiprocessing import Pool
import requests
from urllib.parse import urlencode
from scrapy import item



def get_page(offset):
    headers ={
        'cookie': 'tt_webid=6836174223817377287; s_v_web_id=verify_kb7bqefy_u2pehBZK_l01v_4BxZ_B95c_qpt0tvxuPhqN; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6836174223817377287; csrftoken=1ed7c2630ba7dc7e8ad9c47076ceeafd; SLARDAR_WEB_ID=12628b3b-f646-49b6-9cbf-0bc82ef4b9fa; ttcid=891a3f925ca74d198ddb8c2a0e05352926; tt_scid=-Il46FsCz1xMQlGTLd8KDfKlFgIag0.8u.d-WeDL6OrysXmwIM3TqH2Ctek7gkeN56b1; __tasessionId=8vlw3rq1c1591677948206',
        'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        

    }
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
    }
    url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except:
        print("状态码解析错误")


def get_image(json):
    if json.get('data'):
        title = item.get('data')
        images = item.get('image_list')
        for image in images:
            yield {
                'image': image.get('url'),
                'title': title
            }

def save_image(item):
    if not os.path.exists(item.get('title')):
        #os.path.exists(path)	如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item)
        if response.status_code == 200:
            file_path ='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            # md5().hexdigest():将文件保存时，通过哈希函数对每个文件进行文件名的自动生成
            # requests.content 返回的是二进制响应内容
            if not os.path.exists(file_path):
                with open(file_path,'wb')as f:
                    f.write(response.content)
            else:
                print('已经下载',file_path)
    except:
        print('保存图片失败')

def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20


if __name__ == '__main__':
    pool =Pool()
    groups =([x*20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    # map () 函数会将第二个参数的需要迭代的列表元素一个个的传入第一个参数我们的函数中，第一个参数是我们需要引用的函数，这里我们看到第一个参数我们自己定义的函数并没有设置形参传值。因为我们的 map 会自动将数据作为参数传进去。
    pool.close()
    pool.join()
