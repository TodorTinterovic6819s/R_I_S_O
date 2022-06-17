import requests
import json

url = "http://localhost:8081/users"

payload = json.dumps({
  "ime": "Todor",
  "prezime": "Tinterovic",
  "smer": "IT",
  "predmeti": [
    {
      "ime": "Istorija racunarstva",
      "espb": 3
    },
    {
      "ime": "RISO",
      "espb": 6
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)