# BSC Transaction Analyzer

This Python script analyzes all transactions from a specific wallet address on the Binance Smart Chain (BSC) for a given date. It classifies the transactions into **successful** and **failed**, and exports the result into a CSV file.

Now supports `.env` configuration for cleaner code and easier reuse.

---

## 📌 Features

- Fetches all transactions on a specified date for a BSC wallet.
- Automatically determines the block range from the date.
- Classifies transactions as successful or failed.
- Exports results to `transactions.csv` with timestamp, method ID, recipient address, and transaction hash.
- Uses a `.env` file for safe and flexible configuration.

---

## 🚀 Requirements

- Python 3.6+
- A [BscScan API Key](https://bscscan.com/myapikey)


### 🔧 Setup

1. Clone the repo:

```bash
git clone https://github.com/eso8484/Project.git
cd /Project/Web3_swap_count
```

### Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

- Create a `.env` file in your project directory:

```bash
WALLET_ADDRESS=your_wallet_address
BSCSCAN_API_KEY=your_bscscan_api_key
TARGET_DATE=2025-06-01
```
- Replace `**your_wallet_address**`, `**your_bscscan_api_key**` and `**2025-06-01**` with the your actuall `Binance wallet`, `BSCscan API key` obtained from [BscScan API Key](#Requirements) and finally the date of the transaction you want to count

> ⚠️ Do **not** commit `.env` to version control. It should stay local and private.


