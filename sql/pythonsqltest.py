# This example comes primarily from http://www.mysqltutorial.org/python-mysql/
# with a few changes of my own (database, connection method, command line
# arguements, etc)

from mysql.connector import MySQLConnection, Error
import sys


def query_with_fetchone():
    try:
        #dbconfig = read_db_config()
        #conn = MySQLConnection(**dbconfig)
        conn = MySQLConnection(user='root', password='tksql',
                               host='127.0.0.1',
                               database='test')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM name")
                                             
        row = cursor.fetchone()
                                                   
        while row is not None:
            print(row)
            row = cursor.fetchone()
                                                                                          
    except Error as e:
        print(e)
                                                                                   
    finally:
        cursor.close()
        conn.close()

def insert_name(title, isbn):
    query = "INSERT INTO name(lastname, firstname) " \
            "VALUES(%s,%s)"
    args = (title, isbn)
                                 
    try:
        #db_config = read_db_config()
        #conn = MySQLConnection(**db_config)
        conn = MySQLConnection(user='root', password='tksql',
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


def main():
    print('Usage: Provide [LastName FirstName] to insert into name table. Any other combination will display the table data only')
    if len(sys.argv) > 2:
        insert_name(str(sys.argv[1]), str(sys.argv[2]))
    query_with_fetchone()
                                                                                                                                      
if __name__ == '__main__':
    main()

#cnx.close()
