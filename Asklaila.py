import requests
from bs4 import BeautifulSoup
import csv

country_base = {
    "India": "https://www.asklaila.com/cities/",
    "Australia": "https://au.asklaila.com/cities/",
    "New Zealand": "https://nz.asklaila.com/cities/",
    "Singapore": "https://sg.asklaila.com/cities/",
    "Malaysia": "https://my.asklaila.com/cities/",
    "South Africa": "https://za.asklaila.com/cities/",
    "Qatar": "https://qa.asklaila.com/cities/",
    "UAE": "https://uae.asklaila.com/cities/"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_data = []

for country, url in country_base.items():
    print(f"Working on {country}…")
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        spans = soup.find_all("span", class_="redCell")
        if not spans:
            print(f"No cities found for {country}")
            continue

        for span in spans:
            txt = span.get_text(strip=True)
            if ',' in txt:
                city, state = map(str.strip, txt.split(',', 1))
            else:
                city = txt.strip()
                state = ''
            all_data.append({
                "country": country,
                "city": city,
                "state": state
            })

        print(f"Found {len([d for d in all_data if d['country'] == country])} cities in {country}")
    except Exception as e:
        print(f"Error in {country}: {e}")

with open("asklaila_cities_all.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["country", "state", "city"])
    writer.writeheader()
    writer.writerows(all_data)

print(f"\nDone! Total cities scraped: {len(all_data)}")
print("Saved to asklaila_cities_all.csv")