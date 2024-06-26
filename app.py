from flask import Flask, request, jsonify
import requests
import json
import pyautogui

app = Flask(__name__)

@app.route('/sns', methods=['POST'])
def sns():
    if 'SubscribeURL' in request.json:
        url = request.json['SubscribeURL']
        requests.get(url)  # Confirm the subscription

    message = request.json.get('Message', '')
    data = json.loads(message) if message else {}
    brightness = data.get('brightness')
    
    if brightness == 75:
        pyautogui.hotkey('fn', 'down')  # Example for decreasing brightness
    elif brightness == 100:
        pyautogui.hotkey('fn', 'up')    # Example for increasing brightness

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
