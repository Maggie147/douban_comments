# -*- coding: utf-8 -*-
'''
    @File    csv handle test [python3.5]
    @Author  tx
    @Created On 2018-04-28
    @Updated On 2018-04-28
'''
import os
import sys
import pprint
pwd = os.path.dirname(os.path.realpath(__file__))           #pwd2 = sys.path[0]
# pardir = os.path.abspath(os.path.join(pwd, os.pardir))
sys.path.append(pwd)
from data_handle import CSVHandle, get_outpath


def list_csv(dpath):
    fname = os.path.join(dpath, 'test_list.csv')
    # print(fname)

    list_data = [ ['name', 'age'], ['aa', 15], ['bb', 16], ['cc', 17], ['dd', 18] ]

    csvObj = CSVHandle()

    csvObj.writer_csv(fname, list_data)

    values = csvObj.read_csv(fname)
    pprint.pprint(values)
    print('\n')

    values2 = csvObj.dic_read_csv(fname)
    pprint.pprint(values2)

    print('list_csv test end.')



def dict_csv(dpath):
    fname = os.path.join(dpath, 'test_dict.csv')
    print(fname)

    dict_data = [{'name':'aa', 'age':15}, {'name':'bb', 'age':16}, {'name':'cc', 'age':17}, {'name':'dd', 'age':18}]

    csvObj = CSVHandle()

    csvObj.dic_write_csv(fname, dict_data)

    values = csvObj.dic_read_csv(fname)

    pprint.pprint(values)

    print('dict_csv test end.')


def main():
    print(pwd)
    ret_path = get_outpath()
    if not ret_path:
        sys.exit(1)

    list_csv(ret_path)
    dict_csv(ret_path)



if __name__ == '__main__':
    main()