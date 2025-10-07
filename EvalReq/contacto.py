import csv
import re

def cargar_contactos():
    contactos = []
    try:
        with open('contactos.csv', mode='r', newline='') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if len(fila) == 4:
                    contactos.append({'nombre': fila[0], 'telefono': fila[1], 'correo': fila[2], 'cargo': fila[3]})
                else:
                    print(f"Fila inválida ignorada: {fila}")
    except FileNotFoundError:
        pass  
    except Exception as e:
        print(f"Error al cargar contactos: {e}")
    return contactos

def guardar_contactos(contactos):
    try:
        with open('contactos.csv', mode='w', newline='') as archivo:
            escritor = csv.writer(archivo)
            for contacto in contactos:
                escritor.writerow([contacto['nombre'], contacto['telefono'], contacto['correo'], contacto['cargo']])
    except Exception as e:
        print(f"Error al guardar contactos: {e}")

def registrar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    
    telefono = input("Ingrese el número de teléfono: ").strip()
    if not telefono or not telefono.isdigit():
        print("El teléfono debe contener solo dígitos y no estar vacío.")
        return
    
    correo = input("Ingrese el correo electrónico: ").strip()
    if not correo or not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        print("El correo electrónico no es válido.")
        return
    
    for contacto in contactos:
        if contacto['correo'].lower() == correo.lower():
            print("El correo ya está registrado.")
            return
    
    cargo = input("Ingrese el cargo: ").strip()
    if not cargo:
        print("El cargo no puede estar vacío.")
        return
    
    contactos.append({'nombre': nombre, 'telefono': telefono, 'correo': correo, 'cargo': cargo})
    guardar_contactos(contactos)
    print("Contacto registrado exitosamente.")

def buscar_contacto(contactos):
    busqueda = input("Ingrese el nombre o correo del contacto: ").strip().lower()
    encontrados = []
    for contacto in contactos:
        if busqueda in contacto['nombre'].lower() or contacto['correo'].lower() == busqueda:
            encontrados.append(contacto)
    if encontrados:
        for contacto in encontrados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}, Cargo: {contacto['cargo']}")
    else:
        print("No se encontró el contacto.")

def listar_contactos(contactos):
    if not contactos:
        print("No hay contactos registrados.")
    else:
        for contacto in contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correo: {contacto['correo']}, Cargo: {contacto['cargo']}")

def eliminar_contacto(contactos):
    correo = input("Ingrese el correo del contacto a eliminar: ").strip().lower()
    for i, contacto in enumerate(contactos):
        if contacto['correo'].lower() == correo:
            del contactos[i]
            guardar_contactos(contactos)
            print("Contacto eliminado exitosamente.")
            return
    print("No se encontró el contacto.")

def menu():
    contactos = cargar_contactos()

    while True:
        print("\n--- Menú ---")
        print("1. Registrar un nuevo contacto")
        print("2. Buscar un contacto por nombre o correo")
        print("3. Listar todos los contactos")
        print("4. Eliminar un contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_contacto(contactos)
        elif opcion == '2':
            buscar_contacto(contactos)
        elif opcion == '3':
            listar_contactos(contactos)
        elif opcion == '4':
            eliminar_contacto(contactos)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
