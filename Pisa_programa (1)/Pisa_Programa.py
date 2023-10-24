import io
import random


# Jorge
def regresar():
    # Le pido al usuario que seleccione una opcion
    opcion = int(input("""Si quieres la explicacion a tu problema presiona(1) 
  y te mostrare links a yt, si deseas volver al menu(2) """))
    # Escoge entre la opcion solucion que llama a su respectiva funcion o menu
    if opcion == 1:
        solucion()
    if opcion == 2:
        main()
    else:
        print("Seleccione una opcion valida")
        regresar()


def solucion():
    # Lee el archivo que contiene referencias linea por linea y lo imprime
    file = open("pisa.txt", "r")
    text = file.readlines()
    for line in text:
        print(line)


# Mentor

def buscar_resultadop(resultado):
    if resultado == "Si":
        print("La respuesta es correcta!!\n")
    elif resultado == "No":
        print("La respuesta es incorrecta\n")
    else:
        print("La opcion no es válida\n")


def buscar_resultadon(resultado):
    if resultado == "Si":
        print("La respuesta es incorrecta\n")
    elif resultado == "No":
        print("La respuesta es correcta!!\n")
    else:
        print("La opcion no es válida\n")


def buscar_resultadoint(resultado_int, num):
    if resultado_int == num:
        print("La respuesta es correcta!!\n")
    else:
        print("La respuesta es incorrecta \n")

#Convierte una variable entera en string y lo evalua con su caracter en formato string
def resultado_str(resultado_int,caracter):
    resultado_int=str(resultado_int)
    if resultado_int==str(caracter):
        print ("La respuesta es correcta!!\n")
    elif resultado_int!=str(caracter):
        print("La respuesta es incorrecta\n")
        
#Imprime los archivos al recibir el nombre de dicho archivo
def imprimir_archivo(titulo):
    titulo=str(titulo)+".txt"
    archivo = open(titulo,"r")
    texto = archivo.read()
    print (texto)
    archivo.close()
#Almacenar una variable en forma string dada por el usuario, la capitaliza y evalua    
def inp_capitalize_str(texto):
    resultado_tres=str(input(texto).capitalize())
    buscar_resultadon(resultado_tres)

#Mentor
def ejercicios_PISA():
     #Inicio del ciclo para que el usuario pueda resolver los ejercicios aleatoriamente
    while True:
        #Centrar el título del menú
        titulo = "Ejercicios de Práctica PISA".upper()
        print (titulo.center(118," "))
        #Texto del menu en formato string
        print ("\n1. El concierto de rock\n2. El sueño de las focas".upper())
        print ("3. Estatura de los alumnos\n4. Selección Pizza\n5. El Patio\n0. Salir".upper())
        #Se pide al usuario la seleccion del menú al que desea ingresar o si desea salir
        seleccion = str(input("\nPresione la opción deseada: "))
        if seleccion == "1":
            print()
            #Se desarrolla la primera pregunta modelo PISA usando archivos, condiciones y funciones
            imprimir_archivo("ejercicio1")
            print()
            resultado_uno=str(input("Por favor ingrese su respuesta: ").upper())
            resultado_str(resultado_uno,"C")
            continue
        elif seleccion == "2":
            print()
            #Se desarrolla la segunda pregunta modelo PISA usando archivos, condiciones y funciones
            imprimir_archivo("ejercicio2")
            print()
            resultado_dos=str(input("Por favor ingrese su respuesta: ").upper())
            resultado_str(resultado_dos,"B")
            continue
        elif seleccion == "3":
            print()
            #Se desarrolla la tercera pregunta modelo PISA usando archivos, condiciones y funciones
            imprimir_archivo("ejercicio3")
            print()
            #Se capitaliza y evalúa con la funcion previamente establecida
            inp_capitalize_str("Los dos estudiantes son chicas (Si/No): ")
            inp_capitalize_str("\nUno de los estudiantes es un chico y el otro es una chica (Si/No): ")
            inp_capitalize_str("\nLos dos estudiantes tienen la misma estatura (Si/No): ")
            inp_capitalize_str("\nLa estatura media de todos los estudiantes no cambió (Si/No): ")
            inp_capitalize_str("\nPedro sigue siendo el más bajo (Si/No): ")
            continue
        elif seleccion == "4":
            print()
            #Se desarrolla la cuarta pregunta modelo PISA usando archivos, condiciones y funciones
            imprimir_archivo("ejercicio4")
            print()
            resultado_cuatro=str(input("¿Cuántas combinaciones diferentes podría seleccionar Jaime?: "))
            resultado_str(resultado_cuatro,6)
            continue
        elif seleccion == "5":
            print()
            #Se desarrolla la quinta pregunta modelo PISA usando archivos, condiciones y funciones
            imprimir_archivo("ejercicio5")
            print()
            resultado_cinco=str(input("¿Cuantos ladrillos necesita Nicolás?: "))
            resultado_str(resultado_cinco,1276)
            continue
        elif seleccion == "0":
            #Se rompe el ciclo del menu y el usuario sale de él
            break
        else:
            #En caso de que el usuario tenga errores de digitacion, el ciclo se repite
            print("La opción no es valida, intentelo de nuevo: \n\n")
            continue
           
