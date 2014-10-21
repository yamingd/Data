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