import uuid
import csv
import pymysql
import logging
import datetime
import re

try:
    conn = pymysql.connect(user='root', password='**********',host='localhost',
        database='db_name',charset = 'utf8', cursorclass = pymysql.cursors.DictCursor,
        local_infile = True, autocommit=True)
    print("connection is established")
    
except (pymysql.Error, pymysql.Warning) as connectError:
    print(connectError)
    

cursor = conn.cursor()
csv_data = csv.reader(open('/path/to/file/data.csv', encoding='ISO-8859-1'))

next(csv_data, None)
count = 0

try:
    for row in csv_data:
        count+=1
        print(row)
        
        try:
            sqlCmd = '''INSERT INTO table_name (id, name, status, data, dept, country) 
            VALUES ("%s", "%s", "%s", "%s", "%s", "%s")''' % (row[0],row[1],row[2],row[3],row[4],row[5])
            print("%s\n" %sqlCmd)
            cursor.execute(sqlCmd)

        except Exception as error:
            print(sqlCmd)
            print(error)

except Exception as error:
    print("Error while parsing csv is",error)

finally:
    conn.commit()
    cursor.close()
    print("connection closed successfully")