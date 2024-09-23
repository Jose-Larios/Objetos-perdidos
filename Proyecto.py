#Codigo completo.py

import sqlite3

#Creando funcion para crear la conexion
def conectar():
    conexion = sqlite3.connect("TeEncontre.db")
    return conexion

#Creacion de la tabla 
def crear_tabla_ObjetosPerdidos(conexion):
    cursor = conexion.cursor()
    sentencia = '''
    CREATE TABLE IF NOT EXISTS ObjetosPerdidos(
        No INTEGER PRIMARY KEY, 
        NombreObjeto TEXT NOT NULL, 
        Descripcion TEXT NOT NULL, 
        LugarEncontrado TEXT NOT NULL, 
        Telefono1 INTEGER NOT NULL,
        Telefono2 INTEGER NOT NULL
    )'''
    cursor.execute(sentencia)
    conexion.commit()

#Creacion de la tabla 
def crear_tabla_ObjetosEncontrados(conexion):
    cursor = conexion.cursor()
    sentencia = '''
    CREATE TABLE IF NOT EXISTS ObjetosEncontrados(
        No INTEGER PRIMARY KEY, 
        NombreObjeto TEXT NOT NULL, 
        Descripcion TEXT NOT NULL, 
        LugarEncontrado TEXT NOT NULL, 
        PersonaEntregado TEXT NOT NULL,
        Telefono INTEGER NOT NULL
    )'''
    cursor.execute(sentencia)
    conexion.commit()

#Insertar objeto
def insertar_Objeto(conexion, NombreObjeto, Descripcion, LugarEncontrado, Telefono1, Telefono2):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ObjetosPerdidos( NombreObjeto, Descripcion, LugarEncontrado, Telefono1, Telefono2) VALUES (?,?,?,?,?)",
                       ( NombreObjeto, Descripcion, LugarEncontrado, Telefono1, Telefono2))
        conexion.commit()
        print("Se ha insertado correctamente")
   
    except sqlite3.OperationalError:
        print("Error inesperado")

#Insertar objeto encontrado
def insertar_ObjetoEncontrado(conexion, NombreObjeto, Descripcion, LugarEncontrado, PersonaEntregado, Telefono):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ObjetosEncontrados( NombreObjeto, Descripcion, LugarEncontrado, PersonaEntregado, Telefono) VALUES (?,?,?,?,?)",
                       ( NombreObjeto, Descripcion, LugarEncontrado, PersonaEntregado, Telefono))
        conexion.commit()
        print("Se ha insertado correctamente")
   
    except sqlite3.OperationalError:
        print("Error inesperado")

#Mostar objetos
def mostrar_objetos(conexion):
    try:
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM ObjetosPerdidos"
        cursor.execute(sentencia)
        objetos = cursor.fetchall()
        
        #Creando encabezados
        print("*"*175)
        print("="*175)
        print(f"|{'No':3}|{'NombreObjeto':^40}|{' Descripcion':^40}|{'LugarEncontrado':^18}|{'Telefono1':^13}|{'Telefono2':^13}|" )
        print("-"*175)
        
        for objeto in objetos:
            No, NombreObjeto, Descripcion, LugarEncontrado, Telefono1, Telefono2 = objeto
            print(f"|{No:3}|{NombreObjeto:^40}|{Descripcion:^40}|{LugarEncontrado:^18}|{Telefono1:^13}|{Telefono2:^13}|" )

        print("-" * 175)
        #Alineaciones: ^ Centrada, >Izquierda, <Derecha
  
    except sqlite3.OperationalError:
        print("Error inesperado")

#Mostar objetos encontrados
def mostrar_objetosEncontrados(conexion):
    try:
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM ObjetosEncontrados"
        cursor.execute(sentencia)
        objetos = cursor.fetchall()
        
        #Creando encabezados
        print("*"*175)
        print("="*175)
        print(f"|{'No':3}|{'NombreObjeto':^40}|{' Descripcion':^40}|{'LugarEncontrado':^25}|{'PersonaEntregado':^25}|{'Telefono':^13}|" )
        print("-"*175)
        
        for objeto in objetos:
            No, NombreObjeto, Descripcion, LugarEncontrado, PersonaEntregado, Telefono = objeto
            print(f"|{No:3}|{NombreObjeto:^40}|{Descripcion:^40}|{LugarEncontrado:^25}|{PersonaEntregado:^25}|{Telefono:^13}|" )

        print("-" * 175)
        #Alineaciones: ^ Centrada, >Izquierda, <Derecha
  
    except sqlite3.OperationalError:
        print("Error inesperado")

