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

## ⚙️ Configuration

Create a `.env` file in your project directory:


> ⚠️ Do **not** commit `.env` to version control. It should stay local and private.


