##########################################################
# Actividad de cierre unidad 3 - Estructuras Repetitivas #
##########################################################
# Ejercicio 1 #
###############

nombre = input("Ingrese el nombre del cliente: ")
productos_a_comprar = input("Ingrese la cantidad de productos a comprar: ")

while not nombre.isalpha():
    nombre = input("Ingrese un nombre válido: ")

while not productos_a_comprar.isdigit() or int(productos_a_comprar) <= 0:
    productos_a_comprar = input("Ingrese una cantidad válida de productos: ")

total_sin_descuento = 0
total_acumulado = 0
listado_productos = ""

for i in range(1, int(productos_a_comprar) + 1):
    precio = input(f"Ingrese el precio del producto {i}: ")
    while not precio.isdigit():
        precio = input(f"Ingrese un precio válido para el producto {i}: ")
    
    descuento = input(f"¿El producto {i} tiene descuento? (s/n): ").lower()
    while descuento not in ['s', 'n']:
        descuento = input(f"Respuesta inválida. ¿El producto {i} tiene descuento? (s/n): ").lower()
    
    if descuento == 's':
        precio_final = float(precio) * 0.9
    else:
        precio_final = float(precio)
    
    total_sin_descuento += float(precio)
    total_acumulado += precio_final
    listado_productos += f"Producto {i} - Precio: ${precio} Descuento (S/N): {descuento}\n"

total_con_descuento = total_acumulado
total_sin_descuento = total_sin_descuento
total_ahorrado = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / int(productos_a_comprar)

