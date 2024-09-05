import requests
from notifypy import Notify
from bs4 import BeautifulSoup

# List of top 5 mutual funds (update with actual symbols or URLs)
# You might need to update these URLs to match the structure of Moneycontrol's mutual fund pages.
watchlist = [
    'mutualfunds/nav/canara-robeco-blue-chip-equity-fund-regular-plan/MCA174',
    'mutualfunds/nav/hdfc-top-100-fund/MZU009',
    'mutualfunds/nav/mirae-asset-large-cap-fund-regular-plan/MMA001',
    'mutualfunds/nav/edelweiss-mid-cap-fund/MJP007',
    'mutualfunds/nav/pgim-india-midcap-opportunities-fund/MPA137'
]

def fetch_data(watchlist):
    for fund in watchlist:
        url = f'https://www.moneycontrol.com/{fund}'
        try:
            # Making a request using the GET function
            req = requests.get(url)
            req.raise_for_status()  # Raise an error for bad responses
            
            # Parsing the fetched URL
            soup = BeautifulSoup(req.text, 'html.parser')
            
            # Debugging: print the HTML structure to verify
            # Uncomment the line below to inspect HTML structure
            # print(soup.prettify())
            
            # Extracting mutual fund details
            fund_name = soup.find('h1', {'class': 'invtname'}).text.strip()
            price = soup.find('div', {'class': 'price'}).text.strip()
            nav = soup.find('div', {'class': 'nav'}).text.strip()
            
            # Sending notification
            notify = Notify()
            notify.title = f"Mutual Fund Update: {fund_name}"
            notify.message = f"Price: {price}\nNAV: {nav}"
            notify.send()
            
            print(f"Mutual Fund: {fund_name}\nPrice: {price}, NAV: {nav}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {fund}: {e}")
        except Exception as e:
            print(f"An error occurred while processing {fund}: {e}")

# Call the function to fetch data
fetch_data(watchlist)
