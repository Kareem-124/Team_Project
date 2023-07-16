
# StockMaster - Inventory Management Web Application®

StockMaster is a powerful web application designed to streamline inventory management for all types of stores, warehouses, and industries. It provides a user-friendly interface for entering product details, tracking expiration dates, and efficiently managing stock levels. With StockMaster, users can effortlessly monitor their inventory, identify products nearing expiration, and easily execute export and import operations.
## Table of Contents

- Features
- Technologies Used
- Installation
- Contributing
- License
- Contact
- Templates of the Application (MVP Version)
- Team Members

## Features
 * User-friendly dashboard highlighting products nearing expiration (within 7 days) and providing a quick overview of the total number of available products.
 * Seamless product entry with comprehensive details, including name, barcode, quantity, expiration date, image, and category.
 * Convenient navbar for effortless navigation to different sections: Dashboard, Enter Products, Export Products, History, and Categories.
 * Effortless export functionality to remove products from the inventory. Barcode scanning enables an automatic population of product details for quick and accurate removal.
 * History page displays a complete log of all export and import movements, allowing easy reference and tracking.
 
## Technologies Used
-   Front-end: HTML, JavaScript, AJAX, Bootstrap
-	Back-end: Python, Django

## Installation
1- Clone the repository:
``` bash
git clone https://github.com/your-username/stockmaster.git
```
2 - Navigate to the project directory:
``` bash
cd stockmaster
```
3- Install the required dependencies:
```
pip install -r requirements.txt
```
4- Set up the database and apply migrations:
```
python manage.py migrate
```
5- Start the development server:
```
python manage.py runserver
```
6- Open your web browser and visit: http://localhost:8000

## Templates of the Application (MVP Version)
1. Dashboard: Displays products nearing expiration and the total number of available products.
2. Enter Products: Allows users to enter product details such as name, barcode, quantity, expiration date, image, and category.
3. Export Products: Enables users to remove products from the inventory by entering the product barcode, which auto-fills its data.
4. History: Displays a log of all export and import movements.
5. Categories: Provides functionality to manage and categorize products.
	
## License
StockMaster is licensed under the MIT License. You are free to use, modify, and distribute the code according to the terms of the license.

## Contact
For any inquiries or further information, please contact the project maintainers at kareem.malhis@outlook.com or //// or //// 

## Project team members:
The StockMaster project is developed and maintained by the following team members:

1. Shatha - Scrum Master
2. Hamada - Back-end / Data Base Developer
3. Kareem - Front-end Developer / UI/UX Designer 
4. Yazan -Back-end / Front-end Developer
We appreciate the collaborative efforts of our team members in creating and improving StockMaster to meet your inventory management needs.
  



