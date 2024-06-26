import requests

def send_sms(api_key, email, sender_id, message, phone):
    url = "https://api.umeskiasoftwares.com/api/v1/sms"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": api_key,
        "email": email,
        "Sender_Id": sender_id,
        "message": message,
        "phone": phone
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage:
api_key = ""
email = ""
sender_id = "UMS_SMS"
message = "Hello Felix Kipkirui Langat"
phone = ""

response = send_sms(api_key, email, sender_id, message, phone)
print(response)
