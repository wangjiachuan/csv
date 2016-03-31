#-*- coding: utf8 -*-
''''''
import sys
import os
import time
import xml.etree.cElementTree as ET


def read_xml_file():
    '''test on python 2.7'''
    tree = ET.ElementTree(file='doc1.xml')
    root = tree.getroot()
    print("read xml file")
    print(root.tag, root.attrib)

    for elem in tree.iter():
        print elem.tag, elem.attrib
    pass



def write_xml_file():
    '''test on python 2.7'''



    a = ET.Element('elem')
    c = ET.SubElement(a, 'child1')
    c.text = "some text"
    d = ET.SubElement(a, 'child2')
    b = ET.Element('elem_b')
    root = ET.Element('root')
    root.extend((a, b))
    tree = ET.ElementTree(root)
    tree.write(sys.stdout)
    tree.write('doc1.xml')


if __name__ == '__main__':
    write_xml_file()
    read_xml_file()
    pass
    
