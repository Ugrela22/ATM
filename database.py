# database.py
import json
import os
from typing import List, Dict, Any
from utils import hash_pin, get_current_timestamp

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.json")
ATM_FILE = os.path.join(DATA_DIR, "atm.json")

def initialize_database():
    """Create data directory and JSON files with default data if they don't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    # Initialize users.json
    if not os.path.exists(USERS_FILE):
        default_users = [
            {
                "unique_id": "U-000001",
                "full_name": "Test User",
                "pin_hash": hash_pin("1111"),
                "balance": 5000.00,
                "is_locked": False,
                "wrong_attempts": 0,
                "created_at": get_current_timestamp()
            }
        ]
        save_users(default_users)
    
    # Initialize transactions.json
    if not os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'w') as f:
            json.dump([], f, indent=2)
    
    # Initialize atm.json
    if not os.path.exists(ATM_FILE):
        default_atm = {
            "cash_balance": 100000.00,
            "currency": "GEL",
            "last_refill": get_current_timestamp()
        }
        save_atm_data(default_atm)

def load_users() -> List[Dict[str, Any]]:
    """Load all users from JSON file."""
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        initialize_database()
        with open(USERS_FILE, 'r') as f:
            return json.load(f)

def save_users(users: List[Dict[str, Any]]):
    """Save users list to JSON file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def load_transactions() -> List[Dict[str, Any]]:
    """Load all transactions from JSON file."""
    try:
        with open(TRANSACTIONS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transaction(transaction: Dict[str, Any]):
    """Append a new transaction to JSON file."""
    transactions = load_transactions()
    transactions.append(transaction)
    with open(TRANSACTIONS_FILE, 'w') as f:
        json.dump(transactions, f, indent=2)

def load_atm_data() -> Dict[str, Any]:
    """Load ATM data from JSON file."""
    try:
        with open(ATM_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        initialize_database()
        with open(ATM_FILE, 'r') as f:
            return json.load(f)

def save_atm_data(data: Dict[str, Any]):
    """Save ATM data to JSON file."""
    with open(ATM_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def generate_user_id() -> str:
    """Generate next sequential user ID."""
    users = load_users()
    if not users:
        return "U-000001"
    
    max_num = 0
    for user in users:
        try:
            num = int(user['unique_id'].split('-')[1])
            max_num = max(max_num, num)
        except (IndexError, ValueError):
            continue
    
    return f"U-{str(max_num + 1).zfill(6)}"

def generate_transaction_id() -> str:
    """Generate next sequential transaction ID."""
    transactions = load_transactions()
    if not transactions:
        return "T-000001"
    
    max_num = 0
    for trans in transactions:
        try:
            num = int(trans['transaction_id'].split('-')[1])
            max_num = max(max_num, num)
        except (IndexError, ValueError):
            continue
    
    return f"T-{str(max_num + 1).zfill(6)}"

def get_user_by_id(user_id: str) -> Dict[str, Any] | None:
    """Find and return user by ID."""
    users = load_users()
    for user in users:
        if user['unique_id'] == user_id:
            return user
    return None

def update_user(updated_user: Dict[str, Any]):
    """Update a specific user in the database."""
    users = load_users()
    for i, user in enumerate(users):
        if user['unique_id'] == updated_user['unique_id']:
            users[i] = updated_user
            save_users(users)
            return True
    return False

def delete_user_by_id(user_id: str) -> bool:
    """Delete a user from the database."""
    users = load_users()
    users = [u for u in users if u['unique_id'] != user_id]
    save_users(users)
    return True