# Miranda
def problemas_geometria():  # Función que contiene todos los problemas de practica del tema de geometría.
    b = random.randint(1, 100)  # Ingreso de las variables que se utilizarán en el programa.
    h = random.randint(1, 100)
    ejercicio = 'Cual es el area de un triangulo cuya base es: ' + str(b) + ' cm y su altura es: ' + str(h) + 'cm?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = (b * h) / 2
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 2
    ejercicio = 'Si un triangulo es equilatero cuanto mide cada uno de sus angulos?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = 180 / 3
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 3
    a = random.randint(1, 180)  # a = valor del ángulo.
    ejercicio = 'Cual es el angulo suplementario de ' + str(a) + '?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = 180 - a
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 4
    lado = random.randint(1, 100)  # medida del lado del cuadrado.
    ejercicio = 'Cual es el perimetro de un cuadrado cuyos lados miden: ' + str(lado) + ' cm.'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = lado * 4
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 5
    base_base = random.randint(1, 1000)  # medida de la base del rectangulo en la base.
    altura_base = random.randint(1, 100)  # medida de la altura del rectangulo en la base.
    altura_prisma = random.randint(1, 100)  # medida de la altura del prisma.
    ejercicio = 'Cual es el volumen de un prisma rectangular con las siguientes medidas? Base =  ' + str(
        base_base) + ' m. Altura de la base= ' + str(altura_base) + ' m. Altura del prisma = ' + str(
        altura_prisma) + ' m.'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = (base_base * altura_base) * altura_prisma
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    regresar()
    problemas_geometria()


def problemas_aritmetica():  # Función que contiene todos los problemas de practica del tema de aritmética.
    # 1
    a = random.randint(1, 1000)  # a= porcentaje que se extraerá del valor p.
    p = random.randint(1, 100)  # p= cantidad total de la cual se extraerá un porcentaje.
    ejercicio = 'Cuanto es el ' + str(p) + '% de ' + str(a) + ' ?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = (a * p) / 100
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 2
    b = random.randint(1, 1000)  # Cantidad de lapices que se compraron.
    c = random.randint(1, 100)  # Cuanto cuesta cada lápiz.
    ejercicio = 'Una persona compró ' + str(b) + ' lápices que cuestan ' + str(c) + ' pesos cada uno. ¿Cuánto pagó?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = (b * c)
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 3
    a = random.randint(1, 1000)  # a y b = valores que serán sumados.
    b = random.randint(1, 1000)
    r = random.randint(1, 1000)  # número que se restará del total.
    ejercicio = 'Réstale ' + str(r) + ' a la suma de: ' + str(a) + ' y ' + str(b) + '?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = (a + b) - r
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 4
    a = random.randint(1, 100)  # Cantidad de blusas compradas.
    d = random.randint(100, 1000)  # Dinero pagado.
    ejercicio = 'Una niña gastó ' + str(d) + ' en la compra de: ' + str(a) + ' blusas. ¿Cuánto le costó cada blusa?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round(d / a)
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 5
    valor = random.randint(1, 1000)  # Valor inicial.
    dif = random.randint(1, 100)  # Diferencia entre la cada valor en la sucesión.
    lista = [valor, valor + dif, valor + (2 * dif), valor + (3 * dif), valor + (4 * dif), valor + (5 * dif)]
    ejercicio = 'Cual es la diferencia entre los valores de la siguiente lista? ', lista
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = dif
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    regresar()
    problemas_aritmetica()


