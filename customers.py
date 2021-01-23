"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __repr__(self):
        """Convenience method to show info about customer"""

        return f"<Customer: {self.first_name} {self.last_name}, email: {email}"

def read_customers_from_file(filepath):
    """Read customer data from file & populate dictionary of customers

    Dictionary will be {email: customer()}
    """

    customer_info = {}

    with open(filepath) as file:
        for line in file:
            (first_name,
            last_name,
            email,
            password) = line.strip().split('|')

            customer_info[email] = Customer(first_name,
                                            last_name,
                                            email,
                                            password)
    
    return customer_info

def get_by_email(email):
    """Returns a customer given an email"""
    
    return customer_info[email]



customer_info = read_customers_from_file("customers.txt")