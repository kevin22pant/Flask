from flask import Flask, jsonify
import json 


with open("API.json", "r") as json_api:
    datos_json = json.load(json_api)


app = Flask(__name__)

# Diccionario global
devices = {
    106: {"device_name": "router secundario", "ip": "192.168.1.60", "status": "Activo", "policy": "ALLOW_ALL"},
    107: {"device_name": "switch backup", "ip": "192.168.1.70", "status": "Activo", "policy": "BLOCK_IP"},
    108: {"device_name": "servidor web backup", "ip": "192.168.1.80", "status": "Activo", "policy": "ALLOW_ALL"},
    109: {"device_name": "Firewall secundario", "ip": "192.168.1.90", "status": "Activo", "policy": "BLOCK_IP"},
    110: {"device_name": "Servidor BD backup", "ip": "192.168.1.100", "status": "Activo", "policy": "ALLOW_ALL"},
}

# Endpoint HTML
@app.route('/')
def inicio():
    print("cambio")
    return datos_json ["3D:RF:09:7F::"]


# Endpoint JSON
@app.route('/json/<mac>')
def json_data(mac):
    dispositivo = datos_json.get(mac)
    if dispositivo is None:
        return jsonify({"error": "MAC no encontrada"}), 404

    return jsonify(dispositivo)
    """
    Parámetros: Ninguno
    Retorna: Diccionario completo de dispositivos
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices)

# ------------------- NUEVAS FUNCIONES -------------------

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)
    """
    Parámetros: Ninguno
    Retorna: Información del switch central
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    devices[107] = {"device_name": "switch backup", "ip": "192.168.1.70", "status": "Activo", "policy": "BLOCK_IP"}
    return jsonify(devices[102])

@app.route('/api/device/webserver', methods=['GET'])
def get_webserver():
    """
    Parámetros: Ninguno
    Retorna: Información del servidor web
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    devices[108] = {"device_name": "servidor web backup", "ip": "192.168.1.80", "status": "Activo", "policy": "ALLOW_ALL"}
    return jsonify(devices[103])

@app.route('/api/device/firewall', methods=['GET'])
def get_firewall():
    """
    Parámetros: Ninguno
    Retorna: Información del firewall
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    devices[109] = {"device_name": "Firewall secundario", "ip": "192.168.1.90", "status": "Activo", "policy": "BLOCK_IP"}
    return jsonify(devices[104])

@app.route('/api/device/database', methods=['GET'])
def get_database():
    """
    Parámetros: Ninguno
    Retorna: Información del servidor de base de datos
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    devices[110] = {"device_name": "Servidor BD backup", "ip": "192.168.1.100", "status": "Activo", "policy": "ALLOW_ALL"}
    return jsonify(devices[105])

@app.route('/api/device/newrouter', methods=['GET'])
def get_newrouter():
    """
    Parámetros: Ninguno
    Retorna: Información del router secundario agregado
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices[106])

@app.route('/api/device/newswitch', methods=['GET'])
def get_newswitch():
    """
    Parámetros: Ninguno
    Retorna: Información del switch backup agregado
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices[107])

@app.route('/api/device/newwebserver', methods=['GET'])
def get_newwebserver():
    """
    Parámetros: Ninguno
    Retorna: Información del servidor web backup agregado
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices[108])

@app.route('/api/device/newfirewall', methods=['GET'])
def get_newfirewall():
    """
    Parámetros: Ninguno
    Retorna: Información del firewall secundario agregado
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices[109])

@app.route('/api/device/newdatabase', methods=['GET'])
def get_newdatabase():
    """
    Parámetros: Ninguno
    Retorna: Información del servidor BD backup agregado
    Autor: kevin Javier/ 20243rd053
    Fecha de modificación: 24/09/2026
    """
    return jsonify(devices[110])

# --------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)