def problemas_algebra_y_estadistica():  # Función que contiene todos los problemas de practica del tema de algebra y
    # estadística.
    # 1
    y = random.randint(1, 1000)  # Número que se sumará a x.
    z = random.randint(1, 1000)  # Total de x + y .
    ejercicio = 'x + ' + str(y) + ' = ' + str(z) + '. ¿Cuál es el valor de x? '
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = z - y
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 2
    d = random.randint(1, 1000)  # Valor que se restará de x.
    e = random.randint(1, 100)  # Diferencia entre x y y.
    ejercicio = 'x - ' + str(d) + ' = ' + str(e) + '. ¿Cuál es el valor de x? '
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = d + e
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 3
    negativo = random.randint(-100, -1)  # Valor negativo del ejercicio.
    positivo = random.randint(1, 100)  # Valor positivo del ejercicio.
    ejercicio = '¿Cuál es el producto de ' + str(negativo) + ' por ' + str(positivo) + '?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = negativo * positivo
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 4
    a = random.randint(100, 1000)  # coeficiente.
    d = random.randint(1, 100)  # exponente 1.
    e = random.randint(1, 100)  # exponente 2.
    ejercicio = '¿Cuál será el exponente resultante de (' + str(a) + '^' + str(d) + ') ^' + str(e) + '?'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = d * e
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 5
    lista = []
    suma = 0
    for i in range(10):
        a = random.randint(1, 10)
        lista.append(a)
        suma += a
    ejercicio = '¿Cuál es la media de la siguiente lista? ', lista
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = suma / len(lista)
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    regresar()
    problemas_algebra_y_estadistica()


def problemas_probabilidad():  # Función que contiene todos los problemas de practica del tema de probabilidad.
    # 1
    f = random.randint(1, 1000)  # Cantidad de pelotas rojas en una bolsa.
    g = random.randint(1, 1000)  # Cantidad de pelotas rosas en una bolsa.
    h = f + g  # Cantidad total de pelotas.
    ejercicio = 'En una caja hay ' + str(h) + ' pelotas, hay ' + str(f) + ' de color rojo y ' + str(
        g) + ' de color rosa. ¿Cuál es la probabilidad de que sacando una al azar salga una pelota rosa?(en %)'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round((g / h) * 100)
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 2
    j = random.randint(1, 6)  # El valor que se busca que salga en los dados.
    ejercicio = 'Si lanzo un dado de 6 caras. ¿Cuál es la probabilidad de que me salga el numero: ' + str(
        j) + '? (en %) '
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round((1 / 6) * 100)
    if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 3

    ejercicio = '¿Cuál es la probabilidad de obtener 2 caras y 1 sol si lanzas 3 monedas. (en %) '
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round(((1 / 2) ** 3) * 100)
    if int(respuesta) == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
        print('Es correcto! Felicidades!')
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 4
    a = random.randint(1, 10)  # cantidad de divisiones moradas en la ruleta.
    b = random.randint(1, 10)  # cantidad de divisiones amarillas en la ruleta.
    d = random.randint(1, 10)  # cantidad de divisiones azules en la ruleta.
    total = a + b + d  # total de divisiones en la ruleta.
    ejercicio = 'Si giro una ruleta de ' + str(total) + ' divisiones: ' + str(a) + ' moradas,  ' + str(
        b) + ' amarillas y ' + str(
        d) + ' azules. ¿Cuál es la probabilidad de que al girar la ruleta caiga en una casilla morada.? (en %)'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round((a / total) * 100)
    if int(respuesta) == respuestacorrecta:
        print('Es correcto! Felicidades!')  # Revisa si la respuesta ingresada es correcta.
    else:
        print('No es correcto. Intenta otra vez')
        intentos(ejercicio, respuesta, respuestacorrecta)
    # 5
    primaria = random.randint(1, 1000)  # cantidad de alumnos de primaria.
    secundaria = random.randint(1, 1000)  # cantidad de alumnos en secundaria.
    ejercicio = 'En una escuela hay  ' + str(primaria) + ' alumnos de primaria y ' + str(
        secundaria) + ' alumnos de secundaria. ¿Si se elige uno al azar' \
                      ', cuál es la probabilidad de que sea de secundaria? (en %)'
    print(ejercicio)
    respuesta = float(input())
    respuestacorrecta = round((secundaria / (primaria + secundaria)) * 100)

    problemas_probabilidad()


