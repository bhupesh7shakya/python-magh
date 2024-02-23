person={
    'name': 'Bikesh',
    'age': '22',
    'address':'jadibuti',
    'members':[
        'friend',
        'friends' ,
        'double battery'
    ]
    
}
print(person['name'], person['age'], person['address']) 
print("members:")
for member in person['members']:
    print(member)

#     # Update the 'members' list
# person['members'] = ['friend']

# # Print the updated 'members' list
# print("Members:", person['members'])