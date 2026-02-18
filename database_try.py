# coding:utf-8
import sqlite3
#crud :create read update delete
connection=sqlite3.connect("base2.db")
cursor=connection.cursor()
cursor.execute('SELECT * from ')
connection.close()