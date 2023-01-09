from django import template
register = template.Library()

# def find_the_dict_value(value,s):
#     print(f'VALUE : {value} == {type(value)}| S : {s} == {type(s)}')
#     print('#'*30)
#     data=value
#     our_data=data
#     return 'Mohan'
# register.filter('fields',find_the_dict_value)


def find_the_dict_value(value,s):
    if isinstance(value,dict) and isinstance(s,str) and s != 'new_data,new_var':
        print(f'VALUE : {value} == {type(value)}| S : {s} == {type(s)}')
        print('#'*30)
        data=value
        our_data=data[s]
        print('Our Data ',our_data)
        return our_data
    # else:
    #     print(f'VALUE : {value} == {type(value)}| S : {s} == {type(s)}')
    #     print('Thankyou Not Executing if block')
    #     return 'Ram'
register.filter('fields',find_the_dict_value)
