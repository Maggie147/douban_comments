# -*- coding: utf-8 -*-
'''
    @File    excel handle test [python3.5]
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
from data_handle import ExcelHandle, get_outpath


def test_excel07(dpath):
    fname = os.path.join(dpath, 'test_excel07.xlsx')
    # print(fname)
    sname = 'write_test'

    list_data = [ ['name', 'age'], ['aa', 15], ['bb', 16], ['cc', 17], ['dd', 18] ]
    xlObj = ExcelHandle()
    xlObj.write07_excel(fname, sname, list_data)
    xlObj.read07_excel(fname)


def test_excel03(dpath):
    fname = os.path.join(dpath, 'test.xls')
    # print(fname)
    sname = 'write_test'

    list_data = [ ['name', 'age'], ['aa', 15], ['bb', 16], ['cc', 17], ['dd', 18] ]

    xlObj = ExcelHandle()
    xlObj.write_excel(fname, sname, list_data)
    xlObj.read_excel(fname)



def main():
    print(pwd)
    ret_path = get_outpath()
    if not ret_path:
        sys.exit(1)

    test_excel07(ret_path)
    test_excel03(ret_path)



if __name__ == '__main__':
    main()