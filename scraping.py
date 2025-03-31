from bs4 import BeautifulSoup
import os 
import pandas as pd

d = {'title' : [], 'price' : [], 'link' : []}

for file in os.listdir("data"):
    try: 
        with open(f"data/{file}")as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc,"html.parser")
            t =soup.find("h2")
            title = t.getText()

            p = soup.find("span",attrs={"class": "a-price-whole"})
            price = p.get_text()
            
            # Extract product link - search for <a> tag inside product container
            a_tag = soup.find("a", class_="a-link-normal", href=True)
            link = "https://www.amazon.in" + a_tag['href'] if a_tag else "N/A"

            # Print extracted data
            print(f"Title: {title}\nPrice: {price}\nLink: {link}\n")

            d["title"].append(title)
            d["price"].append(price)
            d["link"].append(link)

    except Exception as e:
        print(e)

# Convert data to DataFrame and save to CSV
df = pd.DataFrame(data=d)
df.to_csv("Scrapped_data.csv")
print("\nData saved to data_csv.csv")