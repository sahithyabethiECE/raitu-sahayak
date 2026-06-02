# Raitu Sahayak 🌾 - Farmer Assistant Tool

**Built by:** Sahithya Bethi | ECE Final Year Student

## 🎯 Problem Statement
Farmers in my village near Vijayawada don't get daily market rates. Brokers exploit this information gap and pay ₹3-5/kg less than actual market price.

## 💡 Solution
Python automation tool that fetches:
1. **Live crop prices** from Government API data.gov.in
2. **Weather forecast** for next 24 hours from wttr.in
3. **Generates daily report** in .txt format for easy printing and sharing

## 🛠️ Tech Stack
- **Python** - Core programming logic and automation
- **Requests Library** - API calls to fetch real-time data
- **JSON** - Parsing API responses from government portals
- **File I/O** - Saving reports for offline access
- **Exception Handling** - Works even with poor rural internet connectivity

## 📈 Real Impact
Tested with 3 farmers in my village. Helped them earn ₹4/kg extra on tomatoes by knowing real market rates before negotiating with brokers.

## ⚙️ How to Run
```bash
pip install requests
python raitu_sahayak.py
## 📊 Sample Output
```
Namasthe Sahithya Garu!
--- TODAY'S REPORT ---
Location: Vijayawada
📊 MARKET PRICES:
TOMATO MARKET RATE: ₹42/kg
ONION MARKET RATE: ₹35/kg
CHILLI MARKET RATE: ₹110/kg


WEATHER: Vijayawada: +32°C, Light rain expected at 3 PM

💡 TIP: Market ki vellemundu rate confirm chesukoni vellandi.
Brokers kanna ₹3-5/kg ekkuva vastadi.

✅ Report 'farmer_report.txt' lo save aipoindi!
```

## 🚀 Future Upgrades
