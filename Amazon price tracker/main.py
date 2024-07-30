from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

url = "https://www.amazon.in/Instant-Essential-Stainless-Electric-Pressure/dp/B0BWV446TD/ref=sr_1_4"
load_dotenv()
reciever = "vishwasferwani2002@gmail.com"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url=url,headers=header)
data = response.text

soup = BeautifulSoup(data,"html.parser")
# print(soup.prettify())
title = soup.find(id="productTitle").getText()
# print(title)
price_whole = soup.find("span",class_="a-price-whole").get_text().replace(',','')
# price_fraction = soup.find("span",class_="a-price-fraction").get_text()
price = float(price_whole)
# print(price)
message = f"{title} is on sale for {price}!"
# print(message)
if price<21000:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["my_email"], password=os.environ["password"])
        connection.sendmail(from_addr=os.environ["my_email"], to_addrs=reciever, msg=f"Subject:AMAZON PRICE ALERT\n\n{message}\n{url}".encode("utf-8"))
