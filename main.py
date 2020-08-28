class PhoneBook:

    def __init__(self, name):
        self.name = name

        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def show_contact(self, contact):
        if contact in self.contacts:
            return contact

    def del_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

    def find_contact(self, name):
        pass
        # if name == Contact.__name__:
        #     return Contact.__name__

    def find_favor_contact(self, fav):
        pass


class Contact:

    def __init__(self, name, surname, phone, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.inf = args, kwargs

    def favor(self):
        favor = False
        if not favor:
            return 'нет'
        else:
            return 'да'

    def __str__(self):
        return str(f'Имя:{self.name} \nФамилия:{self.surname} \nТелефон:{self.phone} \nВ избранных:{self.favor()}'
                   f' \nДополнительная информация:\n {self.inf}')



book = PhoneBook('test')
jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
alex = Contact('Alex', 'Bolt', '+74683126987', telegram='@Allexx', email='alex@bolt.com')

book.add_contact(jhon)
book.add_contact(alex)

#print(book.show_contact(alex))
#book.del_contact(alex)

print(book.contacts)
