''' UI  OF STREAMLIT IMPLEMNTED USING GPT '''


import streamlit as st
from bank_system import Bank

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create Account", "Deposit Money", "Withdraw Money", "Check Details", "Update Details", "Delete Account"]
)

# ----------------------- CREATE ACCOUNT -----------------------
if menu == "Create Account":
    st.header("Create New Bank Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN")
    
    if st.button("Create Account"):
        if pin.isdigit() and len(pin) == 4:
            result = bank.create_account(name, age, email, int(pin))
            st.success(result["msg"])
            st.json(result["account"])
        else:
            st.error("PIN must be 4 digits")

# ----------------------- DEPOSIT -----------------------
elif menu == "Deposit Money":
    st.header("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if pin.isdigit():
            result = bank.deposit(acc, int(pin), amount)
            st.write(result["msg"])
        else:
            st.error("PIN must be numeric")

# ----------------------- WITHDRAW -----------------------
elif menu == "Withdraw Money":
    st.header("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if pin.isdigit():
            result = bank.withdraw(acc, int(pin), amount)
            st.write(result["msg"])
        else:
            st.error("PIN must be numeric")

# ----------------------- CHECK DETAILS -----------------------
elif menu == "Check Details":
    st.header("Check Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Check"):
        if pin.isdigit():
            user = bank.details(acc, int(pin))
            if user:
                st.json(user)
            else:
                st.error("Not found!")
        else:
            st.error("Invalid PIN")

# ----------------------- UPDATE DETAILS -----------------------
elif menu == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        result = bank.update_details(acc, int(pin), new_name, new_email, new_pin)
        st.write(result["msg"])

# ----------------------- DELETE ACCOUNT -----------------------
elif menu == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Delete"):
        result = bank.delete_account(acc, int(pin))
        st.write(result["msg"])
