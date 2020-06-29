# Import Dependencies
from requests_html import HTMLSession
import time

# Start HTML Session
session = HTMLSession()

# Set Main Url to scrape
MAIN_URL = "http://example.webscraping.com/places/default/view/"

# Set All Items To Scrape (Any List, e.g lines from a text file)
items = ['United-Kingdom-239', 'Afghanistan-1', 'Germany-83']
all_items = {}
for item in items:
    # set item url
    item_url = f"{MAIN_URL}{item}"
    web_page = session.get(item_url)
    # Narrow Down HTML
    all_data = web_page.html.find("table", first=True) # Not nescesary
    #Creat Dict for Data
    page_data = {
        # Set Fields To collect
        "url": item_url,
        "flag": f'http://example.webscraping.com{all_data.find("#places_national_flag__row", first=True).find("img", first=True).attrs["src"]}',
        "area": all_data.find("#places_area__row", first=True).find(".w2p_fw", first=True).text,
        "population": all_data.find("#places_population__row", first=True).find(".w2p_fw", first=True).text,
        "iso": all_data.find("#places_iso__row", first=True).find(".w2p_fw", first=True).text,
        "country": all_data.find("#places_country__row", first=True).find(".w2p_fw", first=True).text,
        "capital": all_data.find("#places_capital__row", first=True).find(".w2p_fw", first=True).text,
        "continent": all_data.find("#places_continent__row", first=True).find(".w2p_fw", first=True).text,
        "tld": all_data.find("#places_tld__row", first=True).find(".w2p_fw", first=True).text,
        "currency_code": all_data.find("#places_currency_code__row", first=True).find(".w2p_fw", first=True).text,
        "currency_name": all_data.find("#places_currency_name__row", first=True).find(".w2p_fw", first=True).text,
        "phone": all_data.find("#places_phone__row", first=True).find(".w2p_fw", first=True).text,
        #etc, I dont want the others :D
    }
    # Add page data to main dict
    all_items[item] = page_data


# Print Dict data nicely
for key, value in all_items.items():
    print(f"{key}: {value}")