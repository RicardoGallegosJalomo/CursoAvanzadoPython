diccionario = {'c1':'valor 1','c2': 'valor 2'}
print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente ={'nombre': 'Ricardo','apellido':'Perez','peso':88,'talla':1.76}

consulta = (cliente['apellido'])
print(consulta)

dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}

print(dic['c2'][1])
print(dic['c3']['s2'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}

print(dic['c2'][1].upper())

dic = {1:'a',2:'b'}
dic[3] = 'c' # adiciona un valor
print(dic)

dic[2] = 'B'
print(dic) # modifica el valor 

print(dic.keys()) # imprime en pantalla todas las llaves
print(dic.values()) # imprime en patalla los valores
print(dic.items()) # imprime en pantalla todo el diccionario

mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points":9,"points":[10,300,15]}}
print(mi_dict['puntos']['points'][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pasi'] = 'Colombia'

print(mi_dic.items())