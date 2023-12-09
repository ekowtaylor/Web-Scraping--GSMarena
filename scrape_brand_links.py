from bs4 import BeautifulSoup
import requests
import re


def get_pages(link, link_list):
    html = requests.get(link).content
    soup_page = BeautifulSoup(html, "lxml")
    pages = soup_page.select("div .nav-pages a")
    for page in pages:
        link_list.append("https://www.gsmarena.com/" + page['href'])


url = "https://www.gsmarena.com/makers.php3"
html = requests.get(url).content
soup = BeautifulSoup(html, 'lxml')
td_links = soup.select('tr td a')

brands = []
links = []
counts = []

for anchor in td_links:
    # Get link
    link = "https://www.gsmarena.com/" + anchor['href']
    links.append(link)

    # Todo
    # What's this for?
    #get_pages(link, links)

    # Get brand
    brand = anchor.contents[0]
    brands.append(brand)

    # Get number of devices
    num_devices = int(re.findall('\d+', anchor.text.split('<br>')[-1])[0])
    counts.append(num_devices)

    # Debug
    # print(f"Link: {link}")
    # print(f"Brand: {brand}")
    # print(f"Number of devices: {num_devices}")

    #print(f"{len(link)} brands are done")

with open("brand_links.txt", "w") as f:
    c = 0
    for i in links:
        f.write(f'{brands[c]},{counts[c]},{i}\n')
        c += 1
