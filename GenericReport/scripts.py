l1=['ram','vikash','rajesh','ranju','manju']
l2=['ram','vikash','rajesh','ranju']

check = all(item in l1 for item in l2)
print('Check ',check)