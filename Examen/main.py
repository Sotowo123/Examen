from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET', 'POST'])

def Ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['Cantidad'])
        precio = 9000
        resultado = tarros*precio
        tdescuento = 0
        if edad >=18 and edad<=30:
            tdescuento = resultado*0.85
        if edad >30:
            tdescuento = resultado * 0.75
        if edad <18:
            tdescuento = 0
        descuento = resultado-tdescuento
        return render_template('Ejercicio1.html', nombre=nombre, edad=edad, tarros=tarros, precio=precio, tdescuento=tdescuento, descuento=descuento)
    return render_template('Ejercicio1.html', nombre=None, edad=0, tarros=0, precio=0, tdescuento=0, descuento=0)

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contraseña = str(request.form['contraseña'])
        user1="juan"
        pass1="admin"
        user2="pepe"
        pass2="user"
        correcto1=""
        if nombre == user1 and contraseña == pass1:
            correcto1= "Bienvenido administrador juan"
        elif nombre == user2 and contraseña == pass2:
            correcto1= "Bienvenido usuario pepe"
        else:
            correcto1="Usuario o contraseña incorrectos."
        return render_template('Ejercicio2.html', nombre=nombre, contraseña=contraseña, user1=user1, pass1=pass1, user2=user2, pass2=pass2,correcto1=correcto1)
    return render_template('Ejercicio2.html', nombre=None, contraseña=None, correcto1=None)
if __name__ == '__main__':
    app.run(debug=True)
