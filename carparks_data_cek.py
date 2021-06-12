import requests
from bs4 import BeautifulSoup
import psycopg2
con = psycopg2.connect(database="parking-system", user="postgres", password="Sinem12345", host="127.0.0.1", port="5432")

URL = 'https://www.bulurum.com/dir/otoparklar/ankara/'

#URL = 'https://yandex.com.tr/harita/104782/cankaya/search/Otoparklar/?ll=32.852151%2C39.922858&sll=32.852151%2C39.922858&sspn=0.003412%2C0.002619&z=15'
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'html.parser')

carparks_html = soup.select('div.ResultsMain')
#['1.html', '2.html']
#print(carparks_html)


for carpark_html in carparks_html:
    address = carpark_html.select_one('div.FreeListingAddress').text
    park_name =carpark_html.select_one('div.CompanyName h2 a span').text
    phone = carpark_html.select_one('div.DetailsText').text
    district_name = ''
    open_until = ''
    image = ''
    latitude = ''
    longitude = ''
    slug = park_name
    print(address)
    print(park_name)
    print(phone)
    cur = con.cursor()

    sql = f"""INSERT INTO carparks_carparks(park_name , phone , district_name , address , open_until , image , latitude , longitude ,slug)
       VALUES('{park_name}','{phone}', '{district_name}', '{address}','{open_until}','{image}','{latitude}','{longitude}','{slug}')"""
    cur.execute(sql);
    con.commit()

    #TRUNCATE carparks_carparks