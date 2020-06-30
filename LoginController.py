# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
from Connection import Connection

db = Connection()


class LoginController:
    def create(self):
        try:
            create_table_string = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY,
                user TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                level TEXT NOT NULL,
                status TEXT
            )'''

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(create_table_string)
        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def login(self, username, password):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            user_data = cursor.execute('SELECT user, password FROM users WHERE user = \'' + username + '\'').fetchone()

            if user_data is None:
                return 'USER NOT FOUND'
                
            
            if password != user_data[1]:
                return 'WRONG PASSWORD'
            else:
                cursor.execute('UPDATE users SET status = \'ON\' WHERE status = \'OFF\' AND user = \'' + username + '\'')
                conn.commit()
                return 'OK'
                
        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def reset_status(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET status = \'OFF\' WHERE status = \'ON\'')
            conn.commit()
            
                
        except Exception as e:
            print(e)

        finally:
            db.close_connection()