# ☕ Brew Haven Coffee Shop – Ordering System

A Python project built to replace Brew Haven Coffee Shop's manual, error-prone order-taking process with a fast, accurate digital system. The project was built in **four stages**, each demonstrating a different programming paradigm — from basic scripting through to a graphical desktop app.

## 📋 Problem Background

Brew Haven is a growing coffee shop that was processing customer orders manually, which became slow and inaccurate during busy periods (morning and lunchtime rushes). This system automates the process to:

* Reduce calculation errors
* Speed up service at the till
* Give customers a clear, accurate order summary

**Business rules:**

* Each coffee costs **R35**
* A **10% discount** is applied automatically when a customer orders **10 or more** coffees

## 🧱 Project Structure

|File|Paradigm|Description|
|-|-|-|
|`part1\_basic.py`|Sequential / Basic I/O|Captures a single order, calculates cost and discount, prints a summary|
|`part2\_procedural.py`|Procedural Programming|Same logic broken into reusable functions (`capture\_order`, `calculate\_total`, `display\_receipt`), with a loop to process multiple customers|
|`part3\_oop.py`|Object-Oriented Programming|Introduces an `Order` class encapsulating customer data and behaviour as attributes and methods|
|`part4\_gui.py`|Event-Driven Programming|A Tkinter GUI with **Place Order** and **Exit** buttons, triggering the underlying `Order` logic on click events|

Each stage builds on the last — the design and calculation logic stay consistent while the *way the program is structured* evolves, showing progression from basic scripting to a full desktop application.

## 🛠️ How It Works

1. Cashier enters the customer's name and number of coffees ordered
2. The program calculates:

   * Total cost (quantity × R35)
   * Discount (10% of total, if quantity ≥ 10)
   * Final amount payable
3. An order summary is displayed with all the above details

### Example Output

```
===== ORDER SUMMARY =====
Customer Name   : Xavier
Quantity Ordered: 15
Price per Coffee: R 35
Total Cost       : R 525
Discount         : R 52.5
Amount Payable   : R 472.5
==================================
```

## ▶️ Running the Project

Requires **Python 3** (Part 4 also requires `tkinter`, which is included in the standard Python installation).

```bash
# Part 1 – Basic script
python part1\_basic.py

# Part 2 – Procedural version (loops until you choose to stop)
python part2\_procedural.py

# Part 3 – OOP version
python part3\_oop.py

# Part 4 – GUI version
python part4\_gui.py
```

## 🧠 What This Project Demonstrates

* Problem analysis, IPO charts, algorithms, pseudocode, and flowcharts as planning tools
* Core Python fundamentals: variables, constants, input/output, arithmetic and comparison operators
* Selection (`if`/`else`) and repetition (`while` loops)
* Functions and code reuse (procedural programming)
* Object-oriented design: classes, attributes, and methods
* Event-driven programming with a GUI (Tkinter)

## 👤 Author

Xavier Van Kolver

