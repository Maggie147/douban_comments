'''
    @File    get Douban comments [python3.5]
    @Author  tx
    @Created On 2018-04-26
    @Updated On 2018-04-28
'''
import os
import sys
import pprint
import requests
from urllib import request
from lxml import etree
from bs4 import BeautifulSoup as bs
pwd = os.path.dirname(os.path.realpath(__file__))           #pwd2 = sys.path[0]
# pardir = os.path.abspath(os.path.join(pwd, os.pardir))
sys.path.append(pwd)
from pylib.data_handle import get_outpath, save_data


class DoubanComments(object):
    def __init__(self):
        self.header = self._get_header()
        self.mySession = requests.session()
        self.movies = []


    def _get_header(self, cookie=None, para=None):
        header  = {}
        header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
        try:
            header.update(self.header)
        except Exception as e:
            pass
        if cookie:
            header['Cookie']  = cookie
        if para:
            header.update(para)
        return header


    def _my_request(self, url):
        try:
            res = self.mySession.get(url, headers=self.header)
            if str(res.status_code)[0] != '2':
                print("request failed, URL: "+url)
                return None
            # res.encoding = 'utf-8'
            return res.text
        except Exception as e:
            print(e)
            return None

    def _my_request2(self, url, rmodel=2):
        try:
            resp = request.urlopen(url)
            html = resp.read().decode('utf-8')
            # html = resp.read().decode('utf-8', 'ignore').encode('GB18030', 'ignore')
            return html if html else None
        except Exception as e:
            print(e)
            return None


    def get_movies(self, model=1):
        url =  'https://movie.douban.com/cinema/nowplaying/chengdu/'
        buf = self._my_request(url)
        if not buf:
            print('get movies main page failed!')
            return None

        movies_list = []
        if model == 1:
            soup = bs(buf, 'html.parser')
            nowplaying   = soup.find_all('div', id='nowplaying')
            playing_list = nowplaying[0].find_all('li', class_='list-item')

            for li in playing_list:
                movie = {}
                movie['id'] = li['id']
                for tag_img_item in li.find_all('img'):         # movie['name'] = li['data-title']
                    movie['name'] = tag_img_item['alt']
                    movies_list.append(movie)

        elif model == 2:
            root = etree.HTML(buf)
            playing_list   = root.xpath('//div[@id="nowplaying"]//li[@class="list-item"]')
            for li in playing_list:
                movie = {}
                movie['id'] = li.xpath('./@id')[0]                 # /@attr, /text()
                movie['name'] = li.xpath('.//img[@alt]/@alt')[0]
                movies_list.append(movie)
        else:
            movies_list = []
        return movies_list if movies_list else None



    def get_comments(self, movieId, pageNum, model=2):
        # 貌似只能看10页的影评(start=200)
        if pageNum>0:
            start = (pageNum -1)*20
        else:
            return None
        url = 'https://movie.douban.com/subject/{}/comments?start={}&limite=20'.format(movieId, start)
        buf = self._my_request(url)
        if not buf:
            print('get comments failed, moviesId:  {}, startId: {}'.format(movieId, start))
            return None

        comments = []
        if model == 1:
            soup = bs(buf, 'html.parser')
            divs = soup.find_all('div', class_='comment')
            for div in divs:
                comment = div.find_all('p')[0].string
                if comment:
                    comments.append(comment)
        elif model == 2:
            root = etree.HTML(buf)
            comments = root.xpath('//div[@class="comment"]//p/text()')
        return comments if comments else None


def main():
    douban = DoubanComments()
    movies = douban.get_movies(model=2)
    pprint.pprint(movies)

    # # 循环获取第一个电影的前10页评论
    commentList = []
    for i in range(10):
        comments = douban.get_comments(movies[0]['id'], i+1)
        commentList.extend(comments)
    print(len(commentList))

    # pprint.pprint(commentList)
    outpath = get_outpath(path1='output', path2='data')
    ret = save_data(commentList, outpath, 'comments.json', ftype='json')
    print(outpath)
    if not ret:
        print("save data failed.")



if __name__ == '__main__':
    main()