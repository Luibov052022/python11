class Person:
    def __init__(self, name, midlename, lastname, numbers):
        self.name = name
        self.midlename = midlename
        self.lastname = lastname
        self.numbers = numbers

    def get_phone(self):
        return self.numbers.get("private")

    def get_name(self):
        return f' {self.lastname} {self.name} {self.midlename}'

    def get_work_phone(self):
        return self.numbers.get("work")

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.midlename} примите участие в нашем ' \
               f'беспроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, company_name, c_type, company_numbers, *args):
        self.company_name = company_name
        self.c_type = c_type
        self.company_numbers = company_numbers
        self.persons = args

    def get_phone(self):
        contact = self.company_numbers.get("contact")
        if not contact:
            for person in self.persons:
                phone = person.get_work_phone()
                if phone:
                    return phone
        else:
            return contact

    def get_name(self):
        return self.company_name

    def get_sms_text(self):
        return f'Для компании {self.company_name} есть супер предложение! ' \
               f'примите участие в конкурсе для {self.c_type}'    

def send_sms(*args):
    for i in args:
        number = i.get_phone()
        if number:
            print(f'Отправлено СМС на номер {number} с текстом: {i.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')

print('ПРИМЕР 1')
print('')
person1 = Person("Ivan", "Ivanonich", "Ivanov", {"private": "+787878787", "work": "+12148578"})
person2 = Person("Petrov", "Petrovicn", "Petrov", {"private": "+458787877"})
person3 = Person("Michail", "Amtonovich", "Sidorov", {"work": "+999778444"})
person4 = Person("Jon", "Unknown", "Doe", {})
company1 = Company("Bell", "OOO", {"contact": "+21445555"}, person3, person4)
company2 = Company("Cell", "AO", {"non_contact": "222"}, person2, person3)
company3 = Company("Dell", "LTD", {"non_contact": "333"}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
print('ПРИМЕР 2')
print('')
person5 = Person("Степан", "Петрович", "Джобсов", {"private": "555"})
person6 = Person("Боря", "Иванович", "Гейтсов", {"private": "777", "work": "888"})
person7 = Person("Семен", "Робертович", "Возняцкий", {"work": "789"})
person8 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company4 = Company("Яблочный комбинат", "OOO", {"contact": "111"}, person5, person6)
company5 = Company("ПластОкно", "AO", {"non_contact": "222"}, person6)
company6 = Company("Пингвинья ферма", "LTD", {"non_contact": "333"}, person8)
send_sms(person5, person6, person7, person8, company4, company5, company6)


