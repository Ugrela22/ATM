# utils.py
import hashlib
import os
from datetime import datetime

def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode()).hexdigest()

def validate_pin(pin: str) -> bool:
    return pin.isdigit() and len(pin) == 4

def validate_name(name: str) -> bool:
    return isinstance(name, str) and len(name.strip()) > 1

def validate_amount(amount: float) -> bool:
    try:
        val = float(amount)
        return val >= 0
    except ValueError:
        return False

def format_currency(amount: float, currency: str = "GEL") -> str:
    return f"{amount:.2f} {currency}"

def get_current_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title: str):
    clear_screen()
    print("=" * 40)
    print(f"{title.center(38)}")
    print("=" * 40)