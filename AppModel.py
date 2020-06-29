# -*- coding: utf-8 -*-

class AppModel:
    def __init__(self, code=None, unique_id=None, registered=None, name=None, father_name=None, mother_name=None, address=None, number=None, complement=None, neighbourhood=None, city=None, state=None, postal_code=None, home_phone=None, mobile_phone=None, course=None, cpf=None, rg=None, emitter=None, home_town=None, home_state=None, birth_date=None, civil_state=None, gender=None, scholarship=None, email=None, company=None, company_time=None, ocupation=None, company_address=None, company_neighbourhood=None, company_number=None, company_city=None, company_state=None, company_postal_code=None, company_phone=None):
        self.code = code
        self.unique_id = unique_id
        self.registered = registered
        self.name = name
        self.father_name = father_name
        self.mother_name = mother_name
        self.address = address
        self.number = number
        self.complement = complement
        self.neighbourhood = neighbourhood
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.cpf = cpf
        self.rg = rg
        self.emitter = emitter
        self.home_town = home_town
        self.home_state = home_state
        self.birth_date = birth_date
        self.civil_state = civil_state
        self.gender = gender
        self.scholarship = scholarship
        self.email = email
        self.course = course
        self.company = company
        self.company_time = company_time
        self.ocupation = ocupation
        self.company_address = company_address
        self.company_neighbourhood = company_neighbourhood
        self.company_number = company_number
        self.company_city = company_city
        self.company_state = company_state
        self.company_postal_code = company_postal_code
        self.company_phone = company_phone

    @property
    def code(self):
        return self.code

    @code.setter
    def code(self, code):
        self.code = code

    @property
    def unique_id(self):
        return self.unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        self.unique_id = unique_id

    @property
    def registered(self):
        return self.registered

    @registered.setter
    def registered(self, registered):
        self.registered = registered

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def father_name(self):
        return self.father_name

    @father_name.setter
    def father_name(self, father_name):
        self.father_name = father_name

    @property
    def mother_name(self):
        return self.mother_name

    @mother_name.setter
    def mother_name(self, mother_name):
        self.mother_name = mother_name

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, address):
        self.address = address

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, number):
        self.number = number

    @property
    def complement(self):
        return self.complement

    @complement.setter
    def complement(self, complement):
        self.complement = complement

    @property
    def neighbourhood(self):
        return self.neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, neighbourhood):
        self.neighbourhood = neighbourhood

    @property
    def city(self):
        return self.city

    @city.setter
    def city(self, city):
        self.city = city

    @property
    def state(self):
        return self.state

    @state.setter
    def state(self, state):
        self.state = state

    @property
    def postal_code(self):
        return self.postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self.postal_code = postal_code

    @property
    def home_phone(self):
        return self.home_phone

    @home_phone.setter
    def home_phone(self, home_phone):
        self.home_phone = home_phone

    @property
    def mobile_phone(self):
        return self.mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        self.mobile_phone = mobile_phone

    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def rg(self):
        return self.rg

    @rg.setter
    def rg(self, rg):
        self.rg = rg

    @property
    def emitter(self):
        return self.emitter

    @emitter.setter
    def emitter(self, emitter):
        self.emitter = emitter

    @property
    def home_town(self):
        return self.home_town

    @home_town.setter
    def home_town(self, home_town):
        self.home_town = home_town

    @property
    def home_state(self):
        return self.home_state

    @home_state.setter
    def home_state(self, home_state):
        self.home_state = home_state

    @property
    def civil_state(self):
        return self.civil_state

    @civil_state.setter
    def civil_state(self, civil_state):
        self.civil_state = civil_state

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, gender):
        self.gender = gender

    @property
    def scholarship(self):
        return self.scholarship

    @scholarship.setter
    def scholarship(self, scholarship):
        self.scholarship = scholarship

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, course):
        self.course = course

    @property
    def company(self):
        return self.company

    @company.setter
    def company(self, company):
        self.company = company

    @property
    def company_time(self):
        return self.company_time

    @company_time.setter
    def company_time(self, company_time):
        self.company_time = company_time

    @property
    def ocupation(self):
        return self.ocupation

    @ocupation.setter
    def ocupation(self, ocupation):
        self.ocupation = ocupation

    @property
    def company_address(self):
        return self.company_address

    @company_address.setter
    def company_address(self, company_address):
        self.company_address = company_address

    @property
    def company_neighbourhood(self):
        return self.company_neighbourhood

    @company_neighbourhood.setter
    def company_neighbourhood(self, company_neighbourhood):
        self.company_neighbourhood = company_neighbourhood

    @property
    def company_number(self):
        return self.company_number

    @company_number.setter
    def company_number(self, company_number):
        self.company_number = company_number

    @property
    def company_city(self):
        return self.company_city

    @company_city.setter
    def company_city(self, company_city):
        self.company_city = company_city

    @property
    def company_state(self):
        return self.company_state

    @company_state.setter
    def company_state(self, company_state):
        self.company_state = company_state

    @property
    def company_postal_code(self):
        return self.company_postal_code

    @company_postal_code.setter
    def company_postal_code(self, company_postal_code):
        self.company_postal_code = company_postal_code

    @property
    def company_phone(self):
        return self.company_phone

    @company_phone.setter
    def company_phone(self, company_phone):
        self.company_phone = company_phone