print(f"Cliente: {nombre}")
print(f"Productos a comprar: {productos_a_comprar}")
print(listado_productos)
print(f"Total sin descuento: ${total_sin_descuento:.2f}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro: ${total_ahorrado:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

###############
# Ejercicio 2 #
###############

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos_maximos = 3
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    print(f"{intentos_realizados + 1}/{intentos_maximos} - Usuario: {usuario_ingresado} \n Clave: {clave_ingresada}")
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos_realizados += 1
        print("Credenciales incorrectas.")
if intentos_realizados == intentos_maximos:
    print("Cuenta bloqueada.")
if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
    print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
opcion = ""
while opcion != "4":
    opcion = input("Opción: ")
    if not opcion.isdigit():
        print("Ingrese un número válido.")
        continue
    if opcion == "1":
        print("Inscripto")
    elif opcion == "2":
        nueva_clave = input("Ingrese la nueva clave: ")
        confirmar_clave = input("Confirme la nueva clave: ")
        if nueva_clave == confirmar_clave and len(nueva_clave) >= 6:
            print("Clave actualizada con éxito.")
        else:
            print("La clave debe tener al menos 6 caracteres.")
            continue
    elif opcion == "3":
        print("El miedo es una ilusion, desaparece cuando avanzas.")
    elif opcion == "4":
        break
    else:
        print("Opción fuera del rango.")

###############
# Ejercicio 3 #
###############

lunes1 = "libre"
lunes2 = "libre"
lunes3 = "libre"
lunes4 = "libre"
turnos_ocupados_lunes = 0
martes1 = "libre"
martes2 = "libre"
martes3 = "libre"
turnos_ocupados_martes = 0

nombre_operador = input("Ingrese el nombre del operador: ")

while nombre_operador.isalpha():
    print("1) Reservar turno 2) Cancelar turno 3) Ver agenda del día 4) Ver resumen general 5) Cerrar sistema")
    opcion = input("Seleccione una opción: ")
    if not opcion.isdigit():
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        continue

    if opcion == "1":
        print("Elegir día (1=Lunes 2=Martes).")
        dia = input("Ingrese el número del día: ")
        if not dia.isdigit():
            print("Día no válido. Por favor, ingrese un número (1 o 2).")
            continue
        nombre_paciente = input("Ingrese el nombre del paciente: ")

        if dia == "1":
            if lunes1 == "libre":
                lunes1 = nombre_paciente
                print(f"Turno para {nombre_paciente} el lunes en el horario 1.")
                turnos_ocupados_lunes += 1
            elif lunes2 == "libre":
                lunes2 = nombre_paciente
                print(f"Turno para {nombre_paciente} el lunes en el horario 2.")
                turnos_ocupados_lunes += 1
            elif lunes3 == "libre":
                lunes3 = nombre_paciente
                print(f"Turno para {nombre_paciente} el lunes en el horario 3.")
                turnos_ocupados_lunes += 1
            elif lunes4 == "libre":
                lunes4 = nombre_paciente
                print(f"Turno para {nombre_paciente} el lunes en el horario 4.")
                turnos_ocupados_lunes += 1
            else:
                print("No hay turnos disponibles para el lunes.")
        
        elif dia == "2":
            if martes1 == "libre":
                martes1 = nombre_paciente
                print(f"Turno para {nombre_paciente} el martes en el horario 1.")
                turnos_ocupados_martes += 1
            elif martes2 == "libre":
                martes2 = nombre_paciente
                print(f"Turno para {nombre_paciente} el martes en el horario 2.")
                turnos_ocupados_martes += 1
            elif martes3 == "libre":
                martes3 = nombre_paciente
                print(f"Turno para {nombre_paciente} el martes en el horario 3.")
                turnos_ocupados_martes += 1
            else:
                print("No hay turnos disponibles para el martes.")
        else:
            print("Día inválido. Por favor, ingrese un número válido (1 o 2).")

    elif opcion == "2":
        print("Elegir día (1=Lunes 2=Martes).")
        dia = input("Ingrese el número del día: ")
        nombre_paciente = input("Ingrese el nombre del paciente: ")

        if dia == "1":
            if lunes1 == nombre_paciente:
                lunes1 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 1.")
                turnos_ocupados_lunes -= 1
            elif lunes2 == nombre_paciente:
                lunes2 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 2.")
                turnos_ocupados_lunes -= 1
            elif lunes3 == nombre_paciente:
                lunes3 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 3.")
                turnos_ocupados_lunes -= 1
            elif lunes4 == nombre_paciente:
                lunes4 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el lunes en el horario 4.")
                turnos_ocupados_lunes -= 1
            else:
                print("No se encontró un turno reservado para ese paciente el lunes.")

        elif dia == "2":
            if martes1 == nombre_paciente:
                martes1 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 1.")
                turnos_ocupados_martes -= 1
            elif martes2 == nombre_paciente:
                martes2 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 2.")
                turnos_ocupados_martes -= 1
            elif martes3 == nombre_paciente:
                martes3 = "libre"
                print(f"Turno cancelado para {nombre_paciente} el martes en el horario 3.")
                turnos_ocupados_martes -= 1
            else:
                print("No se encontró un turno reservado para ese paciente el martes.")
    elif opcion == "3":
        print("Agenda del día:")
        print(f"Lunes: Horario 1: {lunes1}, Horario 2: {lunes2}, Horario 3: {lunes3}, Horario 4: {lunes4}")
        print(f"Martes: Horario 1: {martes1}, Horario 2: {martes2}, Horario 3: {martes3}")
    elif opcion == "4":
        print("Resumen general:")
        print(f"Turnos ocupados el lunes: {turnos_ocupados_lunes}")
        print(f"Turnos ocupados el martes: {turnos_ocupados_martes}")
        if turnos_ocupados_lunes > turnos_ocupados_martes:
            print("El día con más turnos ocupados es el lunes.")
        elif turnos_ocupados_lunes < turnos_ocupados_martes:
            print("El día con más turnos ocupados es el martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")
    elif opcion == "5":
        print("Cerrando sistema.")
        break

###############
# Ejercicio 4 #
###############

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
bloqueado = False
codigo_parcial = ""
conteo_forzar = 0

while True:
    nombre_agente = input("Ingrese el nombre del Agente: ")
    if nombre_agente.isalpha():
        break

print(f"Bienvenido, {nombre_agente}.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print(f"Energía: {energia}, Tiempo: {tiempo}, Cerraduras abiertas: {cerraduras_abiertas}, Alarma: {alarma}")
    print("1) Forzar cerradura 2) Hackear panel 3) Descansar")

    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit():
        opcion = input("Entrada inválida. Ingrese 1, 2 o 3: ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        conteo_forzar += 1

        if conteo_forzar == 3:
            alarma = True
            print("Regla anti-spam activada: tercera forzada consecutiva -> la cerradura se trabó y se activa alarma.")
            break
        else:
            if energia < 40:
                riesgo = input("Energía baja, el riesgo de alarma es alto. Elija un número 1-3: ")
                while not riesgo.isdigit():
                    riesgo = input("Entrada inválida. Ingrese un número entre 1 y 3: ")

                if int(riesgo) == 3:
                    alarma = True
                    print("¡Elección 3! Alarma activada por riesgo de forzar con energía baja.")

            if not alarma:
                cerraduras_abiertas += 1
                print("Forzaste la cerradura con éxito.")
            else:
                print("No se abrió la cerradura debido a alarma.")

    elif opcion == "2":
        conteo_forzar = 0
        energia -= 10
        tiempo -= 3

        print("Comienza hackeo del panel:")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4: código parcial = {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Código compuesto. Se abrió una cerradura adicional automáticamente.")
        else:
            print("Hackeo terminado. No se abrió cerradura automáticamente aún.")

    elif opcion == "3":
        conteo_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activa: se pierde 10 energía extra por descanso.")

        print("Descansaste y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print("Sistema bloqueado por falta de tiempo. DERROTA.")
        break

    if cerraduras_abiertas >= 3:
        print("¡VICTORIA! Se abrieron las 3 cerraduras.")
        break
    if energia <= 0 or tiempo <= 0:
        print("DERROTA. Se acabó la energía o el tiempo.")
        break

if not bloqueado and cerraduras_abiertas < 3 and (energia > 0 and tiempo > 0):
    if cerraduras_abiertas >= 3:
        print("¡VICTORIA! Misíon completada.")
    else:
        print("Derrota.")

###############
# Ejercicio 5 #
###############

nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base_gladiador = 15
daño_base_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = ""
    while not opcion.isdigit():
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        elif int(opcion) not in [1, 2, 3]:
            print("Error: Opción no válida.")

    opcion = int(opcion)

    if opcion == 1:
        daño = daño_base_gladiador
        if vida_enemigo < 20:
            daño = daño_base_gladiador * 1.5
        vida_enemigo -= daño
        print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
    elif opcion == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print("¡Te has curado por 30 puntos!")
        else:
            print("¡No quedan pociones!")
        turno_gladiador = False

    if vida_enemigo <= 0:
        print(f">> ¡VICTORIA! {nombre} ha ganado la batalla. <<")
        break
    elif vida_gladiador <= 0:
        print(">> ¡DERROTA! Has caído en combate. <<")
        break
    else:
        vida_gladiador -= daño_base_enemigo
        print(f"¡El enemigo te ha golpeado por {daño_base_enemigo} puntos de daño!")
        if not turno_gladiador:
            turno_gladiador = True