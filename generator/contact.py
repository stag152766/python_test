from model.contact import Contact
import string
import random
import os
import jsonpickle


n = 5
f = 'data/contact.json'

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phones(prefix, maxlen):
    symbols = string.digits + string.punctuation + " " * 5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname='', homephone='', lastname='', secondaryphone='', workphone='',
                    mobilephone='')] + \
           [Contact(firstname=random_string('firstname', 10), lastname=random_string('lastname', 20),
                    homephone=random_phones('72', 10), workphone=random_phones('82', 10),
                    mobilephone=random_phones('77', 10), secondaryphone=random_phones('83', 10)) for x in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))