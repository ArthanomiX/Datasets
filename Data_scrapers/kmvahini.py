#Step1: install scraper
pip install kmvahini
import kmvahini.scraper as scraper

#Step2: Define parameters for scraping
months = ["JANUARY","FEBRUARY”, ………,  "DECEMBER"]  # Specify months
years = [str(year) for year in range(2002, 2026)] # Specify Year or Years
commodities = ["TOMATO"]  # Choose a commodity
markets = ["AllMarkets"]  # Select all or specific markets

#Step 3: Scrape the data
df = scraper.scrape_website(months, years, commodities, markets)
output=df.to_csv('market_data_2002_2025.csv')
