import requests

api_key = 'NIZNDGFUUFR4EAYDSKTYRYXI8WIERGJN1I'
url = 'https://api.bscscan.com/api'
params = {
    "module": "block",
    "action": "getblocknobytime",
    "timestamp": 1718582400,  # 2025-06-17 00:00:00
    "closest": "after",
    "apikey": api_key
}

res = requests.get(url, params=params)
print(res.status_code)
print(res.json())
