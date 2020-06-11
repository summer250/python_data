# coding:utf-8
import requests
import json
import csv


def write_to_file():
    with open('douban.csv', 'w')as f:
        writer = csv.writer(f)
        writer.writerow(["id", "电影名", '电影评分', '电影详情页'])






url = 'https://movie.douban.com/j/search_subjects'
headers = {

'Cookie': 'bid=_KHFG-WCJbA; douban-fav-remind=1; ll="118226"; __gads=ID=492520f31122d9a0:T=1580559240:S=ALNI_Maj6ymXdwMik-J-HobB9hgHva3clg; _vwo_uuid_v2=D7AC19594013DE5488BDA18375DF42F21|57f1fc2f1c3102934c37ef376ca78a0b; __yadk_uid=La4dxwzRY4HgmtKRCZNUFm6CZ4eLNmVI; push_doumail_num=0; push_noty_num=0; dbcl2="47464892:+jxG33qF1EU"; __utmv=30149280.4746; ct=y; ck=6U4H; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1591608834%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D1%26tn%3Dbaidu%26wd%3D%25E7%2594%25B5%25E5%25BD%25B1%25E6%258E%2592%25E8%25A1%258C%26oq%3D%2525E7%25258C%2525AB%2525E7%25259C%2525BC100%26rsv_pq%3D99b9e58e00079e7d%26rsv_t%3D6f18z%252B%252FgUsNsx8sM0NjmasmXrrFxks0tHcRX4lTCZY%252FARLnmmxBBWzqdcAk%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_dl%3Dtb%26rsv_btype%3Dt%26inputT%3D4716%26rsv_sug3%3D24%26rsv_sug1%3D20%26rsv_sug7%3D100%26rsv_sug2%3D0%26rsv_sug4%3D4716%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1657616189.1571035832.1591597169.1591608834.34; __utmb=30149280.0.10.1591608834; __utmz=30149280.1591608834.34.34.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%94%B5%E5%BD%B1%E6%8E%92%E8%A1%8C; __utma=223695111.1685091634.1585545818.1591598079.1591608834.12; __utmb=223695111.0.10.1591608834; __utmz=223695111.1591608834.12.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%94%B5%E5%BD%B1%E6%8E%92%E8%A1%8C; _pk_id.100001.4cf6=a49d7abd44a63a32.1585545818.11.1591608990.1591599333.',
'Host': 'movie.douban.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',

}
for i in range(0, 25):
    page = str(i*20)
    params = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '20',
        'page_start': f'{page}',

    }
    response = requests.get(url=url, headers=headers, params=params)
    print(response.url + '************')
    if response.status_code == 200:
        # print(response.encoding)
        response.encoding = 'utf-8'
        # print(response.text)
        json_data = json.loads(response.text)
        # print(json_data['subjects'])
    else:
        print(response.url)
        print('xxxxxx')
        for data in json_data['subjects']:
            list_movie = []
            # print(data)

            print('电影id为:' + data['id'])
            list_movie.append(data['id'])
            print('电影名为:' + data['title'])
            list_movie.append(data['title'])
            print('电影评分为:' + data['rate'])
            list_movie.append(data['rate'])
            print('电影详情页为:' + data['url'])
            list_movie.append(data['url'])

            with open('douban.csv', 'a')as f:
                writer = csv.writer(f)
                writer.writerow(list_movie)
            print('第' + str(i) + '爬取结束')



# data = json.loads(response.text)
# print(data)
