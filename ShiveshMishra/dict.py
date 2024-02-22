# person={
#     'name':'ram',
#     'age':25,
#     'city':'janakapur',
#     'family_members':{
#         'father':'Dasharatha', 
#         'mother':'gita',
#         'sister':'jaya',
#         'brother':'raaam'
       
#     }
# }
# print(person['family_members  ']['father'])
 
person={
'name':'ram',
'age':25,
'city':'janakapur',
'family_members':[
    'father','mother','brother'
    
    
]
}
print(person['family_members'][1][2])