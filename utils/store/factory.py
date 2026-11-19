from random import randint
from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(475,573)

fake = Faker('pt-br')

def make_shopp():
    return {
        'title': fake.sentence(nb_words=6),
        'store_name': fake.sentence(nb_words=2),
        'price': fake.pyfloat(
            left_digits=3,
            right_digits=2,
            positive=True,
            min_value= 10.00,
            max_value= 280.00,
        ),
        'id': fake.pyint(
            min_value=1,
            max_value=10,
        ),

        'category': {
            'name': fake.word()
        },
        'category_specific':{
            'name_specific': fake.word()
        },
        'cover': {
            'url': 'https://picsum.photos/%s/%s' % rand_ratio(),
        },


    }