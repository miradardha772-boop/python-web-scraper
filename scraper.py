from bs4 import BeautifulSoup
import csv
import requests

# Target webpage for practice
url = "http://quotes.toscrape.com/"

print("Fetching webpage...")
response = requests.get(url)

if response.status_code == 200:
  print("Page fetched! Parsing data...\n")

  soup = BeautifulSoup(response.text, "html.parser")
  quote_boxes = soup.find_all("div", class_="quote")

  scraped_data = []

  for box in quote_boxes:
    text = box.find("span", class_="text").get_text()
    author = box.find("small", class_="author").get_text()

    print(f"Author: {author}")
    print(f"Quote: {text}\n")

    scraped_data.append([author, text])

  # Save to a CSV file inside Pydroid 3
  filename = "quotes.csv"
  with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Author", "Quote"])
    writer.writerows(scraped_data)

  print(f"Success! Saved to {filename}")

else:
  print(f"Failed to fetch page. Status code: {response.status_code}")