def intentos(ejercicio, respuesta,
             respuestacorrecta):  # Función diseñada para que los alumnos puedan seguir intentando los problemas en
    # los cuales se equivocaron.
    if respuesta != respuestacorrecta:  # Revisa si la respuesta ingresada es incorrecta.
        print(ejercicio)
        respuesta = float(input())
        if respuesta == respuestacorrecta:  # Revisa si la respuesta ingresada es correcta.
            print('Es correcto! Felicidades!')
            seguir = input("Si quieres continuar solo presiona Enter, si deseas volver al menu presiona(1)")
            if seguir == '1':
                regresar()
        else:
            print('No es correcto. Intenta otra vez')
            seguir = input('Quieres seguir intentando?, "si" para continuar, "no" para volver al menu o presiona '
                           'Enter para pasar al siguiente ejercicio.')
            if seguir == 'si':  # Revisa si el alumno quiere seguir practicando el mismo ejercicio.
                intentos(ejercicio, respuesta, respuestacorrecta)
            elif seguir == "no":
                print(' La respuesta correcta era: ', respuestacorrecta)
                regresar()
            elif seguir != "si" and seguir != "no":
                print(' La respuesta correcta era: ', respuestacorrecta)


def modulo_matematicas():  # menú principal del modulo de ejercicios de matemáticas.
    temas = ['Geometría', 'Aritmética', 'Algebra y Estadística', 'Probabilidad']
    print('Que tema quieres practicar? Puedes escoger entre:', temas)
    eleccion = input()
    if eleccion is not None:
        if eleccion == 'geometria':
            problemas_geometria()
        elif eleccion == 'aritmetica':
            problemas_aritmetica()
        elif eleccion == 'algebra y estadística' or eleccion == 'algebra' or eleccion == 'estadistica':
            problemas_algebra_y_estadistica()
        elif eleccion == 'probabilidad':
            problemas_probabilidad()
        elif eleccion == 'ninguno':
            print(
                """Ok, muy buen trabajo. Ahora puedes escoger alguno de nuestros juegos 
                para reforzar lo que aprendiste aqui!!""")
            main()
        else:
            while eleccion != 'geometria' and eleccion != 'aritmetica' and eleccion != 'algebra y estadistica' \
                    and eleccion != 'algebra' and eleccion != 'estadistica' and eleccion != 'probabilidad':
                print('No tenemos problemas de este tema. Favor de volver a intentar. ')
                modulo_matematicas()

            # Ariana


def ensenar_tablero(
        juego):  # Enseña el tablero principal cada vez que el jugador tira, enseñando la jugada del participante y
    # computadora.
    print("TABLERO")
    print("  1 2 3")
    for renglon in range(len(juego)):
        print(renglon + 1, end=" ")
        for columna in range(len(juego[renglon])):
            print(juego[renglon][columna], end=" ")
        print()


def lugar_valido(x, y, juego):  # Mantiene las respuestas de la computadora y pasticipante dentro de 0 y 2.
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    if juego[x][y] == ".":
        return True
    else:
        return False


def turno_humano(juego):  # Es la jugado del participante donde elige su posicion.
    print("-------------------------------")
    print("Es tu turno, elige una posicion")
    valido = False
    while not valido:
        x = int(input("Renglon: ")) - 1
        y = int(input("Columna: ")) - 1
        valido = lugar_valido(x, y, juego)
        if valido:
            juego[x][y] = "X"
        else:
            print("Esa posicion no es valida. Intentalo de nuevo.")


