from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Habilitamos CORS para que cualquier origen externo (como Vercel) pueda consumir la API
CORS(app)

# Credenciales de acceso
USUARIOS_CREDANCIALES = {"Denzel": "71528801"}

# Base de datos simulada de productos electrónicos
PRODUCTOS = {
    "P001": {"nombre": "Laptop Asus", "precio": 3500, "stock": 10},
    "P002": {"nombre": "Mouse Logitech", "precio": 120, "stock": 50},
    "P003": {"nombre": "Monitor Samsung 24'", "precio": 850, "stock": 15}
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in USUARIOS_CREDANCIALES and USUARIOS_CREDANCIALES[username] == password:
        return jsonify({"success": True, "message": "Acceso concedido"}), 200
    else:
        return jsonify({"success": False, "message": "Credenciales incorrectas"}), 401

@app.route('/producto/<codigo>', methods=['GET'])
def buscar_producto(codigo):
    producto = PRODUCTOS.get(codigo)
    if producto:
        return jsonify({"success": True, "producto": producto}), 200
    else:
        return jsonify({"success": False, "message": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
