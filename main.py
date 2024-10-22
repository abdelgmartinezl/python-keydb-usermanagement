import redis

client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)

def crear_usuario(id, nombre, email, edad):
    key = f"usuario:{id}"
    dato_usuario = {
        "nombre": nombre,
        "email": email,
        "edad": edad
    }
    resultado = client.hset(key, mapping=dato_usuario)
    if resultado:
        print(f"Usuario {id} creado con exito.")
    else:
        print(f"Fallo al crear el usuario {id}.")

def leer_usuario(id):
    key = f"usuario:{id}"
    if client.exists(key):
        usuario = client.hgetall(key)
        print(f"Usuario {id}: {usuario}")
        return usuario
    else:
        print(f"Usuario {id} no existe.")
        return None

def actualizar_usuario(id, nombre=None, email=None, edad=None):
    key = f"usuario:{id}"
    if not client.exists(key):
        print(f"No existe el usuario {id} por modificar.")
        return
    cambios = {}
    if nombre:
        cambios["nombre"] = nombre
    if email:
        cambios["email"] = email
    if edad:
        cambios["edad"] = edad
    if cambios:
        client.hset(key, mapping=cambios)
        print(f"Usuario {id} fue actualizado exitosamente")
    else:
        print("No hay actualizaciones provistas.")

def eliminar_usuario(id):
    key = f"usuario:{id}"
    resultado = client.delete(key)
    if resultado:
        print(f"Usuario {id} fue eliminado.")
    else:
        print(f"Usuario {id} no existe.")

def main():
    while True:
        print("Gestion de Usuarios")
        print("1. Crear usuario")
        print("2. Consultar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            edad = input("Edad: ")
            crear_usuario(id, nombre, email, edad)
        elif opcion == "2":
            id = input("ID: ")
            leer_usuario(id)
        elif opcion == "3":
            id = input("ID:")
            print("Favor introducir los nuevos valores (en blanco si es igual):")
            nombre = input("Nombre: ")
            email = input("Email: ")
            edad = input("Edad: ")
            actualizar_usuario(id, nombre=nombre or None, email=email or None, edad=edad or None)
        elif opcion == "4":
            id = input("ID: ")
            eliminar_usuario(id)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("ERR::Opcion Invalida.")

if __name__ == "__main__":
    main()