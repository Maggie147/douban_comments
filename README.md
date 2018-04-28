# douban_comments spider & handle
基于 Python 3.5.4
爬取豆瓣最近上映的电影，及相关电影的影评，然后对影评做分析。


## 主要功能:
- 抓取网页数据，使用`BeautifulSoup`和`xpath`进行解析网页数据。
- 清洗数据，主要使用re正则,jieba, pandas进行清洗处理数据。
- 用词云进行展示


## 相关库的安装: jieba、 pandas、wordcloud
- 1、`wordcloud`词云安装可能失败 `pip install wordcloud`
    解决方法：下载.whl文件 (https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)
    ```
    pip install wordcloud-1.4.1-cp35-cp35m-win_amd64.whl
    ```