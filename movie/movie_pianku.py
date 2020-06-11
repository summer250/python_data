import time
import movie
import re
import json
# import csv


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = movie.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except :
        return '访问错误'


def parse_one_page(html):
    item = re.findall('<a href="(.*?)" title=', html)
    print(item)
    return item



# def write_to_file(data):
#     with open('片库电影', 'w', encoding='utf-8') as csvfile:
#         csvfile.writer = csv.writer((data, csvfile) + '\n')
def write_to_file(data):
    with open('result1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False) + '\n')


def main(package):
    url = 'https://www.pianku.tv/mv/' +str('------')+ str(package) + str('.html')
    print(url)
    html = get_one_page(url)
    print(html)
    parse_one_page(html)
    print(item)
    write_to_file(item)


if __name__ == '__main__':
    for i in range(1, 2):
        main(str(i))
        # time.sleep(1)
