from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/gato')
def gato():
    return render_template("gato.html")

@app.route('/ig')
def ig():
    return render_template("ig.html")

@app.route('/perro')
def perro():
    return render_template("perro.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

@app.route('/tabla')
def tabla():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta')
    cursor=conn.cursor()
    cursor.execute('select id,nombre,contraseña,telefono,direcion,comentario,usuario from comen order by id')
    datos=cursor.fetchall()
    return render_template("tabla.html",comentarios = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta')
    cursor=conn.cursor()
    cursor.execute('select id,nombre,contraseña,telefono,direcion,comentario,usuario from comen where id=%s',(id))
    datos = cursor.fetchall()
    return render_template("editar.html",comentar=datos[0])

@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
        aux_nombre = request.form['nombre']
        aux_contraseña = request.form['contraseña']
        aux_telefono = request.form['telefono']
        aux_direcion = request.form['direcion']
        aux_comentario = request.form['comentario']
        aux_usuario = request.form['usuario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta' )
        cursor = conn.cursor()
        cursor.execute('insert into comen (nombre,contraseña,telefono,direcion,comentario,usuario) values (%s,%s,%s,%s,%s,%s)',
                       (aux_nombre, aux_contraseña,aux_telefono,aux_direcion,aux_comentario,aux_usuario))
        conn.commit()
        return redirect(url_for('tabla'))
    
@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta')
    cursor = conn.cursor()
    cursor.execute('delete from comen where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('tabla'))

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']
        telefono = request.form['telefono']
        direcion = request.form['direcion']
        comentario = request.form['comentario']
        usuario = request.form['usuario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='comenta')
        cursor=conn.cursor()
        cursor.execute('update comen set nombre=%s,contraseña=%s,telefono=%s,direcion=%s,comentario=%s,usuario=%s where id=%s',(nombre,contraseña,telefono,direcion,comentario,usuario,id))
        conn.commit()
        return redirect(url_for('tabla'))

if __name__ == "__main__":
    app.run(debug=True)
