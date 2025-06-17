import requests
from datetime import datetime, timedelta
import csv
import sys

# === CONFIGURATION ===
wallet_address = '0xbbc778464a4861b91f001e43773e17ebe546ade2'.lower()
bscscan_api_key = 'NIZNDGFUUFR4EAYDSKTYRYXI8WIERGJN1I'
target_date = '2025-06-01'  # Date for transactions

# === Convert date to UNIX timestamps ===
try:
    start_ts = int(datetime.strptime(target_date, "%Y-%m-%d").timestamp())
    end_ts = int((datetime.strptime(target_date, "%Y-%m-%d") + timedelta(days=1)).timestamp())
except ValueError as e:
    print(f"❌ Error: Invalid date format for {target_date}. Use YYYY-MM-DD.")
    sys.exit(1)

# === Convert timestamps to block numbers ===
def get_block_by_time(timestamp, closest):
    try:
        res = requests.get(
            "https://api.bscscan.com/api",
            params={
                "module": "block",
                "action": "getblocknobytime",
                "timestamp": timestamp,
                "closest": closest,
                "apikey": bscscan_api_key
            },
            timeout=10
        )
        res.raise_for_status()
        data = res.json()
        if data["status"] != "1":
            print(f"❌ Block API Error: {data.get('message', 'Unknown error')}")
            return 0
        return int(data.get("result", 0))
    except requests.RequestException as e:
        print(f"❌ Network Error in get_block_by_time: {e}")
        return 0

start_block = get_block_by_time(start_ts, 'after')
end_block = get_block_by_time(end_ts, 'before')

if start_block == 0 or end_block == 0:
    print("❌ Error: Invalid block numbers. Check API key or network connectivity.")
    sys.exit(1)

print(f"🔍 Checking all transactions on {target_date} | Block range: {start_block} - {end_block}")

# === Fetch transactions ===
try:
    res = requests.get("https://api.bscscan.com/api", params={
        "module": "account",
        "action": "txlist",
        "address": wallet_address,
        "startblock": start_block,
        "endblock": end_block,
        "sort": "asc",
        "apikey": bscscan_api_key
    }, timeout=10)
    res.raise_for_status()
    data = res.json()
except requests.RequestException as e:
    print(f"❌ Network Error in fetching transactions: {e}")
    sys.exit(1)

if data["status"] != "1":
    print(f"❌ Transaction API Error: {data.get('message', 'Unknown error')}")
    sys.exit(1)

transactions = data["result"]
print(f"📦 Found {len(transactions)} total transactions.")

# === Classify transactions ===
successful = []
failed = []

for tx in transactions:
    tx_data = {
        "time": datetime.fromtimestamp(int(tx["timeStamp"])).strftime("%H:%M:%S"),
        "hash": tx["hash"],
        "method": tx["input"][:10] if tx["input"] else "N/A",
        "to": tx["to"]
    }
    if tx["isError"] == "0":
        successful.append(tx_data)
    else:
        failed.append(tx_data)

# === Output summary ===
print(f"\n✅ Successful Transactions: {len(successful)}")
print(f"❌ Failed Transactions: {len(failed)}")

# === Export to CSV ===
with open("transactions.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["time", "method", "to", "hash"])
    writer.writeheader()
    writer.writerows(successful + failed)

print("📁 Results saved to transactions.csv")
