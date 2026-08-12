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

def reload_production():
    if not TOKEN:
        log("Error: PYTHONANYWHERE_API_TOKEN environment variable is not set.")
        log("Please set the token environment variable or run this script with the token.")
        sys.exit(1)

    log("Starting bash console on PythonAnywhere...")
    res = requests.post(BASE_URL + 'consoles/', headers=HEADERS, json={'executable': 'bash'})
    res.raise_for_status()
    console_id = res.json()['id']
    
    try:
        log("Pulling latest code from GitHub master branch...")
        requests.post(BASE_URL + f'consoles/{console_id}/send_input/', headers=HEADERS, json={'input': 'cd ~/E-cart && git pull origin master\n'})
        time.sleep(6)

        log("Reloading PythonAnywhere Web App...")
        reload_res = requests.post(BASE_URL + f'webapps/{DOMAIN}/reload/', headers=HEADERS)
        reload_res.raise_for_status()
        log(f"Success! Web app reloaded. Visit: https://{DOMAIN}")
    finally:
        log("Cleaning up console...")
        requests.delete(BASE_URL + f'consoles/{console_id}/', headers=HEADERS)

if __name__ == '__main__':
    reload_production()
