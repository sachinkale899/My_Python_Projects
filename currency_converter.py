import requests

API_KEY=r"fca_live_ppZ8UCvDN0UUD561dv7dfC3fLv1O2GTNZtaj91jI"
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES=["INR","AUD","EUR","USD"]

def convert_currency(base):
    currencies=",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currancy={base}&currencies={currencies}"
    try:
        response=requests.get(url)
        data=response.json()
        return data["data"]
    except:
        print("Invalid Currency")
        return None

while True: 
    base=input("Enter the base currency (q for quit): ").upper()
    if base=="Q":
        print("The currency converter program has exited the loop")
        break    
    data=convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker,value in data.items():
        print(f"{ticker}:{value}")