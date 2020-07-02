# -*- coding: utf-8 -*-
import tkinter
from Connection import Connection
from tkinter import messagebox

db = Connection()


class RegisterController:
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
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def insert(self, user, password, level):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            user_id = cursor.execute('SELECT COUNT(*) FROM users').fetchone()[0] + 1

            query_string = f'''INSERT INTO users VALUES ({user_id}, '{user}', '{password}', '{level}', 'OFF')'''

            cursor.execute(query_string)
            conn.commit()
            
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Usuário criado com sucesso!')
            tkinter.Tk().destroy()
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def select(self, username):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            verification = cursor.execute('SELECT COUNT(*) FROM users WHERE user = \'' + username + '\'').fetchone()[0]

            if verification > 0:
                return True
                
            else:
                return False

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()
        
        finally:
            db.close_connection()
