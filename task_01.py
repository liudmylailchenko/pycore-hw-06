from collections import UserDict
from re import fullmatch

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not value:
            raise ValueError("Name can't be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Phone number is not valid")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return fullmatch(r"\d{10}", phone) is not None

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone: str):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break
        else:
            raise ValueError(f"Phone {old_phone} not found")
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones) if self.phones else "No phones"
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Contact {name} not found")

