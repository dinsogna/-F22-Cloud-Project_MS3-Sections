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
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_contact_by_id(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM cloud_project_db.emails where candidate_id=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_address_by_id(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM cloud_project_db.addresses where candidate_id=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result
    
    @staticmethod
    def get_phone_by_id(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT * FROM cloud_project_db.phones where candidate_id=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_email_address_by_id(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT email FROM cloud_project_db.emails where candidate_id=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result

    @staticmethod
    def get_email_type_by_id(key):
        # need to join emails + students table based on student id; then get the email from joined table
        sql = "SELECT kind FROM cloud_project_db.emails where candidate_id=%s";
        conn = ContactsResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()
        return result