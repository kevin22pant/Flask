
nums = ['Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho','Nueve','Diez']
colors = ['Gris','Naranja','Amarillo','Verde','Azul','Rojo','Morado','Rosa','Marrón','Negro']


nums.reverse()
new_list = []



for i in range(len(nums)):
    new_list.append([nums[i], colors[i]])

print(new_list)
#print(nums)
#colors.append('Turquesa')
#colors.extend(['Turquesa','Cafe'])
#colors.insert(0, 'Turquesa')
#colors.clear()
#colors.append('Turquesa')
#colors_1 = colors.copy()
#print(colors_1)


"""for num in nums:
    output = f"[{num}, {colors[nums.index(num)]}]"
    print(output)
"""
#print([nums[0], colors[0]])

"""
ACTIVIDAD AHORA INVIERTE LA LISTA DE NUMS PARA PODER VER ELEMENTOS 
DE LA LISTA ['DIEZ''ROJO']

AL FINAL CREAR UNA NUEVA LISTA AMBOS ELEMENTOS
E IMPRIMIR LA NUEVA LISTA

"""