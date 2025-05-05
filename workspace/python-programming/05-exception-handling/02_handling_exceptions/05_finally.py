try:
    print("DB Connection successfully")
    print("Transaction 01")
    print(f"Transaction 02: {10/10}")
except Exception:
    print("Transaction failed")
else:
    print("All Transactions were successfully")
finally:
    print("finally block- Closing Connection")