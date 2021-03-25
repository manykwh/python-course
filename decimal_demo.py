from decimal import Decimal

# not using string math
product_cost = 88.40
comission_rate = 0.08
qty = 450

product_cost += (comission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal("88.40")
comission_rate = Decimal("0.08")
qty = 450

product_cost += (comission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451 i hope i typed that right

# ------------
# ...

