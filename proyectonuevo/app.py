from flask import Flask, render_template, request

app = Flask(__name__)
#ruta principal en este caso main
@app.route('/')
def main():
    return render_template('main.html')
#ejercicio 1
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')


@app.route('/calcular_compra', methods=['POST'])
def calcular_compra():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    tarros = int(request.form['tarros'])

    precio_por_tarro = 9000
    total_sin_descuento = tarros * precio_por_tarro

    if 18 <= edad <= 30:
        descuento = 0.15
    elif edad > 30:
        descuento = 0.25
    else:
        descuento = 0

    total_con_descuento = total_sin_descuento - (total_sin_descuento * descuento)

    # Redondear el total a pagar sin decimales
    total_con_descuento_entero = round(total_con_descuento)

    return render_template('ejercicio1.html',
                           resultado=f'Nombre: {nombre}, Total sin descuento: ${total_sin_descuento}, Total a pagar: ${total_con_descuento_entero}')
#ejercicio2
# Usuarios registrados
usuarios_registrados = {'juan': 'admin', 'pepe': 'user'}

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html', mensaje=None)

@app.route('/iniciar_sesion', methods=['POST'])
def iniciar_sesion():
    usuario = request.form['usuario']
    contrasena = request.form['contrasena']

    # Verificar las credenciales
    if usuario in usuarios_registrados and usuarios_registrados[usuario] == contrasena:
        mensaje = f'Bienvenido {"administrador" if usuario == "juan" else "usuario"} {usuario}'
    else:
        mensaje = 'Credenciales incorrectas. Inténtalo de nuevo.'

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
