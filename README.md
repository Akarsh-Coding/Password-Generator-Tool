# 🔐 Password Generator Tool (CLI)

## 📌 Project Overview

This **Password Generator Tool** is a **command-line application** developed using **Python** as part of the **RISE (Real‑time Internship & Skill Enhancement)** program by **Tamizhan Skills**.
It allows users to generate strong, customizable, and secure passwords by specifying desired length and optional custom input — offering a simple yet practical approach to improving password security.

---

## 🏁 About RISE

**RISE** is a free, hands-on internship initiative that transforms academic knowledge into practical experience through project-based learning in domains such as:

* 🤖 Artificial Intelligence
* 💻 Web Development
* 📊 Data Science
* 📱 App Development
* 🐍 Python Programming (my chosen domain)
* 🔌 IoT and more
* 🛠️ etc.

---

## 🔧 Project 7: Password Generator Tool (CLI)

### 📝 Problem Statement

Weak and predictable passwords remain one of the top causes of data breaches. Users often reuse or create guessable passwords.

### 🎯 Objective

Build a **Python-based CLI utility** that:

1. Accepts user input for **password length**.
2. Allows **custom strings** to be included.
3. Optionally **save password** to file or clipboard.

---

## 🚀 Features

* ✅ User-defined password length
* ✅ Optional custom string inclusion
* ✅ Randomized mix of:
  * 🅰️ Uppercase and lowercase letters
  * 🔢 Digits
  * 🔣 Special characters
* ✅ Shuffle applied to make passwords unpredictable
* ✅ Colored terminal output using ANSI escape codes (green ✅)
* ✅ Input validation to ensure the password meets user criteria
* ✅ ✂️ Copy to clipboard functionality for quick access
* ✅ Lightweight and fully offline
  
---

## 🧑‍💻 How to Run

1. **Clone or download** this repository.

2. Run the script using:

   ```bash
   python Password-Generator.py
   ```

3. Follow the prompts:

   * Enter your desired password length
   * Optionally include a custom string to embed into the password

---

## 📂 Technologies Used

| Component         | Description                           |
| ----------------- | ------------------------------------- |
| **Python 3.9+**   | Core language                         |
| **random module** | For secure character randomization    |
| **string module** | For accessing built-in character sets |
| **ANSI codes**    | For green terminal output             |

---

## 📊 Expected Outcome

* A secure, strong, and random password with optional customization
* Practice with:

  * `random` and `string` modules
  * List operations and `shuffle()`
  * Input validation and formatting
* A handy utility to demonstrate the real-world application of Python CLI scripts

---

## 📢 Credits

This project is part of the **RISE Internship** by [Tamizhan Skills](https://www.tamizhanskills.com)\
Created by: **Akarsh Kumar**\
Domain: **Python Programming**

---

## 🗂️ Suggested File Structure

```
project_root/
├─ password_generator.py
├─ README.md
```
