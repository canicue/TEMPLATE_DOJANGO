contenido=["hola1","chau2","chau2","chau2","mal2","mal2","29","34","22","22","44","44","0","hostia"]
lista = []
lista_final = []
for numero in contenido:
    lista += numero.split()
lista.sort()
set_lista = set(lista)
set_lista = list(set_lista)
set_lista.sort()
diccio={}
print "Valor:Ocurrencias"
for numero in set_lista:
    lista_final.append((numero,lista.count(numero)))
    diccio[numero]=lista.count(numero)
lista_final.sort(reverse=True)
print lista_final
print diccio
