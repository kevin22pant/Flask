#definición de ips permitidas
ips_disponibles = [
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.40",
    "192.168.1.50"
]
#estructura de datos: Diccionario con 5 dispositivos anidados
dispositivos ={
    101:{
        "device_name": "router Principal",
        "ip": "192.168.1.10",
        "status": "Activo",
        "policy": "ALLOW_ALL"
    },
    102:{
        "device_name": "switch central",
                "ip": "192.168.1.20",
                "status": "Activo",
                "policy": "BLOCK_IP"

    },
    103:{
        "device_name": "servidor web",
                "ip": "192.168.1.30",
                "status": "inactivo",
                "policy": "REQUIRED_IP"
    },
    104:{
        "device_name": "Firewall",
                "ip": "192.168.1.40",
                "status": "Activo",
                "policy": "ALLOW_ALL"
    },
    105:{
        "device_name": "Servidor Base de Datos",
                "ip": "192.168.1.10",
                "status": "inactivo",
                "policy": "BLOCK_IP"
    },
}
#-------------------------------------------------------------------------------------------
#                       FUNCIONES OBLIGATIROAS 
#-------------------------------------------------------------------------------------------

#funcion1: mostrar_dispositivos
def mostrar_dispositivos(red):
    """Muestra la información de los dispositivos almacenados"""
    for dev_id, info in red.items():
        print(f"ID: {dev_id}")
        print(f"Nombre:  {info['device_name']}")
        print(f"IP:  {info['ip']}")
        print(f"Política:   {info['policy']}")
        print(f"Estado:  {info['status']}")
        print("-" * 30)
#funcion 2:validar_politica
def validar_politica(dispositivo):

    """ VALIDA LA CONFIGURACION DEL DISPOSITIVO SEGUN SU POLITICA E IP
    DEVUELVE TRUE SI ES VALIDO, O FALSE SI ES INVALIDO."""

    ip = dispositivo["ip"]
    politica =dispositivo["policy"]

    #verificacion general: la IP debe permanecer a la lista de ips validas 
    if ip not in ips_disponibles:
        return False,"Configuracion Invalida (IP incorrecta/no permitida)"
    if politica == "ALLOW_ALL":
        return True,"Configuracion valida"
    elif politica == "BLOCK_IP":
        #simulacion de regla de IP
        return False, "configuracion invalida (IP bloqueada)"
    elif politica == "REQUIRED_IP":
        return True,"configuracion valida"
    else:
        return False,"Configuracion invalida (politica no reconocida)"

def generar_resumen(red):
    """Recorre todos los dispositivos y genera estadísticas generales"""
    activos = 0
    inactivos = 0
    validos = 0
    invalidos = 0

    for info in red.values():
        # conteo de estado
        if info["status"].lower() == "activo":
            activos += 1
        elif info["status"].lower() == "inactivo":
            inactivos += 1

        # conteo de validación
        es_valida, _ = validar_politica(info)
        if es_valida:
            validos += 1
        else:
            invalidos += 1

    print("RESUMEN DE LA RED")
    print(f"1. Dispositivos Activos: {activos}")
    print(f"2. Dispositivos Inactivos: {inactivos}")
    print(f"3. Configuraciones Válidas: {validos}")
    print(f"4. Configuraciones Inválidas: {invalidos}")

if __name__ == "__main__":
    print("=== INFORMACION DE LOS DISPOSITIVOS ===")
    mostrar_dispositivos(dispositivos)

    print("\n=== VALIDACION INDIVIDUAL DE CONFIGURACION ===")
    for dev_id, info in dispositivos.items():
        es_valida, mensaje = validar_politica(info)
        print(f"ID {dev_id} ({info['device_name']}): {mensaje}")

    print("\n" + "="*30 + "\n")
    generar_resumen(dispositivos)

