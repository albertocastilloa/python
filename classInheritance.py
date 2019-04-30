class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self, product):
    print("I'm a string that stands in for the contents of your shopping cart!")
    self.product = product

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart("iPad")
monty_python.display_order_history()
print(monty_python.customer_id)
print(monty_python.product)