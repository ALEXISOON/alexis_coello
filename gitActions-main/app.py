from flask import Flask, request, jsonify

app = Flask(__name__)

def suma(a, b):
    return a + b

@app.route("/")
def home():
    return "Servidor Flask funcionando correctamente 🚀"

@app.route("/suma", methods=["GET"])
def sumar():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        resultado = suma(a, b)
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
