# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
from Connection import Connection

db = Connection()


class AppController:
    def create(self):
        try:
            create_table_string = '''CREATE TABLE IF NOT EXISTS voluntaries (
                id INTEGER PRIMARY KEY NOT NULL,
                codigo_unico TEXT UNIQUE NOT NULL,
                registrado TEXT NOT NULL,
                nome TEXT NOT NULL,
                nome_do_pai TEXT NOT NULL,
                nome_da_mae TEXT NOT NULL,
                endereco TEXT NOT NULL,
                numero TEXT NOT NULL,
                complemento TEXT,
                bairro TEXT NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                cep TEXT NOT NULL,
                telefone_residencial TEXT,
                telefone_celular TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                rg TEXT NOT NULL UNIQUE,
                emissor TEXT NOT NULL,
                cidade_natal TEXT,
                estado_natal TEXT,
                data_de_nascimento TEXT NOT NULL,
                estado_civil TEXT,
                genero TEXT,
                escolaridade TEXT,
                email TEXT UNIQUE,
                cursando TEXT,
                empresa TEXT,
                ocupacao TEXT,
                tempo_de_empresa TEXT,
                endereco_empresa TEXT,
                bairro_empresa TEXT,
                numero_empresa TEXT,
                cidade_empresa TEXT,
                estado_empresa TEXT,
                cep_empresa TEXT,
                telefone_empresa TEXT
            )'''

            conn = db.create_connection()
            cursor = conn.cursor()
            cursor.execute(create_table_string)
        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def select(self, index):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            data = cursor.execute(f'SELECT * FROM voluntaries WHERE id = {index}').fetchone()
            
            return data

        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def get_access_level(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            level = cursor.execute('SELECT level FROM users WHERE status = \'ON\'').fetchone()[0]

            return level

        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def insert(self, model, date):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            voluntary_id = cursor.execute('SELECT COUNT(*) FROM voluntaries').fetchone()[0] + 1

            insert_string = f'''INSERT INTO voluntaries VALUES(
            {voluntary_id},
            '{model.unique_id}',
            '{date}',
            '{model.name}',
            '{model.father}',
            '{model.mother}',
            '{model.address}',
            '{model.number}',
            '{model.complement}',
            '{model.neighbourhood}',
            '{model.city}',
            '{model.state}',
            '{model.postal_code}',
            '{model.home_phone}',
            '{model.mobile_phone}',
            '{model.cpf}',
            '{model.rg}',
            '{model.emitter}',
            '{model.home_town}',
            '{model.home_state}',
            '{model.birth_date}',
            '{model.civil_state}',
            '{model.gender}',
            '{model.scholarship}',
            '{model.email}',
            '{model.course}',
            '{model.company_name}',
            '{model.ocupation}',
            '{model.company_time}',
            '{model.company_address}',
            '{model.company_neighbourhood}',
            '{model.company_number}',
            '{model.company_city}',
            '{model.company_state}',
            '{model.company_postal_code}',
            '{model.company_phone}')'''

            cursor.execute(insert_string)
            conn.commit()

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Registro de voluntário criado com sucesso!')
            tkinter.Tk().destroy()

            return voluntary_id
        except Exception as e:
            print(e)

        finally:
            db.close_connection()

    def get_total(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            total = cursor.execute('SELECT COUNT(*) FROM voluntaries').fetchone()[0]

            return total

        except Exception as e:
            print(e)

        finally:
            db.close_connection()
