person = {
   "name": "Sebastian",
   "surname": "Duda",
   "age": 20,
   "hobby": ["swimming","crusades"],
   "married": False,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
def dis_name(dict):
    result=dict["name"]
    return result
def dis_hobby(dict):
    result=dict['hobby']
    return result
def dis_dictionary(dict):
    result=dict
    return result
def dis_changesurname(dict,newsurname):
    dict['surname']=f'{newsurname}'
    result=dict['surname']
    return result
def dis_changemarriegestatus(dict):
    if dict['married']:
        dict['married']=False
    else:
        dict['married']=True
    result=dict['married']
    return result
def dis_addgender(dict,gender):
    dict['gender']=gender
    result=dict['gender']
    return result
def dis_addhobby(dict,hobby):
    dict['hobby'].append(hobby)
    result=dict['hobby']
    return result
def dis_addworkphone(dict,workphone):
    dict['phone']['workphone']=f"'{workphone}'"
    result=dict['phone']
    return result
def dis_iterateover(dict):
    for key,value in dict.items():
     print(f"{key} : {value}")
    result='end'
    return result

print(dis_name(person))
print(dis_hobby(person))
print(dis_dictionary(person))
print(dis_changesurname(person,"Banach"))
print(dis_changemarriegestatus(person))
print(dis_addgender(person,"male"))
print(dis_addhobby(person,'bicycle'))
print(dis_addworkphone(person,"3131314444"))
print(dis_iterateover(person))
