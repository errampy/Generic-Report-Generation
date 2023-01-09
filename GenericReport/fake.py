import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GenericReport.settings")
import django
django.setup()
from faker import factory,Faker
from testapp.models import *


def generate_customer(n):
    fake = Faker()
    for i in range(0,n):
        name=fake.name()
        email_address=fake.email()
        phone_no=fake.phone_number()
        address=fake.address()
        print(f'name : {name} | email_address : {email_address} | phone_no : {phone_no} | address : {address} ')
        records=Customer.objects.get_or_create(
            name = name,email_address=email_address,mobile_no=phone_no,address=address
        )
    return True
n=int(input('Enter the number :- '))
abc=generate_customer(n)
if abc:
    print(f'Successfully created "{n}" no. ofrRows')

