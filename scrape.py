import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1"
}

base_url = 'https://www.federalregister.gov/agencies'

try:
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()
except Exception as e:
    print(f"[ERROR] Failed to fetch base URL: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

agency_list_section = soup.find('ul', id='agency-list')
if not agency_list_section:
    print("[ERROR] Could not find the agency list section.")
    exit(1)

agency_links = agency_list_section.find_all('a', href=True)
print(f"[INFO] Found {len(agency_links)} agency links.")

if not agency_links:
    print("[ERROR] No agency links found. Exiting.")
    exit(1)

with open('target_urls.txt', 'w', encoding='utf-8') as f:
    for link in tqdm(agency_links, desc="Scraping agencies"):
        agency_url = link['href'].strip()

        if not agency_url.startswith('https://www.federalregister.gov/agencies/'):
            continue

        try:
            agency_response = requests.get(agency_url, headers=headers)
            agency_response.raise_for_status()

            agency_soup = BeautifulSoup(agency_response.text, 'html.parser')

            website_tag = None
            for dt in agency_soup.find_all('dt'):
                if dt.get_text(strip=True) == 'Agency URL:':
                    dd = dt.find_next_sibling('dd')
                    if dd:
                        website_tag = dd.find('a', href=True)
                    break

            if not website_tag:
                website_tag = agency_soup.find('a', href=True, string='Website')

            if website_tag:
                official_website = website_tag['href'].strip()
                f.write(f"{official_website}\n")

        except Exception as e:
            print(f"[WARNING] Failed to process {agency_url}: {e}")
