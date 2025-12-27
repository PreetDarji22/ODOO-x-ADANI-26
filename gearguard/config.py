import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Preet@123',  # Make sure this matches what you set in Step 1
        database='gearguard',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection