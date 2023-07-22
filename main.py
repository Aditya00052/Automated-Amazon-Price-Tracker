import requests
from bs4 import BeautifulSoup
import smtplib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

product_link = "https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-A30900J-10P/dp/B08ZL6XD9H/ref=sr_1_1_sspa?crid=S2HS8NLJYMLD&keywords=3090&qid=1661844350&sprefix=3090%2Caps%2C368&sr=8-1-spons&psc=1"

response = requests.get(url=product_link,
                        headers=headers)
product_page = response.text

soup = BeautifulSoup(product_page, "html.parser")
# print(soup.prettify())

product_price_txt = (soup.find(name="span", class_="a-price-whole")).getText()
product_price2 = product_price_txt.replace(",", "")
product_price = product_price2.replace(".", "")

print(product_price)

my_email = "your_email"
password_ = "your_pass"

if int(product_price) < 1100:

    connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    connection.login(user=my_email, password=password_)
    connection.sendmail(from_addr=my_email,
                        to_addrs="reciever's_email",
                        msg=f"Subject: Price drop on 3090\n\nZOTAC Gaming GeForce RTX 3090 Trinity OC 24GB GDDR6X 384-bit 19.5 Gbps PCIE 4.0 Gaming Graphics Card is now ${product_price_txt}\n{product_link}")
    connection.close()

