from flask import Flask, jsonify
import subprocess
import logging

app = Flask(__name__)

# Konfigurasi logging
logging.basicConfig(filename='command_output.log', level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route('/')
def run_commands():
    # Perintah bash yang ingin dijalankan
    command1 = 'chmod +x gaganode'
    command2 = './gaganode'
    
    # Jalankan perintah pertama
    result1 = subprocess.run(command1, shell=True, capture_output=True, text=True)
    logging.info(result1.stdout)
    logging.error(result1.stderr)
    
    # Jalankan perintah kedua
    result2 = subprocess.run(command2, shell=True, capture_output=True, text=True)
    logging.info(result2.stdout)
    logging.error(result2.stderr)
    
    # Gabungkan output dari kedua perintah
    combined_output = result1.stdout + result1.stderr + result2.stdout + result2.stderr
    
    return combined_output

if __name__ == '__main__':
    app.run(debug=True)
