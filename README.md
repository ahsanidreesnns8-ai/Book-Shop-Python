# Book-Shop-Python
This is Console Based Book Shop Project with techniques and logics.
# Book Shop Management System 📚

A Python-based retail management script designed for a small-scale bookstore or stationary shop. This project focuses on inventory management, transaction handling, and automated receipt generation using standard Python libraries.

## 🌟 Features

- **Automated Loading Sequence:** Provides a simulated "system start-up" experience using time delays.
- **Dynamic Inventory Catalog:** Features a wide variety of stationary items—from notebooks and textbooks to school bags and calculators—stored efficiently in a Python dictionary.
- **User-Friendly Interface:** - Collects customer details (Name, Phone, Address).
  - Allows users to search for items by name.
  - Supports a 'QUIT' command to finalize the shopping session.
- **Flexible Payment Methods:** - **Cash:** Includes logic to calculate change or request additional funds if the payment is insufficient.
  - **Online:** Provides the shop's account number and verifies transaction status.
- **Automated Discounting:** Automatically applies a **10% discount** to the total bill for all customers.
- **Digital Summary:** Generates a structured summary of the transaction, including the number of items and the final discounted price.

## 🛠️ Technical Concepts

- **Dictionary Mapping:** Efficiently maps item names to their respective prices for $O(1)$ lookup time.
- **Input Handling:** Utilizes `try-except` blocks to manage input errors and ensure program stability.
- **Mathematical Logic:** Implements basic arithmetic for totaling the cart, calculating change, and applying percentages.
- **Time Module:** Uses `time.sleep()` to enhance the command-line interface (CLI) experience.

## 🚀 How to Run

1. **Prerequisites:** Ensure you have Python 3 installed.
2. **Setup:** Save the script as `Book Shop(1st Semester) Project.py`.
3. **Execution:** Run the following command in your terminal:
   ```bash
   python "Book Shop(1st Semester) Project.py"

## Author
M. Ahsan Idrees
