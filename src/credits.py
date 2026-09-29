from storage import load_credits, save_credits

CREDITS_PER_TICKET = 15
FREE_TICKET_COST = 90

class CreditManager:
    def __init__(self):
        self.credits = load_credits()

    def get_balance(self, name):
        return self.credits.get(name, 0)

    def use_free_ticket(self, name):
        balance = self.get_balance(name)
        if balance >= FREE_TICKET_COST:
            self.credits[name] = balance - FREE_TICKET_COST
            save_credits(self.credits)
            return True
        return False

    def add_credits(self, name, paid_tickets):
        earned = paid_tickets * CREDITS_PER_TICKET
        self.credits[name] = self.get_balance(name) + earned
        save_credits(self.credits)
        return earned

    def balance_message(self, name):
        balance = self.get_balance(name)
        if balance < FREE_TICKET_COST:
            return f"You need {FREE_TICKET_COST - balance} more credits for a free ticket."
        return "You have enough credits for a free ticket!"
