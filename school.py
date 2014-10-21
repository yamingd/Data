#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import http
import dbm

dbm.opendb('school.db3')


def parse_loc(item, txt):
    tmp = txt.split(' ')
    item['province'] = tmp[0]
    item['city'] = tmp[1]
    item['district'] = tmp[2] if len(tmp) > 2 else ''


def parse_school(row):
    item = {}
    item['name'] = ''
    item['province'] = ''
    item['city'] = ''
    item['district'] = ''
    item['level'] = ''
    item['private'] = ''
    item['kind'] = ''
    item['addr'] = ''
    item['contact_phone'] = ''

    m = row.find_class('school_m_main')[0]

    h3 = m.get_element_by_id('dsadas')
    print h3
    item['name'] = h3.text_content().strip()

    tags = m.findall('li/b')

    loc = tags[0].text_content().strip()
    parse_loc(item, loc)

    item['level'] = tags[1].text_content().strip()

    tags = m.findall('li/ol/b')
    item['private'] = tags[0].text_content().strip()
    item['kind'] = tags[1].text_content().strip()
    
    tags = row.find_class('school_dz')
    item['addr'] = tags[0].text_content().strip()[5:]
    tags = row.find_class('school_telephone')
    item['contact_phone'] = tags[0].text_content().strip()[5:]

    return item


def parse_doc(doc):
    rows = doc.find_class('reply_box')
    for row in rows:
        item = parse_school(row)
        dbm.save(item)


def main(url):
    doc = http.get_htmldoc(url, encode='gbk')
    tag = doc.find_class('page_link')
    if not tag:
        parse_doc(doc)
    else:
        tag = tag[0].getparent().find_class('down')[-1]
        tag = tag.text_content()[1:]
        print tag
        ps = int(tag)
        parse_doc(doc)
        for x in xrange(1, ps):
            doc = http.get_htmldoc(url + "&page=" + str(x), encode='gbk')
            parse_doc(doc)

if __name__ == '__main__':
    url = 'http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=4403'
    url = 'http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=4401'
    url = 'http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=4404'
    url = 'http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=4419'
    url = 'http://xuexiao.51sxue.com/slist/?t=2&areaCodeS=4413'
    main(url)
