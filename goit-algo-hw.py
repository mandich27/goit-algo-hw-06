from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, name):
        super().__init__(name)
		
class Phone(Field):
    # реалізація класу
    def __init__(self, phone):
        super().__init__(phone)
        if len(self.value) != 10: 
            raise ValueError("Phone number must be exactly 10 digits")
        if not phone.isdigit():
            raise ValueError("Phone number must be exactly only digits")
        
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self,old_phone, new_phone):
        if old_phone in self.phones:
            for p in self.phones:
                if p.value == old_phone:
                    p.value = new_phone
        else:
            raise ValueError (f'This number: {old_phone} does not exist')

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
         

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
         

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            print(f'Contact {name} delete')
        else:
            print(f'Contact {name} not found')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        

	

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
