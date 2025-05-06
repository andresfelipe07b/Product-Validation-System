# 🧮 Product Validation System


This is a small Python script that simulates the total cost of a purchase in a store, including calculation of the subtotal, applied discount, and total to pay. It is intended as a practice tool or a starting point for building a simple Point of Sale (POS) system.

---

## 📌 Features

- Prompts for the product name.
- Properly validates input for:
  - Unit price (must be positive).
  - Quantity (greater than zero).
  - Discount (between 0% and 100%).
- Calculates:
  - Subtotal.
  - Discount amount.
  - Total to pay.
- Displays values formatted as Colombian currency (`COP`).

---

## 🛠️ Technologies Used

- **Language**: Python 3
- **Standard Module**:
  - `locale`: To format values as local currency.

---

## ▶️ How to Run the Program

1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the `.py` file.

```bash
git clone https://github.com/andresfelipe07b/Product-Validation-System
cd Product-Validation-System
```

3. Run the script in the terminal.
4. Follow the on-screen instructions.

---

## 💡 Possible Future Improvements

- [ ] Add support for multiple products in a single run.
- [ ] Include VAT (tax) calculation.
- [ ] Export the information to a `.txt` or `.csv` file.
- [ ] Create a simple graphical interface.
- [ ] Make a web version using Flask or Django.
- [ ] Add sales history per session.
- [ ] Unit tests for calculation functions.

---

## 📷 Example Usage

```
Enter the product name: Shoes
Enter the product price: 120000
Enter the quantity: 2
Enter the discount to apply: 10

======================
Product:          Shoes
Unit Price:       $120,000.00
Quantity:         2.00
Subtotal:         $240,000.00
Discount:         10.0%
Discount Amount:  $24,000.00
-------------------------------
TOTAL TO PAY:     $216,000.00
==============================
```
