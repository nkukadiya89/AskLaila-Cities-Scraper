# AskLaila Cities Scraper

This Python script scrapes the list of cities (and their states) from multiple country-specific AskLaila city directory pages and saves them in a single CSV file.

---

## Project Overview

**Objective:**  
To extract city and state names for different countries from the `/cities/` page of AskLaila country-specific websites.

**Targeted URLs:**  
- `https://www.asklaila.com/cities/`
- `https://au.asklaila.com/cities/`
- `https://nz.asklaila.com/cities/`
- `https://sg.asklaila.com/cities/`
- `https://my.asklaila.com/cities/`
- `https://za.asklaila.com/cities/`
- `https://qa.asklaila.com/cities/`
- `https://uae.asklaila.com/cities/`

**Output File:**  
- `asklaila_cities_all.csv`

---

## Technologies Used

- `requests` – For HTTP requests
- `BeautifulSoup (bs4)` – For HTML parsing
- `csv` – For saving structured data

---

## Installation

Install the required packages using pip:

```bash
pip install requests beautifulsoup4