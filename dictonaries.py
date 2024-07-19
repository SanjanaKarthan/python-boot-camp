'''
DICTONARIES: It is mutable data structure
It has keys and pairs
keys cannot be repeated i.e keys are unique

SYNATX:-
dict_name=[key1:value1,key2:value2.....keyn:valuen)
'''
##example:-
'''
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
print(menu)               ### NORMAL
'''
'''
menu={

    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
menu['fruit_salad']=400      ###TO ADD
print(menu)
'''

'''
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
menu['chiken_kabab']=250     ###TO UDPDATE

print(menu)
'''

'''
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
menu.pop('tandoori_roti')    ###TO DELETE

print(menu)
'''
'''
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
print(menu.keys())          ###TO PRINT KEYS(rates)
print(menu)
'''
'''
menu={
    'chicken_biryani':555,
    'butter_chicken':450,
    'tandoori_roti':200,
    'chicken_kabab':300
    }
print(menu.values())        ###TO PRINT VALUES
for k,v in menu.items():
    print(k,'->',v)
'''


