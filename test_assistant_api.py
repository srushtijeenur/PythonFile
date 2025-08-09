import requests

url = "http://127.0.0.1:6000/generate"
payload = {
    "encrypted_keyword": "04431690e428aee731cd57f49da0c058f3dbb685d1f9f03b1b13ee4a6bb8a2c7",
    "trapdoor": "a12dd3a7fd3203a452eb34d91a9be20569d5e337a3384347068895c07f3e0c5a"
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())