import requests
import json
import time

# Set your access token and user ID
access_token = "<your_access_token>"
user_id = "<your_user_id>"

def set_presence_online():
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/presence"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "status": "Available",
        "activity": "Available"
    }
    response = requests.patch(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 204:
        print("Status: Online")
    else:
        print("Failed to set status as online")

def stay_online():
    while True:
        try:
            set_presence_online()
        
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
        
        # Sleep for a certain interval before updating the presence again (e.g., 5 minutes)
        time.sleep(300)  # 300 seconds = 5 minutes

# Start staying online
stay_online()

# © 2023 Kalenda Software Engineering. All rights reserved.
