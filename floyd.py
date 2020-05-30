# declaramos infinito ya establecido en python
infinito = float('inf')

# metodo de floyd en python

print('\n -------------------------- Método de Floyd --------------------------')

# pedimos numero de nodos hasta que se ingrese un valor valido
n = int(input('\n Ingresa la cantidad de nodos: '))
while (n<=0 or n>10):
    n = int(input(' Ingresa la cantidad de nodos: '))

# ingresamos los valores de las matrices c y z

matriz_z = []
matriz_c = []

# matriz c
print('\n Ingresa las longitudes(si alguna es infinito ingresa la letra i):\n')
for row in range(0,n):
    costos = []
    for element in range(0,n):
        costo_ruta = input(' Ingresa el costo del nodo '+ str(row+1) +' al nodo '+ str(element+1) +': ')
        if costo_ruta == 'i' or costo_ruta == 'I':
            costo_ruta = infinito
        while(costo_ruta == ''):
            costo_ruta = input(' Ingresa el costo del nodo '+ str(row+1) +' al nodo '+ str(element+1) +': ')
            if costo_ruta == 'i' or costo_ruta == 'I':
                costo_ruta = infinito
        costos.append(costo_ruta)
    matriz_c.append(costos)

print('\n Matriz de longitudes:\n')
for row in matriz_c:
    for element in row:
        print(element, end=' ')
    print()

# matriz z
for i in range(0,n):
    costo = []
    for j in range(0,n):
        costo.append(i+1)
    matriz_z.append(costo)

print('\n Matriz de nodos antecesores:\n')

for row in matriz_z:
    for element in row:
        print(element, end=' ')
    print()

print()

# -----------------------   revisamos la existencia de nodos aislados  -----------------------
fila_ais = False
col_ais = False
print('\n ----------- NODOS AISLADOS -----------\n')
for i in range(0, len(matriz_c)):
    cont_col=0
    cont_fila=0
    for j in range(0, len(matriz_c)):
        if(matriz_c[j][i]==infinito):
            cont_col += 1
        if(matriz_c[i][j]==infinito):
            cont_fila += 1
    if cont_col == len(matriz_c)-1:
        print(' El nodo '+str(i+1)+' está aislado en su columna')
        fila_ais = True
    if cont_fila == len(matriz_c)-1:
        print(' El nodo '+str(i+1)+' está aislado en su fila')
        col_ais = True

# ----------------------------------------------  metodo de floyd  ----------------------------------------------
matriz_nueva = []

k = 0
while(k<len(matriz_c)):

    print('\n Iteración K = '+ str(k+1) +'\n')

    lista_fila = []
    lista_col = []
    matriz_anterior = matriz_c
    
    for i in range(0, len(matriz_c)):
        if i != k:
            if matriz_c[i][k]!=infinito:
                lista_col.append(i)
            if matriz_c[k][i]!=infinito:
                lista_fila.append(i)

    if len(lista_fila)==0 or len(lista_col)==0:
        print(' Pasamos a la siguiente iteración pues el nodo está aislado')
    else:
        for i in range(0, len(lista_col)):
            if int(matriz_c[i][i]) < 0:
                print(' Hay un circuito negativo en C'+str(i+1)+str(i+1))
            elif int(matriz_c[i][i]) >= 0 and k==len(matriz_c)-1:
                break
            elif int(matriz_c[i][i]) >= 0 and k<len(matriz_c)-1:
                for j in range(0, len(lista_fila)):

                    minimo = min(float(matriz_c[lista_col[i]][lista_fila[j]]), float(matriz_c[lista_col[i]][k]) + float(matriz_c[k][lista_fila[j]]))

                    if(float(minimo) < float(matriz_c[lista_col[i]][lista_fila[j]])):
                        print(" C"+str(lista_col[i]+1)+str(lista_fila[j]+1)+" = min{"+str(matriz_c[lista_col[i]][lista_fila[j]])+", "+ str(matriz_c[lista_col[i]][k]) +" + ("+ str(matriz_c[k][lista_fila[j]]) +")} = "+str(minimo))
                        matriz_c[lista_col[i]][lista_fila[j]] = minimo  
                        matriz_z[lista_col[i]][lista_fila[j]] = matriz_z[k][lista_fila[j]]  

        # imprimimos las nuevas matrices
        print('\n Nueva matriz de longitudes:\n')
        for i in matriz_c:
            for j in i:
                if j != infinito:
                    print(int(j), end=' ')
                else:
                    print(j, end=' ')
            print()

        print('\n Nueva matriz de nodos antecesores:\n')
        for row in matriz_z:
            for element in row:
                print(element, end=' ')
            print()

        matriz_nueva = matriz_c

    k+=1
    # fin del metodo

# -------------------------------------- RUTA MAS CORTA --------------------------------------

print('\n ---------------------- RUTA MÁS CORTA ----------------------')

opcion = 0

while(opcion!=2):
    print('\n ¿Qué quieres realizar?\n\n 1. Ruta entre dos nodos específicos\n 2. Terminar')

    opcion = int(input('\n Ingresa la opción: '))

    if opcion == 1:
        print('\n Introduce de que nodo a que nodo quieres la ruta:')

        nodo1 = int(input(' Nodo 1: '))
        while nodo1>len(matriz_z) or nodo1<=0:
            nodo1 = int(input(' Nodo 1: '))

        nodo2 = int(input(' Nodo 2: '))
        while nodo2>len(matriz_z) or nodo1<=0:    
            nodo2 = int(input(' Nodo 2: '))

        # ruta
        if matriz_c[nodo1-1][nodo2-1] == infinito:
            print(' No se puede ir del nodo '+str(nodo1)+' al nodo '+str(nodo2))
        else:
            lista_ruta = []
            lista_ruta.append(nodo2)
            valor_nuevo = matriz_z[nodo1-1][nodo2-1]
            lista_ruta.append(valor_nuevo)
            
            i=1
            while i < len(matriz_z):
                valor_nuevo = matriz_z[nodo1-1][lista_ruta[i]-1]

                if valor_nuevo == nodo1:
                    lista_ruta.append(nodo1)
                    break
                else:
                    lista_ruta.append(valor_nuevo)
                
                i+=1

            lista_ruta.reverse()
            if lista_ruta[0] == lista_ruta[1]:
                lista_ruta.pop(0)
                print(' Ruta: '+str(lista_ruta))
            else:
                print(' Ruta: '+str(lista_ruta))

            # costo de ruta
            total = 0
            i=1
            for i in range(1,len(lista_ruta)):
                costo = matriz_nueva[lista_ruta[i-1]-1][lista_ruta[i]-1]
                total += float(costo)
            
            print(' Costo: '+str(int(total)))
