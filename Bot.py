from collections import UserDict
from functools import reduce
import pickle
import datetime as dt
import re
from datetime import datetime as dtdt
import os

def input_error(func):                
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {str(e)}"
    return inner

class BaseClass:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    

class Phone(BaseClass):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print(f'Формат телефону: {phone} задано невірно.')
            raise main()
        

class Name(BaseClass):
    pass


class Birthday(BaseClass):
    def __init__(self, birthday):
        super().__init__(birthday)
        # print(f"birthday = {birthday}")
        pattern = r"\d+\.+\d+\.+\d+"
        da = re.findall(pattern, birthday)
        da = da[0]
        # print(f"   da = {da}")
        if len(da) != 10:
            print(f"Неправильне введення дати. Використовуйте шаблон: addbirthday [name] [YYYY.MM.DD]")
            raise main()   
        else:
            if dtdt.strptime(da, "%Y.%m.%d").date(): # перетворюємо дату народження в об’єкт date
                # print(f"   555 d = {da}")
                birthday = da 
                # print(f"   birthday = {birthday}")
            else:
                print(f"Неправильне введення дати. Використовуйте шаблон: addbirthday name YYYY.MM.DD")
                raise main()
        

class Record: 
    def __init__(self, name):
        self.name = name
        self.phones = None
        # self.birthday = []

    def add_date(self, args):
        self.birthday = args
        # print(f"self.birthday = {self.birthday}")
        Birthday(self.birthday)

    def add_phone(self, phon):
        self.phones = phon
        Phone(self.phones)

