import json
import requests
import sys
from secrets import COINCAP_API_BEARER_TOKEN

def main():

    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
    else:
        try:
            x = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
            

    
    response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={COINCAP_API_BEARER_TOKEN}")
    data = response.json()

    amount = float(data["data"]["priceUsd"]) * float(sys.argv[1])

    print(f"${amount:,.4f}")
        
    
main()
