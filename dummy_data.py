import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from products.models import Product,Brand,Review

def seed_brand(n):
    fake = Faker()
    images=['01.jbg','02.jbg','03.jbg','04.jbg','05.jbg','06.jbg','07.jbg','08.jbg','09.jbg','10.jbg']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f"brand/{images[random.randint(0,9)]}"
        )
    print(f"{n} Brands was added successfully")

def seed_products(n):
    fake = Faker()
    flag_types=['New','Sale','Feature']
    brands =Brand.objects.all()
    images=['01.jbg','02.jbg','03.jbg','04.jbg','05.jbg','06.jbg','07.jbg','08.jbg','09.jbg','10.jbg']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            flag = flag_types[random.randint(0,2)],
            price= round(random.uniform(20.99,99.99),2),
            image = f"product/{images[random.randint(0,9)]}",
            sku = random.randint(100,100000),
            subtitle = fake.text(max_nb_char=450),
            description = fake.text(max_nb_char=4000),
            brand = brands[random.randint(0,len(brands)-1)],
        )
    print(f"{n} Brands was added successfully")


def seed_reviews(n):
    pass

seed_brand(200)
seed_products(1500)