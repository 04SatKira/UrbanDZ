my_dict={'Kira': 1900,'Zhenya': 1988,'Pasha':2012,'Tanya':1989}
print(my_dict)
print(my_dict.get('Pasha'))
print(my_dict.get('Alex', 'Пользователь не найден'))
my_dict.update({'Arina': 2017, 'Polina':2016})
print(my_dict)
del_name=my_dict.pop('Tanya')
print(del_name)
print(my_dict)
my_set={1990,1989,'Kira','Zhenya','Kira',1990,'Tanya',1988,1989,'Zhenya'}
print(my_set)
my_set.update({2012, (1,2,3)})
my_set.remove('Tanya')
print(my_set)