#-*- coding: utf8 -*-
'''pip install fake-factory'''
import sys
import os
import time
from faker import Factory


def create_faker():
    '''test on python 3.4'''
    #fake = Factory.create()
    fake = Factory.create('zh_CN')
    
    a=fake.name()
    print(a)
    b=fake.address()
    print(b)
    c=fake.text()
    print(c)


    for _ in range(0,10):
        print (fake.name())
        print(fake.safe_email())
        print(fake.random_int())
        print(fake.random_element(("USD", "GBP", "EUR")))
        
    pass


if __name__ == '__main__':
    create_faker()
    pass
    
