
def escribir_agenda(nombre_agenda, agenda_digital):
    """escribe la agenda en un fichero de texto

    parametros posicionales
    nombre_agenda -- str que representa el nombre de la agenda en disco
    agenda_digital -- dict que representa la agenda digital y los contactos
    """
    agenda_fichero = open(nombre_agenda, "w", encoding="utf-8")
    # Esta sentencia escribe el diccionario en el fichero


    agenda_fichero.write(str(agenda_digital))
    # Esta sentencia cierra el fichero que has abierto con la funcion open()
    agenda_fichero.close()


def crear_contacto(agenda_digital, nuevo_contacto):
    """introduce un nuevo contacto en la agenda digital
       parámetros posicionales
       agenda_digital -- dict que represental la agenda  digital
        nuevo_contacto -- dict que represental el contacto nuevo
       """
    agenda_digital[nuevo_contacto["nombre"]] = {
        "direccion": nuevo_contacto["direccion"],
        "email": nuevo_contacto["email"],
        "telefono": nuevo_contacto["telefono"]
    }
    return agenda_digital
def leer_agenda(nombre_agenda):
    """Leer la agenda digital de un fichero en disco
    parámetros pósicionales
    nombre_agenda -- str que represental el nombre de la agenda en disco
    """
    agenda_digital_lectura = open(nombre_agenda, "r")
    # Esta sentencia lee todas las líneas del fichero y las asigna a la variable agenda_digital
    agenda_digital = agenda_digital_lectura.readlines()

    # Esta sentencia cierra el fichero que has abierto con la función open()
    agenda_digital_lectura.close()
    return eval(agenda_digital[0])

def solicitar_contacto_agenda():
    """Esta funcion solicita los datos de un nuevo contacto"""
    nombre = input("Introduce el nombre completo del contacto: ")
    direccion = input("Introduce la direccion del contacto: ")
    email = input("Introduce el email del contacto: ")
    telefono = input("Introduce el telefono del contacto: ")
    # construir un diccionario con los valores recibidos
    contacto ={
        "nombre": nombre,
        "direccion": direccion,
        "email": email,
        "telefono": telefono
    }
    return contacto

def consultar_contacto_agenda(agenda_digital):
    """esta funcion consulta un contacto en la agenda"""
    nombre = input("Introduce en nombre completo del contacto: ")
    print("\n[+]", nombre)
    print("\tDireccion:", agenda_digital[nombre]["direccion"])
    print("\tEmail:", agenda_digital[nombre]["email"])
    print("\tTelefono:", agenda_digital[nombre]["telefono"])

#agenda_digital = {}
#escribir_agenda("agenda_digital", agenda_digital)

#agenda_digital = leer_agenda("agenda_digital")
#nuevo_contacto = solicitar_contacto_agenda()
#agenda_digital = crear_contacto(agenda_digital, nuevo_contacto)
#escribir_agenda("agenda_digital", agenda_digital)

agenda_digital = leer_agenda("agenda_digital")
consultar_contacto_agenda(agenda_digital)