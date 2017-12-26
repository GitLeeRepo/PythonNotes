#!/usr/bin/python3

# This example comes primarily from http://www.mysqltutorial.org/python-mysql/
# with a few changes of my own (database, connection method, command line
# arguments, etc)

from mysql.connector import MySQLConnection, Error
import sys


def query_with_fetchone(p, search=None):
    try:
        #dbconfig = read_db_config()
        #conn = MySQLConnection(**dbconfig)
        conn = MySQLConnection(user='demo', password=p,
                               host='127.0.0.1',
                               database='test')

        cursor = conn.cursor()

        sql = "SELECT * FROM name"
        if search != None:
            sql += " WHERE lastname=%s AND firstname=%s"
            print(sql)
            cursor.execute(sql, search)
        else:
            cursor.execute(sql)
                                             
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
                                                                                          
    except Error as e:
        print(e)
                                                                                   
    finally:
        cursor.close()
        conn.close()

def insert_name(p, last, first):
    query = "INSERT INTO name(lastname, firstname) " \
            "VALUES(%s,%s)"
    args = (last, first)
                                 
    try:
        conn = MySQLConnection(user='demo', password=p,
                               host='127.0.0.1',
                               database='test')
                                 
        cursor = conn.cursor()
        cursor.execute(query, args)
                                                                           
        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')
                                                                                                                            
        conn.commit()
    except Error as error:
        print(error)
                                                                                                                                   
    finally:
        cursor.close()
        conn.close()

def delete_name(p, id):
    query = "DELETE FROM name WHERE id = %s " 
    args = (id,)
                                 
    try:
        conn = MySQLConnection(user='demo', password=p,
                               host='127.0.0.1',
                               database='test')
                                 
        cursor = conn.cursor()
        cursor.execute(query, args)
                                                                           
        conn.commit()
    except Error as error:
        print(error)
                                                                                                                                   
    finally:
        cursor.close()
        conn.close()

def readconfig():
    f = open('sql.cfg')
    s = f.read()
    f.close()
    return s.rstrip()

def main():
    p = readconfig()
    print('Usage: Provide [LastName FirstName] to insert into name table, or [-d id] to removed specified id row')
    print('Any other combination will display the table data only')
    if len(sys.argv) > 2:
        if sys.argv[1] == "-d":
            if sys.argv[2] != None:
                delete_name(p, sys.argv[2])
        else:
            insert_name(p, str(sys.argv[1]), str(sys.argv[2]))

    query_with_fetchone(p)
                                                                                                                                      
if __name__ == '__main__':
    main()

