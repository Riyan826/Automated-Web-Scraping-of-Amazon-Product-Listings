# Amazon Product Scraper

## 📌 Overview
This project is an **automated web scraper** that extracts product details (titles, prices, and links) from **Amazon India** using **Selenium and BeautifulSoup**. The extracted data is saved into a CSV file for further analysis.

## 🚀 Features
- **Automates product data extraction** from Amazon
- **Handles multiple pages** with pagination support
- **Extracts clean and structured data** (title, price, product link)
- **Stores the extracted data in a CSV file** for further use
- **Handles exceptions and errors** for a smooth scraping experience

## 🛠️ Technologies Used
- **Python**
- **Selenium** (for web automation)
- **BeautifulSoup** (for HTML parsing)
- **Pandas** (for data storage and processing)
- **CSV** (to save extracted data)

## 📂 Project Structure
```
├── data/               # Folder to store extracted HTML files
├── collect.py          # Script to process and extract data from saved HTML files
├── project.py          # Main script for web scraping
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/riyan826/amazon-product-scraper.git
cd amazon-product-scraper
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run:
```sh
pip install -r requirements.txt
```

### 3️⃣ Download and Set Up WebDriver
Make sure you have **Google Chrome** installed and download the matching **ChromeDriver** from [here](https://chromedriver.chromium.org/downloads). Place it in your project directory.

## 🚀 Usage
### **Run the Web Scraper**
Execute the following command to scrape Amazon product data:
```sh
python project.py
```
This will scrape product details and save HTML files in the `data/` folder.

### **Extract Data from Saved Pages**
Once HTML files are saved, extract relevant details using:
```sh
python collect.py
```
This will generate a **CSV file** (`data_csv.csv`) containing the product details.

## ⚠️ Disclaimer
- This project is **for educational purposes only**.
- Scraping Amazon may violate its **terms of service**. Use responsibly.
- To avoid getting blocked, **limit the request frequency** (e.g., add `time.sleep(5)`).

## 📌 Future Improvements
- Implement **headless browsing** for better efficiency
- Add **proxy rotation** to avoid getting blocked
- Store data in a **database** instead of CSV
