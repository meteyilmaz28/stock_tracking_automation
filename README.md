![image](https://github.com/user-attachments/assets/6f88aae7-66cf-4246-8aad-ac4c6804d920)

Inventory Tracking Application (PyQt5)
This project is a PyQt5-based inventory tracking application. The application is used to track the brand, model, and quantity of products, and stores the data in an Excel file.

Features
Add, delete, and list products
Color-coding of products by brand (e.g., Honda in green, Kawasaki in red)
Rows for products with stock quantities below 10,000 are highlighted in light red
Product information is loaded from and saved to the brands_and_categories.json file
Installation
Requirements:

Python 3.x
PyQt5
openpyxl

Install dependencies:

pip install PyQt5 openpyxl

Clone the project:
git clone [https://github.com/meteyilmaz28/stock_tracking_automation.git](https://github.com/meteyilmaz28/stock_tracking_automation.git)
cd inventory-tracking
Run the application:

python main.py

Usage
Add Product: Enter the brand, model, and quantity, then click the "Add Product" button.
List Products: View the list of current products. Different brands are displayed in their respective colors.
Delete Product: Select the product you wish to delete and click the "Delete" button.
Files
main.py: The main file of the application
brands_and_categories.json: The file containing brand and category data
README.md: This file

Contributing
Contributions are welcome. Please create a pull request or open an issue.
