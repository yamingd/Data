#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
conn = None


def opendb(name):
    global conn
    conn = sqlite3.connect(name)
    c = conn.cursor()
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS school
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, province text, city text, district text, level text, private text, kind text, addr text, contact_phone text)''')

    c.execute('''CREATE TABLE IF NOT EXISTS school2
             (id INTEGER, name text, province_id integer, city_id integer, district_id integer, level_id integer, private_id integer, kind_id integer, addr text, contact_phone text)''')

    c.execute('''CREATE TABLE IF NOT EXISTS version
             (version_id integer, update_time timestamp)''')

    c.execute('select * from version')
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute('insert into version(version_id)values(1)')
    #c.execute('alter table books add column author text')
    #c.execute('alter table books add column remark text')

    conn.commit()


def save(item):
    c = conn.cursor()
    c.execute(
        "INSERT INTO school(name, province, city, district, level, private, kind, addr, contact_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [item['name'].strip().lower(), item['province'], item['city'], item['district'], item['level'], item['private'], item['kind'], item['addr'], item['contact_phone']])
    schoolid = c.lastrowid

    c.execute(
        'update version set version_id = version_id + 1, update_time=CURRENT_TIMESTAMP')

    conn.commit()
    return schoolid


def findall():
    c = conn.cursor()
    c.execute('select * from school')
    return c.fetchall()


def findall2():
    c = conn.cursor()
    c.execute('select name, kind_id, level_id, private_id, province_id, city_id, district_id, contact_phone from school2')
    return c.fetchall()


def save2(item):
    c = conn.cursor()
    c.execute(
        "INSERT INTO school2(id, name, province_id, city_id, district_id, level_id, private_id, kind_id, addr, contact_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [item['id'], item['name'], item['province_id'], item['city_id'], item['district_id'], item['level_id'], item['private_id'], item['kind_id'], item['addr'], item['contact_phone']])


def commit():
    conn.commit()
