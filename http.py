#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

import random
import time
import re
import os
import urlparse
from lxml.html import fromstring
from lxml.html.clean import Cleaner
from cStringIO import StringIO
import pycurl

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)'

#user_agent = 'Baiduspider ( http://www.baidu.com/search/spider.htm)'

default_headers = {
    'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5',
    'Accept-Language': 'ru,en-us;q=0.%(x)d,en;q=0.3;%(lang)s' % {'x': random.randint(5, 9),
                                                                 'lang': random.choice(['ua', 'gb', 'uk'])},
    'Accept-Charset': 'utf-8,gbk,gb2312,windows-1251;q=0.%(x)d,*;q=0.%(x)d' % {'x': random.randint(5, 9)}
}

img_type_map = {'image/jpeg': '.jpg',
                'image/gif': '.gif', 'image/x-png': '.png'}

cookie_file = os.path.join(os.getcwd(), '.cookie.txt')

cleaner = Cleaner(page_structure=False, links=False)


def page_charset(curl):
    content_type = curl.getinfo(pycurl.CONTENT_TYPE)
    print content_type
    if content_type is not None:
        s = re.findall('charset=(.+)', content_type.lower())
        if s:
            return s[0]
    return None


def urldomain(url):
    met = urlparse.urlsplit(url)
    return met.netloc

count = 0
start_at = None
timeout_max = None


def progress(download_t, download_d, upload_t, upload_d):
    global count, start_at, timeout_max
    count = count + 1
    if count % 1000 == 0 and download_t > 0:
        r = download_d * 100.0 / download_t
        print "Total %d bytes, have %d bytes so far, %d%s" % (download_t, download_d, r, '%')
    ds = time.time() - start_at
    if timeout_max and ds >= timeout_max:
        raise pycurl.error(-1, u'download timeout. max=%s' % timeout_max)


def _open(url, fp, timeout=5):
    global count, start_at, timeout_max
    count = 0
    start_at = time.time()
    timeout_max = timeout

    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, str(url.encode('utf8')))
    curl.setopt(pycurl.WRITEFUNCTION, fp.write)
    curl.setopt(pycurl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.NOPROGRESS, 0)
    curl.setopt(pycurl.PROGRESSFUNCTION, progress)  # 调用过程函数
    curl.setopt(pycurl.MAXREDIRS, 1)
    curl.setopt(pycurl.OPT_FILETIME, 1)
    if timeout:
        curl.setopt(pycurl.CONNECTTIMEOUT, timeout)
        # curl.setopt(pycurl.TIMEOUT, timeout)
    curl.setopt(pycurl.USERAGENT, user_agent)
    curl.setopt(pycurl.HTTPHEADER, ['%s: %s' % (
        a, b) for a, b in default_headers.iteritems()])
    curl.setopt(pycurl.COOKIEFILE, cookie_file)
    curl.setopt(pycurl.COOKIEJAR, cookie_file)
    curl.perform()
    return curl


def download_file(url, file_path, timeout=300, mode='w+'):
    with open(file_path, mode) as fp:
        try:
            curl = _open(url, fp, timeout=timeout)
            http_code = curl.getinfo(pycurl.HTTP_CODE)
            if http_code == 400 or http_code == 401 or http_code == 404:
                return http_code
            return None
        except:
            log.exception('unexpected error:%s' % url)
            return 500


def _getcontent(url, timeout=5):
    html = StringIO()
    try:
        log.debug('fetch content:%s' % url)
        curl = _open(url, html, timeout=timeout)
        data = html.getvalue()
        code = page_charset(curl)
        curl.close()
        return code, data
    except:
        log.exception('unexpected error:%s' % url)
        raise
    finally:
        html.close()


def get_image(url, fp, timeout=5):
    try:
        log.debug('fetch img:%s' % url)
        curl = _open(url, fp, timeout=timeout)
        # 通过content-type推动图片后缀
        content_type = curl.getinfo(curl.CONTENT_TYPE)
        curl.close()
        if content_type == u'text/html':
            log.error('return %s' % content_type)
            raise Exception(content_type)
        img_type = img_type_map.get(
            content_type, '.jpg') if content_type else '.jpg'
        return img_type
    except:
        log.exception('unexpected error:%s', url)
        raise


def get_htmldoc(url, encode='utf8', timeout=60):
    if url.startswith('file://'):
        with open(url[7:]) as f:
            content = f.read()
            content = content.decode(encode, 'ignore')
            print content.__class__
            try:
                content = cleaner.clean_html(content)
            except:
                pass
            doc = fromstring(content)
            return doc
    code, data = _getcontent(url, timeout=timeout)
    #print code
    #encode = 'utf8'
    if code:
        encode = code
    codedata = data.decode(encode, 'ignore')
    try:
        print codedata.__class__
        codedata = cleaner.clean_html(codedata)
    except:
        print 'Error: ', url
        log.exception('unexpected error:%s(%s)' % (url, encode))
        #raise
    #with open('error_page.html', 'w+') as fw:
    #    fw.write(codedata.encode(encode))
    doc = fromstring(codedata)
    # log.debug(codedata)
    return doc


def get_xmldoc(url, timeout=5):
    code, data = _getcontent(url, timeout=timeout)
    print code
    doc = fromstring(data)
    return doc


def timeit(fc):
    def wrapper(*args, **kwargs):
        t1 = time.time() * 1000
        ret = fc(*args, **kwargs)
        t2 = time.time() * 1000 - t1
        print fc.__name__, t2
        return ret
    return wrapper

if __name__ == '__main__':
    #print get_htmldoc(u'http://www.mfxsb.com/xiaoshuo/2/2562/7224263.html', encode='gbk')
    print get_htmldoc(u'file://error_page.html', encode='gbk')