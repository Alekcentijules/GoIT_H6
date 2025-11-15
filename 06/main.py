from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value,):
        super().__init__(value)
        

class Phone(Field):
    def __init__(self, value):
        if not len(value) == 10:   
            raise ValueError("The length of the telephone number must not exceed 10 digits.")
        elif not value.isdigit():
            raise ValueError("Values must consist of numbers.")
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str):
        phone = Phone(phone_str)
        self.phones.append(phone)
    
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        if not any(p.value == old_phone for p in self.phones):
            raise ValueError("Old phone number not found.")
        
        removed = False
        new_phones = []
        for p in self.phones:
            if p.value == old_phone and not removed:
                removed = True
                continue
            new_phones.append(p)
        new_phones.append(Phone(new_phone))
        self.phones = new_phones

    def find_phone(self, phone: str):
        if not len(phone) == 10:    
            raise ValueError("The length of the telephone number must not exceed 10 digits.")
        elif not phone.isdigit():
            raise ValueError("Values must consist of numbers.")
        
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name: str):
        return self.data.get(name)
    
    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


book = AddressBook()

johny_record = Record('Johny')
johny_record.add_phone('3939393939')
johny_record.add_phone('6464646333')

book.add_record(johny_record)

jane_record = Record('Jane')
jane_record.add_phone('4365464563')
jane_record.add_phone('4365464563')
book.add_record(jane_record)

print(book)

jane = book.find('Jane')
jane.edit_phone('4365464563', '2828282828')

print(jane)

found_phone = jane.find_phone('2828282828')
print(f"{jane.name}: {found_phone}")

book.delete('John')
print(book)