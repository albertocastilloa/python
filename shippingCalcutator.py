def cost_ground_shipping(weight):
  flat_charge = 20.00
  premium_flat_charge = 125.00
  price_per_pound = 0.00
  if (weight < 2):
    price_per_pound = 1.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 3.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  
  return (weight * price_per_pound) + flat_charge
  
def cost_drone_shipping(weight):
  flat_charge = 0.00
  price_per_pound = 0.00
  if (weight < 2):
    price_per_pound = 4.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 9.00
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  
  return (weight * price_per_pound) + flat_charge
  
def shipping_cheapest_method(weight):
    ground_shipping = cost_ground_shipping(weight)
    drone_shipping = cost_drone_shipping(weight)
    if ground_shipping < drone_shipping:
        return("Ground shipping is cheapest method and it would cost: %.2f" % (ground_shipping))
    else:
        return("Drone shipping is cheapest method and it would cost: %.2f" % (drone_shipping))

print(shipping_cheapest_method(41.5))