# 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
#  La función debe devolver una tupla que contenga la media y el estado.



def evaluar_media (lista_notas, nota_aprobado=5):
    media = sum (lista_notas) / len (lista_notas) #podriamos utilizar // para enteros
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)


notas = [4, 6, 5.5, 9]
resultado = evaluar_media (notas)
print (resultado)