# 🏦 Bank Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

**A web-based banking application with Streamlit UI built with Python**

</div>

## 📚 Overview

This project is a fully functional Bank Management System implemented in Python. It simulates core banking operations with a user-friendly web-based bStreamlit web interfaceanking application with Streamlit UI, featuring secure account management, transaction processing, and persistent data storage using JSON.

## ✨ Features

### 👤 Account Management
- **Create New Account** - Secure account creation with validation
  - Age verification (18+ required)
  - 4-digit PIN security
  - Unique account number generation
  - Email registration

### 💵 Banking Operations
- **Deposit Money** - Add funds to your account
  - Deposit limit: ₹10,000 per transaction
  - Real-time balance updates
  - Transaction confirmation

- **Withdraw Money** - Secure cash withdrawal
  - Balance verification
  - PIN authentication
  - Instant balance update

- **Check Account Details** - View complete account information
  - Account number
  - Account holder name
  - Current balance
  - Email address

### 🔒 Security Features
- PIN-based authentication for all transactions
- Secure account number generation
- Input validation and error handling

### 💾 Data Persistence
- JSON-based data storage
- Automatic save after each transaction
- Data integrity maintenance

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Libraries:**
  - `json` - Data storage and retrieval
  - `random` - Account number generation
  - `string` - String operations
  - `pathlib` - File path handling
  - `streamlit` - Web UI framework for interactive applications

## 📁 Project Structure

```
BANK_MANAGEMENT/
│
├── app.py              # Main application entry point
├── bank_system.py      # Core banking logic and operations
├── main.py             # Application runner
├── data.json           # User data storage (auto-generated)
└── README.md           # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- Basic understanding of web-based bStreamlit web interfaceanking application with Streamlit UI

### Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/surag29/BANK_MANAGEMENT.git
   cd BANK_MANAGEMENT
   ```

2. **Run the application**
   ```bash
   streamlit run app.py   ```
   python[[](url)](url) app.py[[](url)](url)
   ```[](url)

3. **Follow the on-screen menu:**
   - Create a new account
   - Deposit money
   - Withdraw money
   - Check account details
   - Exit

## 📝 Example Workflow

1. **Create Account** → Enter name, age (18+), email, and 4-digit PIN
2. **Receive Account Number** → Unique alphanumeric account number generated
3. **Deposit Money** → Enter account number, PIN, and amount (max ₹10,000)
4. **Check Balance** → View account details anytime
5. **Withdraw Money** → Enter credentials and amount (subject to balance)

## 📊 Skills Demonstrated

- **Object-Oriented Programming** - Class-based design pattern
- **File I/O Operations** - JSON data handling
- **Data Validation** - Input verification and error handling
- **Security Implementation** - PIN-based authentication
- **User Interface Design** - Interactive CLI menu system
- **Algorithm Design** - Account number generation logic

## 📌 Key Learning Outcomes

✅ Implemented CRUD operations for account management
✅ Designed secure authentication system
✅ Created persistent data storage using JSON
✅ Developed input validation and error handling
✅ Built user-friendly web-based bStreamlit web interfaceanking application with Streamlit UI
✅ Applied Python OOP principles

## 🔮 Future Enhancements

- [ ] Transaction history tracking
- [ ] Fund transfer between accounts
- [ ] Interest calculation
- [ ] Account statement generation
- [ ] Password encryption
- [ ] Database integration (SQLite/PostgreSQL)

## 💬 Feedback & Contributions

This project is part of my learning journey in Python programming and software development. Feedback and suggestions are always welcome!

---

<div align="center">

**Built with ❤️ by [Surag N Devadiga](https://github.com/surag29)**

*Developing practical projects to strengthen programming fundamentals*

</div>
