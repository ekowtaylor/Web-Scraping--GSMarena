from bs4 import BeautifulSoup
import requests

# Init lists
brand_links = []

# Read file into lists
with open("brand_links.txt", "r") as f:
    lines = f.readlines()[0:2]  # len(f.readlines())
    for line in lines:
        print(f"Item:{line}")
        brand_links.append(line.strip())

i = 0
phone_brand = []
phone_links = []
for link in brand_links:
    html = requests.get(link.split(",")[2]).content
    print(html)
    soup = BeautifulSoup(html, 'lxml')
    phone_tags = soup.select('div.makers ul li a')
    for phone in phone_tags:
        phone_link = "https://www.gsmarena.com/" + phone['href']
        phone_brand.append(link.split(",")[0])
        phone_links.append(phone_link)
    i = i + 1
    print(f"{i} links are done")

# Write results to file
with open("phone_links.txt", "w") as f:
    j = 0
    for i in phone_links:
        f.write(f'{phone_brand[j]},{i}\n')
        j += 1