def turno_compu(juego):  # Es la jugada de la computadora y elige su posicion.
    print("-------------------------------")
    print("Turno de la computadora")
    valido = False
    while not valido:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        valido = lugar_valido(x, y, juego)
        if valido:
            juego[x][y] = "O"

    ensenar_tablero(juego)


def gano_letra(letra, juego):  # Checar si en el tablero algun participante ha ganado por su jugada.
    # Checar si hay un renglon donde gano
    for renglon in juego:
        gano = True
        for columna in renglon:
            if columna != letra:
                gano = False
        if gano:
            return True

    # checar columnas si se gano
    for columna in range(0, 3):
        gano = True
        for renglon in range(0, 3):
            if juego[renglon][columna] != letra:
                gano = False
        if gano:
            return True

    # checar diagonales si se gano
    # diagonal hacia abajo
    if juego[0][0] == letra and juego[1][1] == letra and juego[2][2] == letra:
        return True
    # diagonal haccia arriba
    if juego[0][2] == letra and juego[1][1] == letra and juego[2][0] == letra:
        return True
    # Los returns muestran si la accion fue correcta o incorrecta.

    return False


def juego_lleno(juego):  # checar si en algun espacio esta vacio
    for renglon in juego:
        for columna in renglon:
            if columna == ".":
                return False
    return True


def checar_estado(juego):  # Checar que jugador gano
    if gano_letra("X", juego):
        return 1
    elif gano_letra("O", juego):
        return 2
    elif juego_lleno(juego):
        return 3
    else:
        return 0


def gato():  # el main del gato donde se utiliza las funciones y se realiza todo el juego
    quiere_jugar = input("Quieres jugar al gato? ")
    while quiere_jugar != "no" and quiere_jugar != "si":
        quiere_jugar = input("Vuelve a responsder con Si o no.\n¿Quieres jugar al gato?")
    if quiere_jugar == "no":
        main()
    while quiere_jugar.lower() == "si":
        juego = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]
        ]
        turno = 0
        estado = 0  # 0 jugando, #1 gano humano, #2 gano compu, #3 empate

        ensenar_tablero(juego)
        while estado == 0:
            # jugando el juego

            if turno % 2 == 0:
                turno_humano(juego)
            else:
                turno_compu(juego)
            estado = checar_estado(juego)
            turno = turno + 1

        print("---------------")

        if estado == 1:
            print("GANASTE")
        elif estado == 2:
            print("Perdiste, gano la compu :(")
        else:
            print("Fue un empate.")
        ensenar_tablero(juego)
        print("--------------------------")
        quiere_jugar = input("Quieres volver a jugar? ")
        while quiere_jugar != "no" and quiere_jugar != "si":
            quiere_jugar = input("Vuelve a responsder con Si o no.\n¿Quieres jugar a los acertijos?")
    if quiere_jugar == "no":  # Regresar al menu
        main()


def aleatorios_acer(acertijos):  # Funcion para mostrar los acertijos aleatorios y observar las respuestas
    print("----------------------------")
    respuestas_correctas = 0
    respuestas_incorrectas = 0
    random.shuffle(acertijos)  # acetijos aleatorios
    for acertijo in acertijos:
        print(acertijo[0])  # acertijo
        pista = input("¿Quieres una pista?")  # dar las pistas
        while pista != "si" and pista != "no":
            pista = input("Responde de nuevo. Si o no")
        if pista.lower() == "si":
            print(acertijo[2])
        else:
            print("Esta bien. Continua")
        r = input("Respuesta: ")
        if r.lower() == acertijo[1]:  # Checar si la respuesta esta bien o no
            print("Correcto")
            respuestas_correctas += 1
        else:
            print("incorrecto")
            print("Respuesta correcta es ", acertijo[1])
            respuestas_incorrectas += 1
        print("--------------------------")
    print("Respuestas correctas= ",
          respuestas_correctas)  # Mostrar las respuestas correctass e incorecctas al participante
    print("Respuestas incorrectas=", respuestas_incorrectas)
    print("______________________________")
    if respuestas_correctas == 6:
        print("Excelente, lo lograste, sigue adelante")
    elif respuestas_correctas > respuestas_incorrectas:
        print("Muy bien, Sacaste la mayoria correctas")
    else:
        print("Mejora para la proxima, Amig@")


