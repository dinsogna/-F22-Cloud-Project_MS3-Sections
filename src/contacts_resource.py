import pymysql

import os

class ContactsResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            # user='admin',
            user='root',
            password='4355Sasha2056!',
            host='localhost',
            # host='e6156.cwjkexlxpxly.us-east-1.rds.amazonaws.com',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_email_by_uni(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM f22_databases.emails where CUID=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_address_by_uni(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM f22_databases.addresses where CUID=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result
    
    @staticmethod
    def get_phone_by_uni(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM f22_databases.phones where CUID=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_email_address_by_uni(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT email FROM f22_databases.emails where CUID=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_email_type_by_uni(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT kind FROM f22_databases.emails where CUID=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result