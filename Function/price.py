def apply_discount(item_name, price, promo_code):

    if promo_code == "SAVE10":
        discounted_price = price - (price * 0.10)

    elif promo_code == "HALFOFF":
        discounted_price = price - (price * 0.50)

    else:
        discounted_price = price

    return discounted_price


item_name = input("Enter item name: ")
price = float(input("Enter price: "))
promo_code = input("Enter promo code: ")

final_price = apply_discount(item_name, price, promo_code)

print(item_name, "final price is:", final_price)