def losacertijos_juego():  # Es el main del juego donde se ejecuta el codigo
    quiere_jugar = input("Quieres jugar a los Acertijos? ")
    while quiere_jugar != "no" and quiere_jugar != "si":
        quiere_jugar = input("Vuelve a responsder con Si o no.\n¿Quieres jugar a los acertijos?")
    if quiere_jugar == "no":
        main()
    while quiere_jugar.lower() == "si":
        acertijos = [
            ["Cuatro gatos en un cuarto, cada gato en un rincón, cada gato ve tres gatos, adivina cuántos gatos son.",
             "cuatro gatos", "c_ua_ _ _ g_ _ _s"],
            ["Hay 2 padres y 2 hijos, pero solo hay 3 personas ¿Cómo es? ", "el abuelo, el padre y el hijo",
             "¿Qué relación de parentesco tienen estas personas?"],
            ["Tengo mas de 3 lados y menos de 5 lados. Tengo todos mis lados iguales. ¿quien soy?", "cuadrado",
             "c_ _d_ _"],
            ["No soy triangular, no soy rectangular, no soy el cuadrado. Mi lado es una línea curva. ¿quien soy?",
             "circulo", "_i_ _l_"],
            [
                "Son las doce de la mañana, hora de mis pastillas. Me tengo que tomar 4 pastillas, una cada hora. ¿A "
                "qué hora me tomaré la última?",
                "a las 3 de la tarde", "_ _a_ d_ _a _a_d_"],
            [
                "Si 5 máquinas hacen 5 artículos en 5 minutos, ¿cuánto tiempo dedicarán 100 máquinas en hacer 100 "
                "artículos?",
                "5 minutos", "Son minutos y observa bien la situación"]

        ]
        print(
            "Bienvenido al juego de los ACERTIJOS\nLee con cuidado, piensa y razonalo. Pon la respuesta que más te "
            "parezca correcta")

        # jugando a los acetijos
        aleatorios_acer(acertijos)
        print("--------------------------")
        quiere_jugar = input("Quieres volver a jugar? ")
        while quiere_jugar != "no" and quiere_jugar != "si":
            quiere_jugar = input("Vuelve a responsder con Si o no.\n¿Quieres jugar a los acertijos?")
    if quiere_jugar.lower == "no":  # Regresar al menu
        main()


# Jorge + Unir todo el programa
def minijuegos():
    # Le pide al usuario que seleccione un minijuego
    choise = int(input("""Bienvenido a la seccion de minijuegos que juego deseas jugar?
  (Debes ingresar el numero en () para seleccionar tu opcion) Gato(1) o Acertijos(2)"""))
    # Escoge entre gato o acertijos
    if choise == 1:
        gato()
    if choise == 2:
        losacertijos_juego()
    # Regresa un mensaje de error y lo manda al menu
    else:
        print("Lo siento, no he podido entenderte, ingresa la opcion en el formato solicitado, te regresare al menu")
        main()


def main():
    # es el menu principal donde se selecciona cada juego mediante un if
    # y este los manda a la funcion de cada modulo
    menu = int(input(""" Bienvenido al programa de preparacion PISA
    Selecciona que ejercicios deseas realizar(Debes ingresar el numero en () para seleccionar tu opcion): 
    ejercicios estilo libro PISA (1), Modulo de matematicas por secciones(2),
    por ultimo el modulo de los minijuegos(3) y por ultimo si deseas salir del programa(4) """))
    if menu == 1:
        ejercicios_PISA()
    elif menu == 2:
        modulo_matematicas()
    elif menu == 3:
        minijuegos()
    elif menu == 4:
        exit()
    else:
        # en caso de error manda un mensaje y vuelve a lanzar la funcion menu
        print("Lo siento, no he podido entenderte, ingresa la opcion en el formato solicitado, te regresare al menu")
        main()


main()
