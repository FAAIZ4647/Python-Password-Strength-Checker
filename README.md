# 🔐 Python Password Strength Checker

A simple **Python command-line program** that validates password strength based on common security requirements.

The program checks whether a password contains:

* Minimum length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

If any requirement is missing, the program asks the user to try again.

---

# 📌 Project Overview

This project demonstrates basic **Python validation logic** used in authentication systems.
It continuously prompts the user until a **valid password** is entered.

---

# ⚙️ Features

* Minimum **8 character password requirement**
* Requires **uppercase letter**
* Requires **lowercase letter**
* Requires **number**
* Requires **special character**
* Loop until a valid password is entered
* Clear feedback messages for missing conditions

---

# 🧠 Concepts Used

This project uses several fundamental Python concepts:

* `while` loops
* `for` loops
* conditional statements (`if`, `elif`)
* string methods
* input validation

---

# 📂 Project Structure

```
Python-Password-Strength-Checker
│
├── password_checker.py
└── README.md
```

---

# ▶️ How to Run

### Clone repository

```
git clone https://github.com/FAAIZ4647/Python-Password-Strength-Checker.git
```

### Open project folder

```
cd Python-Password-Strength-Checker
```

### Run the program

```
python password_checker.py
```

---

# 💻 Example Output

```
Enter password: hello

Password should have at least 8 characters

Enter password: Hello123

Please include at least one symbol like @ or #

Enter password: Hello123@

✅ Password accepted
```

---

# 🚀 Future Improvements

Possible upgrades:

* Password strength meter
* GUI version using Tkinter
* Web version using Flask
* Password generator feature
* Hashing and encryption support

---

# 👨‍💻 Author

**A Mohammed Faaiz**

GitHub:
https://github.com/FAAIZ4647

---

# ⭐ Support

If you found this project helpful, consider giving it a **star ⭐ on GitHub**.
