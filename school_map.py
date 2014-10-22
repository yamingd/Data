#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbm
import enums

dbm.opendb('school.db3')


def strip_name(row):
    name = row[1]
    f0 = row[2]
    f2 = row[3]
    f3 = row[4]
    name = name.replace(f0, '')
    name = name.replace(f2, '')
    name = name.replace(f3, '')
    return name


def get_district_id(item, row):
    s = row[4]
    if len(s) == 0:
        return None
    ds = enums.district[item['city_id']]
    if s in ds:
        return ds[s]
    s = s.replace(u'市', u'区')
    return None


def get_private_id(row):
    if len(row[6]) == 0:
        return None
    return enums.school_attr[row[6]]


def map_row(row):
    """
    select id, name, province, city, district, level, private, kind, addr, contact_phone from school
    """
    item = {}
    item['id'] = row[0]
    item['name'] = strip_name(row)
    item['province_id'] = enums.province[row[2]]
    print row[0], 'province:', row[2], item['province_id']
    item['city_id'] = enums.city[item['province_id']][row[3]]
    print row[0], 'district:', row[4], item['city_id']
    item['district_id'] = get_district_id(item, row)
    print row[0], 'district:', row[4], item['district_id']
    item['level_id'] = enums.school_level[row[5]]
    print row[0], 'private: ', row[6]
    item['private_id'] = get_private_id(row)
    item['kind_id'] = enums.school_type[row[7]]
    item['addr'] = row[8]
    item['contact_phone'] = row[9]
    return item


def sql_value(val):
    if val is None:
        return 'null'
    return val


def dump_sql():
    s0 = "insert into school(name, typeId, levelId, attrId, provinceId, cityId, districtId, contactPhone)values('%s', %s, %s,%s,%s,%s,%s,'%s');"
    rows = dbm.findall2()
    with open('school.sql', 'w+') as fw:
        for row in rows:
            vs = []
            for i in xrange(len(row)):
                vs.append(sql_value(row[i]))
            s = s0 % (
                vs[0].encode('utf8'), vs[1], vs[2], vs[3], vs[4], vs[5], vs[6], vs[7].encode('utf8'))
            fw.write(s)
            fw.write('\n')


def main():
    rows = dbm.findall()
    for row in rows:
        item = map_row(row)
        dbm.save2(item)
    dbm.commit()


if __name__ == '__main__':
    # main()
    dump_sql()
