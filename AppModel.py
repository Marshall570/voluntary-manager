# -*- coding: utf-8 -*-

class AppModel:
    def __init__(self, unique_id=None, registered=None, name=None, father=None, mother=None, address=None, number=None, complement=None, neighbourhood=None, city=None, state=None, postal_code=None, home_phone=None, mobile_phone=None, course=None, cpf=None, rg=None, emitter=None, home_town=None, home_state=None, birth_date=None, civil_state=None, gender=None, scholarship=None, email=None, company_name=None, company_time=None, ocupation=None, company_address=None, company_neighbourhood=None, company_number=None, company_city=None, company_state=None, company_postal_code=None, company_phone=None):
        self._unique_id = unique_id
        self._registered = registered
        self._name = name
        self._father = father
        self._mother = mother
        self._address = address
        self._number = number
        self._complement = complement
        self._neighbourhood = neighbourhood
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._home_phone = home_phone
        self._mobile_phone = mobile_phone
        self._cpf = cpf
        self._rg = rg
        self._emitter = emitter
        self._home_town = home_town
        self._home_state = home_state
        self._birth_date = birth_date
        self._civil_state = civil_state
        self._gender = gender
        self._scholarship = scholarship
        self._email = email
        self._course = course
        self._company_name = company_name
        self._company_time = company_time
        self._ocupation = ocupation
        self._company_address = company_address
        self._company_neighbourhood = company_neighbourhood
        self._company_number = company_number
        self._company_city = company_city
        self._company_state = company_state
        self._company_postal_code = company_postal_code
        self._company_phone = company_phone

    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, UniqueId):
        self._unique_id = UniqueId

    @property
    def registered(self):
        return self._registered

    @registered.setter
    def registered(self, Registered):
        self._registered = Registered

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, Name):
        self._name = Name

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, FatherName):
        self._father = FatherName

    @property
    def mother(self):
        return self._mother

    @mother.setter
    def mother(self, MotherName):
        self._mother = MotherName

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, Address):
        self._address = Address

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, Number):
        self._number = Number

    @property
    def complement(self):
        return self._complement

    @complement.setter
    def complement(self, Complement):
        self._complement = Complement

    @property
    def neighbourhood(self):
        return self._neighbourhood

    @neighbourhood.setter
    def neighbourhood(self, Neighbourhood):
        self._neighbourhood = Neighbourhood

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, City):
        self._city = City

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, State):
        self._state = State

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, PostalCode):
        self._postal_code = PostalCode

    @property
    def home_phone(self):
        return self._home_phone

    @home_phone.setter
    def home_phone(self, HomePhone):
        self._home_phone = HomePhone

    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, MobilePhone):
        self._mobile_phone = MobilePhone

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, Cpf):
        self._cpf = Cpf

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, Rg):
        self._rg = Rg

    @property
    def emitter(self):
        return self._emitter

    @emitter.setter
    def emitter(self, Emitter):
        self._emitter = Emitter

    @property
    def home_town(self):
        return self._home_town

    @home_town.setter
    def home_town(self, HomeTown):
        self._home_town = HomeTown

    @property
    def home_state(self):
        return self._home_state

    @home_state.setter
    def home_state(self, HomeState):
        self._home_state = HomeState
    
    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, BirthDate):
        self._birth_date = BirthDate

    @property
    def civil_state(self):
        return self._civil_state

    @civil_state.setter
    def civil_state(self, CivilState):
        self._civil_state = CivilState

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, Gender):
        self._gender = Gender

    @property
    def scholarship(self):
        return self._scholarship

    @scholarship.setter
    def scholarship(self, Scholarship):
        self._scholarship = Scholarship

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, Email):
        self._email = Email

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, Course):
        self._course = Course

    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, Company):
        self._company_name = Company

    @property
    def company_time(self):
        return self._company_time

    @company_time.setter
    def company_time(self, CompanyTime):
        self._company_time = CompanyTime

    @property
    def ocupation(self):
        return self._ocupation

    @ocupation.setter
    def ocupation(self, Ocupation):
        self._ocupation = Ocupation

    @property
    def company_address(self):
        return self._company_address

    @company_address.setter
    def company_address(self, CompanyAddress):
        self._company_address = CompanyAddress

    @property
    def company_neighbourhood(self):
        return self._company_neighbourhood

    @company_neighbourhood.setter
    def company_neighbourhood(self, CompanyNeighbourhood):
        self._company_neighbourhood = CompanyNeighbourhood

    @property
    def company_number(self):
        return self._company_number

    @company_number.setter
    def company_number(self, CompanyNumber):
        self._company_number = CompanyNumber

    @property
    def company_city(self):
        return self._company_city

    @company_city.setter
    def company_city(self, CompanyCity):
        self._company_city = CompanyCity

    @property
    def company_state(self):
        return self._company_state

    @company_state.setter
    def company_state(self, CompanyState):
        self._company_state = CompanyState

    @property
    def company_postal_code(self):
        return self._company_postal_code

    @company_postal_code.setter
    def company_postal_code(self, CompanyPostalCode):
        self._company_postal_code = CompanyPostalCode

    @property
    def company_phone(self):
        return self._company_phone

    @company_phone.setter
    def company_phone(self, CompanyPhone):
        self._company_phone = CompanyPhone