class AddressBook(UserDict):  # Клас для зберігання та управління записами
    def __init__(self):
        self.data1 = []

    @input_error
    def add_record(self, name, phones):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        kk = True
        for el in self.data1:
            # print(f"   el = {el} el[name]= {el["name"]} name = {name}")
            
            if "name" in el:
                if name==el["name"]:
                    el["phones"].append(phones)
                    kk = False
                    break
        if kk:
            a = {"name": name, "phones": [phones]}
            self.data1.append(a)
        self.save_to_file(r'D:\Projects\Module8\Module8\A1.pkl')
        print (f'Контакт користувача додано.')

    @input_error
    def add_birthday(self, name, birthday):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        for el in self.data1:
            # print(f"   el = {el} el[name]= {el["name"]} name = {name}")
            if name==el["name"]:
                a = {"birthday":birthday}
                print(f" birthday = {birthday}")
                el.update(a)
                # print(f" el = {el}")
                kk = False
                self.save_to_file(r'D:\Projects\Module8\Module8\A1.pkl')
                print (f'День народження користувача додано.')
                break
        if kk:
            print(f"Користувача {name} не знайдено: помилка вводу імені")

    @input_error
    def list(self):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        i = 0
        if len(self.data1) > 0:
            for value in self.data1:
                i +=1
                aa = value.get("name")
                bb = value.get("phones")
                string1 = ''
                for el in bb:
                    string1 += el + " "
                print(f"{i:2}. {aa:10} Телефон(и): {string1}")
        else:
            print("Список пустий")

    @input_error
    def find_birthday(self, name):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        for el in self.data1:
            kk = True
            if "name" in el and "birthday" in el:
                if name==el["name"]:
                    birthday = el["birthday"]
                    print(f"День народження користувача {name}: {birthday}")
                    kk = False
                    break
        if kk:
            print(f"Помилка вводу імені користувача або дані про день народження відсутні.")

    @input_error
    def find_name(self, name):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        kk = False
        i = 0
        for el in self.data1:
            if "name" in el:
                if name==el["name"]:
                    kk = True
                    len1 = len(el["phones"])
                    if len1 > 1:
                        print(f"{len1} телефони користувача {name} знайдено:")  
                    else:
                        print(f"Телефон користувача {name} знайдено:")  
                    for value in el['phones']:
                        i +=1
                        print(f"{i:5}.  {value}")            
        if kk !=True:
            print(f"Телефон користувача {name} не знайдено.")   

    @input_error
    def remove_name(self, name):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        i = -1
        kk = True
        for el in self.data1: 
            i +=1
            if "name" in el:
                    if name==el["name"]:
                        self.data1.pop(i)
                        # print(f" self.data1.pop  = {self.data1}     s = {s}")
                        kk = False
                        print(f"Інформація про користувача {name} видалена") 
                        # self.erase_pic(r'D:\Projects\Module8\Module8\A1.pkl')
                        self.save_to_file(r'D:\Projects\Module8\Module8\A1.pkl')
        if kk:
            print(f"Користувача {name} не знайдено: помилка вводу") 

    # def change_name(self, name, name2):
    #     self.checit_json(r'D:\Projects\Module7\Module7-1\A1.json')
    #     if self.data1.get(name) != None:
    #         # print(f" name = {name} name2 = {name2} a = {self.data1.get(name)}")
    #         self.data1[name2] = self.data1.pop(name)
    #         self.erase_json(r'D:\Projects\Module7\Module7-1\A1.json')
    #         self.write_json(r'D:\Projects\Module7\Module7-1\A1.json')
    #         print(f"Ім'я користувача {name} змінено на {name2}") 
    #     else: 
    #         print(f"Користувача {name} не знайдено: помилка вводу імені") 

    @input_error
    def change_phone(self, name, phon):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        i = 0
        kk = True
        for el in self.data1: 
                if name==el["name"]:
                    for value in el['phones']:
                        i +=1
                        print(f"{i:5}.  {value}")   
                    if i > 1:
                        number_tel = input("Який телефон змінюємо: введіть його порядковий номер:")
                        if number_tel.isdigit():
                            number_tel = int(number_tel)
                            if number_tel > 0 and number_tel <= len(el["phones"]): 
                                el["phones"][number_tel - 1] = phon
                            else:
                                print(f"Невірний порядковий номер {number_tel}")
                                raise main()
                        else:
                            print(f"Невірний порядковий номер {number_tel}")
                            raise main()
                    else:
                        el["phones"] = [phon]
                    # self.erase_pic(r'D:\Projects\Module8\Module8\A1.pkl')
                    self.save_to_file(r'D:\Projects\Module8\Module8\A1.pkl')
                    print(f"Телефон користувача {name} змінено на {phon}:")
                    kk = False
                    i = 0
                    for val in el["phones"]:
                        i +=1
                        print(f"{i:5}.  {val}") 
        if kk: 
            print(f"Користувача {name} не знайдено: помилка вводу імені")
            raise main()

    @input_error
    def get_upcoming_birthdays(self):
        self.checit_pic(r'D:\Projects\Module8\Module8\A1.pkl')
        tdate=dtdt.today().date() # беремо сьогоднішню дату
        birthdays=[] # створюємо список для результатів
        for user in self.data1: # перебираємо користувачів
            if 'birthday' not in user:
                continue
            bdate=user["birthday"] # отримуємо дату народження людини у вигляді рядка
            bdate=str(tdate.year)+bdate[4:] # Замінюємо рік на поточний
            bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
            week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
            days_between=(bdate-tdate).days # рахуємо різницю між зараз і днем народження цьогоріч у днях
            # print(f" days_between = {days_between}")
            if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні
                if week_day<6: #  якщо пн-пт
                    birthdays.append({'name':user['name'], 'birthday':bdate.strftime("%Y.%m.%d")}) 
                    # Додаємо запис у список.
                else:
                    if (bdate+dt.timedelta(days=1)).weekday()==0:# якщо неділя
                        birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
                    elif (bdate+dt.timedelta(days=2)).weekday()==0: #якщо субота
                        birthdays.append({'name':user['name'], 'birthday':(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
        # print(f" birthdays = {birthdays}")
        i = 0
        if len(birthdays) > 0:
            print("Необхідно привітати наступних користувачів:")
            for el in birthdays:
                i +=1
                print(f"{i:5}.  День народження користувача {el["name"]}: {el["birthday"]}")
        else:
            print("На найближчий час днів народжень користувачів не передбачається")

    def save_to_file(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.data1, f)

    def checit_pic(self, filename): 
        if os.path.exists("A1.pkl") == False:
            self.data1 = []
            print(f"Файл пустий")
            with open("A1.pkl", 'wb') as f:
                pickle.dump(self.data1, f)
        else:
            with open(filename, "rb") as f: 
                self.data1= pickle.load(f)
                kk = True
            return kk
        
    # def erase_pic(self, filename):
    #     with open(filename, 'w') as file:
    #         pickle.dump([], file)

def parse_input(user_input): #ввод команди та аргументів
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    # args0.clear()
    # for a in args:
    #     print(f" a = {a}")
    #     if str(a).isdigit():
    #         args0.append(a)
    #         print(f" 0 args0 = {args0}")
    # print(f" args0 = {args0}")
    return cmd, *args

def main():
        addressBook = AddressBook()
        print("Ласкаво просимо до бота-помічника!")
        print("Формат команд:\nclose або exit\nadd [name] [phone]\nlist\nfindname [name]\nremove [name]\nchangephone [name] [new phone]\naddbirthday [name] [YYYY.MM.DD]")
        print("findbirthday [name]\nbirthday")
        while True: 
            user_input = input("Введіть команду: ")
            command, *args = parse_input(user_input)
            # print(f"000 comand = {command} args = {args}")
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                record = Record(args[0])
                record.add_phone(args[1])
                addressBook.add_record(record.name, record.phones)
            elif command == "list":
                addressBook.list() 
            elif command == "findname":
                addressBook.find_name(args[0])
            elif command == "remove":
                addressBook.remove_name(args[0])
            # elif command == "changename":
            #     addressBook.change_name(args[0],args[1])
            elif command == "changephone":
                    record = Record(args[0])
                    record.add_phone(args[1])
                    addressBook.change_phone(record.name, record.phones)
            elif command == "addbirthday":
                record = Record(args[0])
                record.add_date(args[1])  # birthday
                addressBook.add_birthday(record.name, record.birthday)
            elif command == "findbirthday":
                addressBook.find_birthday(args[0])
            elif command == "birthday":
                addressBook.get_upcoming_birthdays()
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()