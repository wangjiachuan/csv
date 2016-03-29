#-*- coding: utf8 -*-
import sys
import os
import time
import csv


def create_csv():
    '''only apply to python 2.7'''

    if sys.version_info >= (3,0,0):
        csvfile = open('csvtest.csv', 'w', newline='')
    else:
        csvfile = open('csvtest.csv', 'wb')
    #csvfile = file('csvtest.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'url', 'keywords'])
    data = [
      ('1', 'http://www.xiaoheiseo.com/', '小黑'),
      ('2', 'http://www.baidu.com/', '百度'),
      ('3', 'http://www.jd.com/', '京东')
    ]
    writer.writerows(data)
    csvfile.close()
    

def read_csv():
    csvfile = file('csvtest2.csv', 'rb')
    reader = csv.reader(csvfile)

    for line in reader:
        print (line)

    csvfile.close()


def dict_writer():
    rows = [{'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
    {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
    {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
    {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'},
    {'Column1': '0', 'Column2': '1', 'Column3': '2', 'Column4': '3'}]
    
    fieldnames = ['Column1', 'Column2', 'Column3', 'Column4']
    dict_writer = csv.DictWriter(open(r'csvtest2.csv', 'wb'), fieldnames=fieldnames)
    dict_writer.writeheader() # first line need be added manually
    dict_writer.writerows(rows) 



if __name__ == '__main__':
    create_csv()
    dict_writer()
    read_csv()
    
