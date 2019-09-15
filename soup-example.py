import bs4
import requests

res = requests.get('https://www.amazon.com/dp/B072YZP97P')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('#price_inside_buybox')
print(elems[0].text.strip())
