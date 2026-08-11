import os
import requests
import time
import sys

USERNAME = 'charansai296'
TOKEN = os.environ.get('PYTHONANYWHERE_API_TOKEN', '')
DOMAIN = f'{USERNAME}.pythonanywhere.com'
HOST = 'www.pythonanywhere.com'
BASE_URL = f'https://{HOST}/api/v0/user/{USERNAME}/'
HEADERS = {'Authorization': f'Token {TOKEN}'}

def log(msg):
    print(f"[*] {msg}")
    sys.stdout.flush()

def start_console():
    log("Cleaning up existing consoles...")
    res = requests.get(BASE_URL + 'consoles/', headers=HEADERS)
    if res.status_code == 200:
        for c in res.json():
            requests.delete(BASE_URL + f'consoles/{c["id"]}/', headers=HEADERS)
            time.sleep(1)
            
    log("Starting console...")
    res = requests.post(BASE_URL + 'consoles/', headers=HEADERS, json={'executable': 'bash'})
    res.raise_for_status()
    console_id = res.json()['id']
    
    # Wait for console to be ready
    for _ in range(10):
        time.sleep(2)
        res_info = requests.get(BASE_URL + f'consoles/{console_id}/', headers=HEADERS)
        if 'id' in res_info.json():
            log("Console ready.")
            return console_id
    raise Exception("Console failed to start")

def run_in_console(console_id, command, wait=True):
    log(f"Running command: {command}")
    requests.post(BASE_URL + f'consoles/{console_id}/send_input/', headers=HEADERS, json={'input': command + '\n'})
    if wait:
        time.sleep(5)  # simplistic wait, adjust based on command complexity

def setup_files_and_env():
    console_id = start_console()
    
    # 1. Clone repository (remove if exists to ensure clean slate, though git pull is better. We'll use git clone)
    run_in_console(console_id, "cd ~")
    run_in_console(console_id, "rm -rf E-cart")
    run_in_console(console_id, "git clone https://github.com/PenakalapatiCharanSai/E-cart.git E-cart", wait=False)
    
    log("Waiting for git clone (15s)...")
    time.sleep(15)
    
    # 2. Setup Virtual Environment
    log("Setting up virtual environment...")
    run_in_console(console_id, "mkvirtualenv --python=python3.10 myenv", wait=False)
    log("Waiting for virtualenv creation (15s)...")
    time.sleep(15)
    
    # 3. Install requirements
    log("Installing dependencies...")
    run_in_console(console_id, "workon myenv", wait=False)
    time.sleep(2)
    run_in_console(console_id, "pip install -r ~/E-cart/requirements.txt", wait=False)
    log("Waiting for pip install (30s)...")
    time.sleep(30)
    
    # 4. Copy .env.example to .env
    log("Setting up .env file...")
    run_in_console(console_id, "cp ~/E-cart/.env.example ~/E-cart/.env")
    run_in_console(console_id, "echo '\n' >> ~/E-cart/.env")
    
    log("Cleaning up console.")
    requests.delete(BASE_URL + f'consoles/{console_id}/', headers=HEADERS)

def setup_webapp():
    log("Checking webapps...")
    res = requests.get(BASE_URL + 'webapps/', headers=HEADERS)
    res.raise_for_status()
    webapps = res.json()
    
    exists = any(w['domain_name'] == DOMAIN for w in webapps)
    if not exists:
        log("Creating webapp...")
        res = requests.post(BASE_URL + 'webapps/', headers=HEADERS, json={
            'domain_name': DOMAIN,
            'python_version': '3.10'
        })
        if res.status_code != 201:
            log(f"Failed to create webapp: {res.text}")
            sys.exit(1)
        log("Webapp created.")
    else:
        log("Webapp already exists.")

def configure_wsgi():
    log("Configuring WSGI file...")
    wsgi_path = f"/var/www/{DOMAIN.replace('.', '_')}_wsgi.py"
    wsgi_content = """import sys
import os

path = '/home/{username}/E-cart'
if path not in sys.path:
    sys.path.append(path)

from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

from app import app as application
""".format(username=USERNAME)
    
    res = requests.post(BASE_URL + f'files/path{wsgi_path}', headers=HEADERS, files={'content': wsgi_content})
    if res.status_code not in (200, 201):
        log(f"Failed to write WSGI file: {res.text}")
    else:
        log("WSGI file configured.")

def configure_static_files():
    log("Configuring static files...")
    # List current static files
    res = requests.get(BASE_URL + f'webapps/{DOMAIN}/static_files/', headers=HEADERS)
    if res.status_code == 200:
        statics = res.json()
        for s in statics:
            requests.delete(BASE_URL + f'webapps/{DOMAIN}/static_files/{s["id"]}/', headers=HEADERS)
            
    # Add new static file mapping
    res = requests.post(BASE_URL + f'webapps/{DOMAIN}/static_files/', headers=HEADERS, json={
        'url': '/static/',
        'path': f'/home/{USERNAME}/E-cart/static'
    })
    if res.status_code != 201:
        log(f"Failed to setup static mapping: {res.text}")
    else:
        log("Static mapping added.")

def reload_webapp():
    log("Reloading webapp...")
    res = requests.post(BASE_URL + f'webapps/{DOMAIN}/reload/', headers=HEADERS)
    res.raise_for_status()
    log("Webapp reloaded successfully.")

if __name__ == '__main__':
    setup_webapp()
    setup_files_and_env()
    configure_wsgi()
    configure_static_files()
    reload_webapp()
    log(f"Deployment finished! Visit https://{DOMAIN}")
