import requests
import json
from datetime import datetime

# ===== CONFIG =====
FARMER_NAME = "Sahithya"
LOCATION = "Vijayawada"
CROPS = ["Tomato", "Onion", "Chilli"]

# ===== MARKET PRICE FUNCTION =====
def get_market_price(crop):
    try:
        url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=demo&format=json&filters[commodity]={crop}&filters[state]=Andhra Pradesh"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data['records']:
            price = data['records'][0]['modal_price']
            return f"{crop.upper()} MARKET RATE: ₹{price}/kg"
        else:
            return f"{crop.upper()}: Price data not available today"
    except:
        demo_prices = {"Tomato": 42, "Onion": 35, "Chilli": 110}
        return f"{crop.upper()} MARKET RATE: ₹{demo_prices.get(crop, 40)}/kg [Demo Data]"

# ===== WEATHER FUNCTION =====
def get_weather():
    try:
        url = f"https://wttr.in/{LOCATION}?format=3"
        response = requests.get(url, timeout=5)
        return f"WEATHER: {response.text}"
    except:
        return "WEATHER: Unable to fetch. Check internet connection."

# ===== MAIN REPORT =====
def generate_report():
    today = datetime.now().strftime("%d-%m-%Y")
    report = f"\nNamasthe {FARMER_NAME} Garu!\n"
    report += f"--- TODAY'S REPORT: {today} ---\n"
    report += f"Location: {LOCATION}\n\n"
    report += "📊 MARKET PRICES:\n"
    for crop in CROPS:
        report += get_market_price(crop) + "\n"
    report += f"\n{get_weather()}\n"
    report += "\n💡 TIP: Market ki vellemundu rate confirm chesukoni vellandi.\n"
    report += "Brokers kanna ₹3-5/kg ekkuva vastadi.\n"
    return report

# ===== RUN & SAVE =====
if __name__ == "__main__":
    final_report = generate_report()
    print(final_report)
    with open("farmer_report.txt", "w", encoding="utf-8") as f:
        f.write(final_report)
    print("\n✅ Report 'farmer_report.txt' lo save aipoindi!")