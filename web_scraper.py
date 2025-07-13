import requests
from bs4 import BeautifulSoup
import csv

# ✅ Target URL: Meesho's product search page
url = "https://www.meesho.com/search?q=dress"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# CSV file setup
with open("meesho_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])  # headers

    # Find all products (customize selector as per site structure)
    for product in soup.find_all("div", class_="Card__base"):
        name = product.find("p", class_="Text__title").get_text(strip=True) if product.find("p", class_="Text__title") else "N/A"
        price = product.find("span", class_="Text__price").get_text(strip=True) if product.find("span", class_="Text__price") else "N/A"
        rating = product.find("span", class_="Text__rating").get_text(strip=True) if product.find("span", class_="Text__rating") else "N/A"
        writer.writerow([name, price, rating])

print("✅ Data saved to meesho_products.csv")
