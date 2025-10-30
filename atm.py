import streamlit as st

# Title of the web app
st.title("💳 Python ATM Simulation System")

# Initialize session state variables (to store values between actions)
if "pin" not in st.session_state:
    st.session_state.pin = None
if "balance" not in st.session_state:
    st.session_state.balance = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Create PIN section
st.header("🔐 Create PIN")
new_pin = st.text_input("Create your PIN (4 digits)", type="password")
new_balance = st.number_input("Enter your starting balance (₹)", min_value=0)

if st.button("Create PIN"):
    if len(new_pin) == 4 and new_pin.isdigit():
        st.session_state.pin = new_pin
        st.session_state.balance = new_balance
        st.success("✅ PIN created successfully!")
    else:
        st.error("❌ Please enter a valid 4-digit PIN.")

st.divider()

# Login section
st.header("🔑 Login to Your ATM Account")
entered_pin = st.text_input("Enter your PIN", type="password")

if entered_pin == st.session_state.pin and entered_pin != "":
    st.session_state.logged_in = True
    st.success("Login successful!")
elif entered_pin != "" and entered_pin != st.session_state.pin:
    st.error("Incorrect PIN!")

# Once logged in
if st.session_state.logged_in:
    st.divider()
    st.subheader("🏦 ATM Menu")

    choice = st.selectbox("Choose an operation", [
        "Check Balance",
        "Deposit Money",
        "Withdraw Money",
        "Change PIN",
        "Exit"
    ])

    # Check balance
    if choice == "Check Balance":
        st.info(f"💰 Your current balance is ₹{st.session_state.balance}")

    # Deposit money
    elif choice == "Deposit Money":
        deposit = st.number_input("Enter amount to deposit", min_value=0)
        if st.button("Deposit"):
            st.session_state.balance += deposit
            st.success(f"Deposited ₹{deposit}. New balance: ₹{st.session_state.balance}")

    # Withdraw money
    elif choice == "Withdraw Money":
        withdraw = st.number_input("Enter amount to withdraw", min_value=0)
        if st.button("Withdraw"):
            if withdraw <= st.session_state.balance:
                st.session_state.balance -= withdraw
                st.success(f"Withdrew ₹{withdraw}. Remaining balance: ₹{st.session_state.balance}")
            else:
                st.warning("Insufficient balance!")

    # Change PIN
    elif choice == "Change PIN":
        old_pin = st.text_input("Enter old PIN", type="password")
        new_pin2 = st.text_input("Enter new 4-digit PIN", type="password")
        if st.button("Change PIN"):
            if old_pin == st.session_state.pin and len(new_pin2) == 4 and new_pin2.isdigit():
                st.session_state.pin = new_pin2
                st.success("PIN changed successfully!")
            else:
                st.error("Invalid input or old PIN mismatch!")

    # Exit
    elif choice == "Exit":
        st.session_state.logged_in = False
        st.info("Thank you for using our ATM system 👋")