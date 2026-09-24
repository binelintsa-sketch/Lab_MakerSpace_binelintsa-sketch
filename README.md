# Campus MakerSpace Checkout System

A command-line interface (CLI) application built with Python and SQLite to manage equipment inventory, member registration, and checkout/return workflows for a campus MakerSpace.

---

## 📌 Project Overview

The **Campus MakerSpace Checkout System** is a tool that simplifies equipment management by providing a persistent database layer paired with an Object-Oriented Programming (OOP) model. It allows admins to register members, list available inventory, process item checkouts, and handle equipment returns cleanly through an interactive terminal menu.

---

## 📁 Repository Structure

```text
Lab_MakerSpace_binelintsa-sketch/
├── database.py       # SQLite connection setup and schema creation
├── models.py         # OOP classes (Member, Equipment, Loan) with DB operations
├── main.py           # CLI menu loop and application logic
├── makerspace.db     # Generated SQLite database file
└── README.md         # Project documentation

## 🛠️ Features & Technical Stack

* **Language:** Python 3.14
* **Database:** SQLite3 (with Foreign Key constraints enabled)
* **Architecture:** Object-Oriented Design (Class-based models interfacing with SQLite)
* **Key Features:**
  * Interactive CLI terminal interface for MakerSpace administration
  * Member registration and listing
  * Equipment inventory tracking with real-time availability status (`1` for available, `0` for checked out)
  * Checkout and return tracking with timestamp logging
  * Relational integrity enforced via SQLite foreign key constraints (`ON DELETE CASCADE`)



## 📌 Overview

The **Campus MakerSpace Checkout System** is a Python CLI application backed by SQLite that manages equipment loans and member registrations.

### Project Architecture
* `database.py`: Handles SQLite database initialization and table schema setup.
* `models.py`: OOP domain models (`Member`, `Equipment`, `Loan`) encapsulating CRUD and checkout logic.
* `main.py`: Interactive CLI menu loop interfacing with domain models.
* `makerspace.db`: SQLite database file storing persistent records.

## 🗄️ Database Schema

* **`members`**: `member_id` (PK), `name`, `email` (UNIQUE), `phone`
* **`equipment`**: `equipment_id` (PK), `name`, `categorie`, `is_available` (0/1)

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed

### How to Run

1. **Clone the repository:**
   *git clone [https://github.com/binelintsa-sketch/Lab_MakerSpace_binelintsa-sketch.git](https://github.com/binelintsa-sketch/Lab_MakerSpace_binelintsa-sketch.git)
   cd Lab_MakerSpace_binelintsa-sketch
2. Run the main script using Python:
   python main.py
  
##AI Tools Used: Google Gemini.

#Scope of Assistance:

*Debugging Python runtime errors (parameter ordering in __init__).

*Resolving SQLite schema conflicts (synchronizing category column across queries).

*Explaining OOP-to-database interaction patterns (mapping raw SQL tuples to model instances).

   ## ✍️ Author

* **Developer:** Ntsa Bineli
* **Repository:** `Lab_MakerSpace_binelintsa-sketch`