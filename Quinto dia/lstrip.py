str = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(str.lstrip(',:_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(4,'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)