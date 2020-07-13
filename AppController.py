# -*- coding: utf-8 -*-
import tkinter
import fpdf
import pandas
import datetime
import os
import platform
from tkinter import messagebox
from Connection import Connection
from plyer import notification

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
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def select(self, index):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            data = cursor.execute(f'SELECT * FROM voluntaries WHERE id = {index}').fetchone()
            
            return data

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def get_access_level(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            level = cursor.execute('SELECT level FROM users WHERE status = \'ON\'').fetchone()[0]

            return level

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

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
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def update(self, model, index):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()            

            update_string = f'''UPDATE voluntaries SET             
            nome = '{model.name}',
            nome_do_pai = '{model.father}',
            nome_da_mae = '{model.mother}',
            endereco = '{model.address}',
            numero = '{model.number}',
            complemento = '{model.complement}',
            bairro = '{model.neighbourhood}',
            cidade = '{model.city}',
            estado = '{model.state}',
            cep = '{model.postal_code}',
            telefone_residencial = '{model.home_phone}',
            telefone_celular = '{model.mobile_phone}',
            cpf = '{model.cpf}',
            rg = '{model.rg}',
            emissor = '{model.emitter}',
            cidade_natal = '{model.home_town}',
            estado_natal = '{model.home_state}',
            data_de_nascimento = '{model.birth_date}',
            estado_civil = '{model.civil_state}',
            genero = '{model.gender}',
            escolaridade = '{model.scholarship}',
            email = '{model.email}',
            cursando = '{model.course}',
            empresa = '{model.company_name}',
            ocupacao = '{model.ocupation}',
            tempo_de_empresa = '{model.company_time}',
            endereco_empresa = '{model.company_address}',
            bairro_empresa = '{model.company_neighbourhood}',
            numero_empresa = '{model.company_number}',
            cidade_empresa = '{model.company_city}',
            estado_empresa = '{model.company_state}',
            cep_empresa = '{model.company_postal_code}',
            telefone_empresa = '{model.company_phone}'
            WHERE id = {index}'''

            cursor.execute(update_string)
            conn.commit()

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Registro de voluntário editado com sucesso!')
            tkinter.Tk().destroy()

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def get_total(self):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            total = cursor.execute('SELECT COUNT(*) FROM voluntaries').fetchone()[0]

            return total

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def delete(self, index):
        try:
           conn = db.create_connection()
           cursor = conn.cursor()
           cursor.execute(f'DELETE FROM voluntaries WHERE id = {index}')

           cursor.execute(f'UPDATE voluntaries SET id = id - 1 WHERE id > {index}')

           conn.commit()

           root = tkinter.Tk()
           root.withdraw()
           messagebox.showinfo('SUCESSO', 'Registro deletado com sucesso!')
           tkinter.Tk().destroy()
        
        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def id_search(self, word):
        try:
            conn = db.create_connection()
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT id, nome FROM voluntaries WHERE nome LIKE '%{word}%'").fetchall()

            if result == []:
                root = tkinter.Tk()
                root.withdraw()
                messagebox.showwarning('ATENÇÃO', 'Não foram encontrados resultados com o termo utilizado.')
                tkinter.Tk().destroy()

            else:
                message = ''

                for row in result:
                    for column in row:
                        message += str(column)
                        message += ' - '                
                
                    message = message[:-3]
                    message += '\n\n'

                root = tkinter.Tk()
                root.withdraw()
                messagebox.showinfo('ATENÇÃO', message)
                tkinter.Tk().destroy()                

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()

    def gen_contract(self, index):
        try:
            notification.notify(
                app_name = 'GERENCIADOR DE VOLUNTÁRIOS',
                title = 'GERANDO CONTRATO',
                message = 'Aguarde enquanto o contrato está sendo gerado, uma mensagem aparecerá na tela ao término da operação.',
                timeout = 5
            )

            database_fields = [
                'ID',
                'SERIAL',
                'REGISTRADO EM',
                'NOME',
                'NOME DO PAI',
                'NOME DA MAE',
                'ENDERECO',
                'NUMERO',
                'COMPLEMENTO',
                'BAIRRO',
                'CIDADE',
                'ESTADO',
                'CEP',
                'TELEFONE (RESIDENCIAL)',
                'TELEFONE (CELULAR)',
                'CPF',
                'RG',
                'ORGAO EMISSOR',
                'CIDADE NATAL',
                'ESTADO NATAL',
                'DATA DE NASCIMENTO',
                'ESTADO CIVIL',
                'GENERO',
                'ESCOLARIDADE',
                'EMAIL',
                'CURSO DOUTRINARIO',
                'EMPRESA',
                'OCUPACAO',
                'TEMPO DE EMPRESA',
                'ENDERECO DA EMPRESA',
                'BAIRRO DA EMPRESA',
                'NUMERO DA EMPRESA',
                'CIDADE DA EMPRESA',
                'ESTADO DA EMPRESA',
                'CEP DA EMPRESA',
                'TELEFONE DA EMPRESA'
            ]

            conn = db.create_connection()
            cursor = conn.cursor()
            result = cursor.execute(f'SELECT * FROM voluntaries WHERE id = {index}').fetchone()
            
            emitter = result[17].split('/')

            pdf = fpdf.FPDF(format = 'A4')
            pdf.add_page()
            pdf.set_font('times', 'B', size = 20)
            pdf.set_fill_color(200,200,200)
            pdf.write(18,'DADOS DO VOLUNTÁRIO')
            pdf.ln()

            i = 1
            while i < len(database_fields):
                if result[i] != '' and not result[i].endswith('-') and database_fields[i] != 'ESTADO DA EMPRESA':
                    pdf.set_font('helvetica', 'B',size = 12)
                    pdf.cell(55, 9, database_fields[i], 1, 0, '', 1, '')
                    pdf.set_font('helvetica', size = 12)
                    pdf.multi_cell(0, 9, result[i], 1, 'J', 0)
                
                i += 1

            pdf.add_page()
            pdf.image('./assets/contract/contract_header.png', w=190, h=45)
            pdf.ln()
            
            string_contract = f'''
            Eu, {result[3]}, portador da cédula de identidade no Registro Geral nº {result[16]} emitida 
            no estado da UF {emitter[1].strip()} pelo Órgão Emissor {emitter[0].strip()} e CPF {result[15]}, 
            disponho-me a prestar serviços voluntários nos moldes da lei 9608/98, a qual tenho pleno conhecimento, 
            firmo por essa melhor forma de direito, MINHA DISPOSIÇÃO DE SERVIR COMO VOLUNTÁRIO(A) POR TEMPO 
            INDETERMINADO nas tarefas beneficentes da ASSOCIAÇÃO ESPÍRITA LAURO MACHADO, com sede à Avendida Ulisses 
            Guimarães, nº 1901, Bairro Vila Guilherme na cidade de Francisco Morato no Estado de São Paulo, doando 
            minhas horas disponíveis, bem como minhas atividades, em favor dos menos favorecidos como e quando me for 
            possível, segundo o melhor critério adotado pela entidade, por dispor de renda própria para minha 
            subsistência, submeto-me às cláusulas abaixo:
            '''

            string_clause = f'''
            * Cláusula 1ª - Ao teor do que dispõe o Parágrafo Único do Artigo 1 da Lei 9608/98,
                                    a prestação do serviço voluntário em questão não gera vínculo empregatício,
                                    nem obrigação de natureza trabalhista, previdenciária ou afim.

            * Cláusula 2ª - A prestação do serviço voluntário não será remunerada, sendo que eventuais
                                    despesas realizadas no desempenho das atividades não serão reembolsadas
                                    pela instituição.
            
            * Cláusula 3ª - Como voluntário(a) disponho-me a realizar as atividades relacionadas acima,
                                    comprometendo-me a observar o Regulamento Interno da Instituição.
            
            * Cláusula 4ª - A prestação de serviço voluntário poderá ser encerrada a qualquer tempo
                                    por uma das partes.
            '''

            string_days = f'''
            Dias disponíveis: de Segunda-feira à Sexta-feira das 08:00 hs. às 17:00 hs., Sábados das 08:00 hs. 
            às 19:00 hs., Domingos das 08:00 hs. às 13:00 hs., e Quartas-feiras além do horário normal, das 19:00 
            hs. às 20:30 hs., podendo alterar estes horários em eventos, com prévio aviso e concordância.
            '''

            string_agreement = f'''
            Desta forma, lido e achado conforme assinam o presente Termo de Adesão de Serviço Voluntário, 
            na presença de duas testemunhas que também o subscreve.
            '''

            contract = string_contract.replace('\n', '').replace('    ', '') + '\n'
            contract += string_clause + '\n'
            contract += string_days.replace('\n', '').replace('    ', '') + '\n\n'
            contract += string_agreement.replace('\n', '').replace('    ', '') + '\n'

            pdf.set_font('times', size = 12)
            pdf.multi_cell(0, 6.5, contract, 1, 'J', 0)
            pdf.set_font('times', 'B', size = 14)
            # pdf.write(6,'FRANCISCO MORATO, SP - ' + datetime.datetime.now().strftime('%d/%m/%Y'))
            # pdf.ln()
            pdf.ln()
            pdf.ln()
            pdf.image('./assets/contract/contract_footer.png', w=190, h=4)


            if platform.system() == 'Linux':
                if not os.path.exists(os.path.expanduser("~") + '/Documentos/CONTRATOS_DE_VOLUNTARIOS'):
                    os.mkdir(os.path.expanduser("~") + '/Documentos/CONTRATOS_DE_VOLUNTARIOS')
                
                pdf.output(os.path.expanduser("~") + '/Documentos/CONTRATOS_DE_VOLUNTARIOS/Contrato_de_' + result[3] + '.pdf')

            else:
                if not os.path.exists(os.path.expanduser("~") + '\\Documents\\CONTRATOS_DE_VOLUNTARIOS'):
                    os.mkdir(os.path.expanduser("~") + '\\Documents\\CONTRATOS_DE_VOLUNTARIOS')
                
                pdf.output(os.path.expanduser("~") + '\\Documents\\CONTRATOS_DE_VOLUNTARIOS\\Contrato_de_' + result[3] + '.pdf')

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Contrato de voluntariado gerado com sucesso!')
            tkinter.Tk().destroy()

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            pdf.close()
            db.close_connection()

    def gen_xlsx(self):
        try:
            select_string = '''
            SELECT
            nome, telefone_celular 
            FROM
            voluntaries
            '''
            
            conn = db.create_connection()
            data_frame = pandas.read_sql_query(select_string, conn)

            if platform.system() == 'Linux':
                data_frame.to_excel(os.path.expanduser("~") + '/Documentos/PLANILHA_DE_VOLUNTARIOS.xlsx', index=False)
            else:
                data_frame.to_excel(os.path.expanduser("~") + '\\Documents\\PLANILHA_DE_VOLUNTARIOS.xlsx', index=False)

            root = tkinter.Tk()
            root.withdraw()
            messagebox.showinfo('SUCESSO', 'Planilha de voluntários gerada na pasta de documentos.')
            tkinter.Tk().destroy()

        except Exception as e:
            root = tkinter.Tk()
            root.withdraw()
            messagebox.showerror('ERRO', e)
            tkinter.Tk().destroy()

        finally:
            db.close_connection()
        