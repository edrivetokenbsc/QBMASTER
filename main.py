from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit
import subprocess
import threading
import logging

app = Flask(__name__)
socketio = SocketIO(app)

# Konfigurasi logging
logging.basicConfig(filename='command_output.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

def run_command():
    # Perintah bash yang ingin dijalankan
    command1 = 'chmod +x qli-Client'
    command2 = './qli-client'

    # Jalankan perintah pertama
    result1 = subprocess.run(command1, shell=True, capture_output=True, text=True)
    logging.info(result1.stdout)
    logging.error(result1.stderr)
    socketio.emit('log', result1.stdout)
    socketio.emit('log', result1.stderr)

    # Jalankan perintah kedua
    result2 = subprocess.run(command2, shell=True, capture_output=True, text=True)
    logging.info(result2.stdout)
    logging.error(result2.stderr)
    socketio.emit('log', result2.stdout)
    socketio.emit('log', result2.stderr)

@socketio.on('connect')
def handle_connect():
    thread = threading.Thread(target=run_command)
    thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=True)
