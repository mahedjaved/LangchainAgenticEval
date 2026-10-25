from langchain.tools import tool
from data import users_data
from dotenv import load_dotenv

import logging

from objects import PurchaseItem
from datetime import date

load_dotenv()


@tool
def get_user_purchase_history(user: str) -> dict:
    """
    This tool takes the user username and returns a dict of the user purchase history if the user exists
    """
    logging.info(f"[TOOL:{__name__}]Getting purchase history for user: {user}")
    if users_data.get(user):
        return users_data[user]
    return {"status": f"No user found for {user}"}


@tool
def calculate_right_refund(user: str, items: list[PurchaseItem]) -> str:
    """
    This tool takes a list of the items to be returned and the username and will return how much the refund is worth
    """
    logging.info(f"[TOOL:{__name__}] Calculating refund for user: {user}")
    if users_data.get(user):
        total_refund = 0
        for item in items:
            if users_data[user].get(item.name):
                total_refund += user_data[user][items]["price"]
        return f"The value of the refund is: {total_refund}"
    return {"status": f"No username found for: {user}"}


@tool
def issue_refund_ticket(user: str, refund_amount: int) -> str:
    """
    This tool will send a ticket to the teams to the return the refund. For security we are not returning money as agents go rogue they may misuse this function to transfer money
    """
    logging.info(f"[TOOL:{__name__}] Issuing refund for user: {user}")
    return f"Refund tick has been issued successfully with amount {refund_amountF} for user: {user}"


@tool
def get_today_date(user: str) -> str:
    """
    This tool will return today's date
    """
    logging.info(f"[TOOL:{__name__}] Fetching today's date for user: {user}")
    return date.today()


print(get_user_purchase_history.invoke("user123"))
