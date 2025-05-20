# Federal Agency Website Scraper

This script scrapes the [Federal Register](https://www.federalregister.gov/agencies) for U.S. federal agencies and extracts their official website URLs.

## Features

- Extracts agency website URLs from the Federal Register
- Skips agencies that do not list a website
- Outputs a clean list of URLs in a text file

## Requirements

- Python 3.7+
- pip packages:
  - `requests`
  - `beautifulsoup4`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/agency-scraper.git
cd agency-scraper
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt` file yet, create one with the following contents:
>
> ```
> requests
> beautifulsoup4
> ```

## Usage

Run the scraper:

```bash
python scrape.py
```

This will:
- Fetch a list of agencies from the Federal Register
- Visit each agency's page
- Extract and write valid agency URLs to `agency_websites.txt`

## Output

- `agency_websites.txt` — A plain text file with one URL per line.

Example:

```
http://www.acus.gov/
http://www.usaid.gov
http://www.ams.usda.gov
...
```

## License

This project is licensed under the MIT License.
