# transaction.py
from typing import Optional
from database import generate_transaction_id
from utils import get_current_timestamp

class Transaction:
    """Represents a single transaction in the ATM system."""
    
    def __init__(self, user_id: str, trans_type: str, amount: float, 
                 currency: str = "GEL", target_user_id: Optional[str] = None):
        """
        Initialize a transaction.
        
        Args:
            user_id: ID of the user making the transaction
            trans_type: Type of transaction (deposit, withdraw, transfer)
            amount: Transaction amount
            currency: Currency type (default GEL)
            target_user_id: Target user ID for transfers (optional)
        """
        self.transaction_id = generate_transaction_id()
        self.user_id = user_id
        self.type = trans_type
        self.amount = amount
        self.currency = currency
        self.timestamp = get_current_timestamp()
        self.target_user_id = target_user_id
        self.status = "completed"
    
    def to_dict(self) -> dict:
        """Convert transaction to dictionary for JSON storage."""
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "type": self.type,
            "amount": self.amount,
            "currency": self.currency,
            "timestamp": self.timestamp,
            "target_user_id": self.target_user_id,
            "status": self.status
        }
