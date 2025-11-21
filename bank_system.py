''' CODE IMPROVISED BY GPT '''


import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load existing data or create a new file
    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        print(f"Error loading database: {err}")
        data = []

    # Update JSON file
    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    # Account Number Generator
    @classmethod
    def __account_generate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        special = random.choice("!@#$%^&*")
        acc = alpha + num + [special]
        random.shuffle(acc)
        return "".join(acc)

    # Create Account
    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return {"status": False, "msg": "Age must be 18+, PIN must be 4 digits"}

        acc_no = self.__account_generate()
        new_user = {
            "NAME": name,
            "AGE": age,
            "EMAIL": email,
            "PIN": pin,
            "ACCOUNTNO": acc_no,
            "BALANCE": 0
        }

        Bank.data.append(new_user)
        Bank.__update()

        return {"status": True, "msg": "Account created successfully", "account": new_user}

    # Deposit Money
    def deposit(self, acc, pin, amount):
        user = next((u for u in Bank.data if u["ACCOUNTNO"] == acc and u["PIN"] == pin), None)

        if user is None:
            return {"status": False, "msg": "Account not found!"}

        if amount > 10000:
            return {"status": False, "msg": "Deposit limit is 10,000"}

        user["BALANCE"] += amount
        Bank.__update()

        return {"status": True, "msg": "Amount deposited!", "balance": user["BALANCE"]}

    # Withdraw Money
    def withdraw(self, acc, pin, amount):
        user = next((u for u in Bank.data if u["ACCOUNTNO"] == acc and u["PIN"] == pin), None)

        if user is None:
            return {"status": False, "msg": "Account not found!"}

        if user["BALANCE"] < amount:
            return {"status": False, "msg": "Insufficient balance"}

        user["BALANCE"] -= amount
        Bank.__update()

        return {"status": True, "msg": "Withdrawal successful!", "balance": user["BALANCE"]}

    # Check Details
    def details(self, acc, pin):
        user = next((u for u in Bank.data if u["ACCOUNTNO"] == acc and u["PIN"] == pin), None)

        if not user:
            return None
        return user

    # Update User Details
    def update_details(self, acc, pin, new_name, new_email, new_pin):
        user = next((u for u in Bank.data if u["ACCOUNTNO"] == acc and u["PIN"] == pin), None)

        if not user:
            return {"status": False, "msg": "Account not found"}

        if new_name:
            user["NAME"] = new_name
        if new_email:
            user["EMAIL"] = new_email
        if new_pin:
            if len(str(new_pin)) == 4:
                user["PIN"] = int(new_pin)
            else:
                return {"status": False, "msg": "PIN must be 4 digits"}

        Bank.__update()
        return {"status": True, "msg": "Details updated successfully"}

    # Delete Account
    def delete_account(self, acc, pin):
        user = next((u for u in Bank.data if u["ACCOUNTNO"] == acc and u["PIN"] == pin), None)

        if not user:
            return {"status": False, "msg": "Account not found"}

        Bank.data.remove(user)
        Bank.__update()

        return {"status": True, "msg": "Account deleted successfully"}
