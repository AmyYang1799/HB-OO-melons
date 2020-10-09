"""Classes for melon orders."""


class AbstractMelonOrder():
    """An Abstract base class that other Melon Orders inherit from"""


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3


        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = .08

    def __init__(self, species, qty):
        
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.shipped = False

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = .17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    
    order_type = "government"
    tax = 0 

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.passed_inspection = False

    def __repr__(self):
        return f"<Government Melon Order: My species = {self.species}, the quantity = {self.quantity}!"


    def mark_inspection(self):
        """Record the fact than an order has been inspected."""

        self.passed_inspection = True

order66 = GovernmentMelonOrder('cantaloupe', 5)




