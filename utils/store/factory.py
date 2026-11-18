from random import randint
from faker import Faker

def rand_ration():
    return randint(840, 900), randint(475,573)

fake = Faker('pt-br')

def make_shopp():
    return {
        'title': fake.sentence(nb_words=6),
        'store_name': fake.sentence(nb_words=2),
        'price': fake.pyfloat(),

        'category': {
            'name': fake.word()
        },
        'cover': {
            'url':'https://loremflickr.com/%s/%s/jewelry' %rand_ration()
        },
    }
