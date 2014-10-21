#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

ds = None
pid = 0
cid = 0
with open('area.json') as fr:
    ds = json.loads(fr.read())

sql = open('china.sql', 'w+')


def city(pid, cid0, cs):
    global cid
    for c in cs:
        cid = cid + 1
        name = c['n']
        pos = map(float, c['p'].split(','))
        sql.write("insert into city(id, countryId, provinceId, cityId, name, lat, lnt)values(%s,%s,%s,%s,'%s', %s, %s);\n" % (cid, 1, pid, cid0, name.encode('utf8'), pos[0], pos[1]))
        if 'l' in c:
            city(pid, cid, c['l'])


def province(ls):
    global pid
    for pi in ls:
        name = pi["n"]
        pid = pid + 1
        #p = map(float, pi['p'].split(','))
        #save province
        sql.write("insert into province(id, countryId, name)values(%s,%s,'%s');\n" % (pid, 1, name.encode('utf8')))
        cs = pi["l"]
        city(pid, 'null', cs)


ls = ds["l"]
province(ls)

sql.close()
