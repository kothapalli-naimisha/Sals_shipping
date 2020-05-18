def ground_shipping(weight):
  if weight <= 2:
    price = 1.50
  elif weight < 6:
    price = 3.00
  elif weight <= 10:
    price = 4.00 
  else:
    price = 4.75
  return (price * weight) + 20 
premium_shipping = 125
def drone_shipping(weight):
  if weight <= 2:
    price = 4.50
  elif weight < 6:
    price = 9.00
  elif weight <= 10:
    price = 12.00 
  else:
    price = 14.25
  return price *weight
def cheapest_shipping(weight):
  premium = premium_shipping 
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if (premium < drone) and (premium < ground):
    return ("Premium shipping is the cheapest ",premium)
  elif (drone < premium) and (drone < ground):
    return ("Drone shipping is the cheapest ",drone)
  else:
    return ("Ground shipping is the cheapest ",ground)

print(cheapest_shipping(4.8))

print(cheapest_shipping(42.5))










