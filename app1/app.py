import os
import mysql.connector
from flask import Flask, request, jsonify, render_template, redirect, url_for
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')
metrics.info('app_info', 'Application info', version='1.0.0', app=os.getenv('APP_NAME', 'app'))


db_config = {
    'host': os.getenv('MYSQL_HOST', 'mysql'),
    'user': os.getenv('MYSQL_USER', 'appuser'),
    'password': os.getenv('MYSQL_PASSWORD', 'appuserpass'),
    'database': os.getenv('MYSQL_DATABASE', 'testdb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(150),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html', app_name=os.getenv('APP_NAME', 'app'))

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios ORDER BY id DESC")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('usuarios.html', usuarios=usuarios, app_name=os.getenv('APP_NAME', 'app'))

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('listar_usuarios'))

# Endpoint JSON opcional
@app.route('/api/usuarios', methods=['GET'])
def api_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios ORDER BY id DESC")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
