class PhoneBook:

    def __init__(self, name):
        self.name = name

        self.contacts = []

    # def show_contacts(self, contact):
    #     self.contacts.values(contact)

    def add_contact(self, contact):
        self.contacts.append(contact)
        #
        # def del_contact(self, contact):
        #     self.contacts.popitem(contact)
        #
        # def find_favor_contacts(self, contact):
        #     self.contacts.items(contact)
        #
        # def find_contact(self):
        # pass


class Contact:

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

        self.additional_information = {}

    def __str__(self):
        return str(self.__dict__)

    def add_information(self, email, add_num, social_network, *args, **kwargs):
        self.additional_information.update(email)
        self.additional_information.update(add_num)
        self.additional_information.update(social_network)

    favor = False


book = PhoneBook('test')
c1 = Contact('jora', 'sidorov', '+7918')

book.add_contact(c1)
print(book.contacts)
print(c1)
