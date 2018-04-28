'''
    @File    handle Douban comments [python3.5]
    @Author  tx
    @Created On 2018-04-26
    @Updated On 2018-04-28
'''

import os
import sys
import re
import jieba
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pprint
pwd = os.path.dirname(os.path.realpath(__file__))           #pwd2 = sys.path[0]
# pardir = os.path.abspath(os.path.join(pwd, os.pardir))
sys.path.append(pwd)
from pylib.data_handle import get_outpath, save_data, get_data



def handle_buffer(buf):
    if not buf:
        print('No data to clean.')

    # (清洗) 将列表中的数据转换为字符串
    comments = ''
    for i in range(len(buf)):
        comments = comments + str(buf[i]).strip()
    # print(comments)

    # 使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    c_comments = ''.join(filterdata)
    # print(c_comments)

    # 使用结巴分词进行中文分词
    segment  = jieba.lcut(c_comments)
    words_df = pd.DataFrame({'segment': segment})

    # 去掉停用词
    stpwdpath = os.path.join(pwd, 'stopwords', './stopwords.txt')
    stopwords = pd.read_csv(stpwdpath, index_col=False, quoting=3, sep="\t",
        names=['stopword'],encoding='utf-8')
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    # print(words_df.head())

    # 统计词频
    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending = False)
    # print(words_df.head())


    # (用词云进行显示)   指定字体类型、大小、颜色
    wordcloud = WordCloud(font_path="simhei.ttf",
                            background_color="white",
                            max_font_size=80)

    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    wordcloud=wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()



def main():
    outpath = get_outpath(path1='output', path2='data')
    buff = get_data(outpath, 'comments.json', ftype='json')
    # print(len(buff))
    # print(type(buff))
    handle_buffer(buff)

if __name__ == '__main__':
    main()