#Podremos buscar entre Objeto perdido y lugar donde se econtro
def buscar_objeto(conexion, termino):
    try:
        cursor = conexion.cursor()
        sentencia = "SELECT * FROM ObjetosPerdidos WHERE NombreObjeto LIKE ? or LugarEncontrado LIKE ?"
        cursor.execute(sentencia,[f"%{termino}%", f"%{termino}%"])

        objetos = cursor.fetchall()

        #Creando encabezados
        print("*"*175)
        print("="*175)
        print(f"|{'No':3}|{'NombreObjeto':^40}|{' Descripcion':^40}|{'LugarEncontrado':^18}|{'Telefono1':^13}|{'Telefono2':^13}|" )
        print("-"*175)
        
        for objeto in objetos:
            No, NombreObjeto, Descripcion, LugarEncontrado, Telefono1, Telefono2 = objeto
            print(f"|{No:3}|{NombreObjeto:^40}|{Descripcion:^40}|{LugarEncontrado:^18}|{Telefono1:^13}|{Telefono2:^13}|" )

        print("-" * 175)

    except sqlite3.OperationalError:
        print("Error inesperado")

#Eliminacion de un objeto perdido
def eliminar_objeto(conexion, No_objeto):
    try:
        cursor = conexion.cursor()
        sentencia = "DELETE FROM ObjetosPerdidos WHERE No = ?"
        cursor.execute(sentencia, [No_objeto])

        print("Eliminacion exitosa")
        conexion.commit()

    except sqlite3.OperationalError:
        print("Error inesperado")

#Eliminacion de un objeto encontrado
def eliminar_objetoEncontrado(conexion, No_objeto):
    try:
        cursor = conexion.cursor()
        sentencia = "DELETE FROM ObjetosEncontrados WHERE No = ?"
        cursor.execute(sentencia, [No_objeto])

        print("Eliminacion exitosa")
        conexion.commit()

    except sqlite3.OperationalError:
        print("Error inesperado")

#Crear funcion principal1
        
def main():
    conexion = conectar() #Realizar la conexion con BD (TeEncontre)
    crear_tabla_ObjetosPerdidos(conexion) #Realizando la conecion con la tabla ("ObjetosPerdidos")
    crear_tabla_ObjetosEncontrados(conexion) #Realizando la conecion con la tabla ("ObjetosEncontrados")

    while True:
        print("*" * 60)
        print("Base de datos de Te encontre")
        print("*" * 60)

        print("\nOpciones")
        print("1. Insertar objeto perdido")
        print("2. Insertar objeto encontrado")
        print("3. Mostrar objeto perdidos ")
        print("4. Mostrar objetos encontrados")
        print("5. Buscar objeto perdido")
        print("6. Borrar objeto perdido")
        print("7. Borrar objeto encontrado")
        print("8. Salir")

        opcion = (input("Selecione una opcion: "))

        if opcion == "1":
            print("Insertar objeto")
            nombre_objeto = input("Nombre del objeto: ")
            descripcion = input("Descricion del objeto: ")
            lugar_encontrado = input("Lugar donde se econtro: ")
            telefono1 = int(input("Telefono de contacto 1: "))
            telefono2 = int(input("Telefono de contacto 2: "))
            insertar_Objeto(conexion, nombre_objeto, descripcion, lugar_encontrado, telefono1, telefono2)

        elif opcion == "2":
            print("Insertar objeto encontrado")
            nombre_objeto = input("Nombre del objeto: ")
            descripcion = input("Descricion del objeto: ")
            lugar_encontrado = input("Lugar donde se econtro: ")
            persona_entregado = input("Persona a quien se le entrego: ")
            telefono = int(input("Telefono de la persona a la que se le entrego: "))
            insertar_ObjetoEncontrado(conexion, nombre_objeto, descripcion, lugar_encontrado, persona_entregado, telefono)

        elif opcion == "3":
            print("Mostrar objetos perdidos")
            mostrar_objetos(conexion)

        elif opcion == "4":
            print("Mostrar objetos encontrados")
            mostrar_objetosEncontrados(conexion)

        elif opcion == "5":
            print("Buscar objeto")
            termino = input("Termino de busqueda (Nombre del objeto o lugar donde se perdio): ")
            buscar_objeto(conexion, termino)

        elif opcion == "6":
            No_objeto = int(input("No del objeto a eliminar: "))
            eliminar_objeto(conexion, No_objeto)

        elif opcion == "7":
            No_objeto = int(input("No del objeto a eliminar: "))
            eliminar_objetoEncontrado(conexion, No_objeto)

        elif opcion == "8":
            print("Cerrando programa")
            break

        else:
            print("Opcion no valida, Intente de nuevo")

    conexion.close()

main()