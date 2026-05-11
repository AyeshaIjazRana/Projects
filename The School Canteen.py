def dic_menu():
    print("Welcome to the Canteen!")
    items = {
        "Samosa":30,
        "Chicken Roll":50,
        "Shawarma":100,
        "Burger":150,
        "Juice":20,
        "Water":10
    }
    return items

def show_menu(items):
    print("MENU:")
    for num, (item, price) in enumerate(items.items(), 1):
        print(f"{num}. {item} Rs. {price}")
def is_valid_item(item, items):
    return item.title() in items


def cart_total(order, items):
    total = sum(quantity * items[item] for item, quantity in order.items())
    return total

def take_order(student_name, items):
    show_menu(items)
    order = {}
    while True:
        item = input("Enter the item you want to order or 'done': ")
        if item.lower() == 'done':
            break
        if is_valid_item(item, items):
            try:
                quantity = int(input(f"Enter the quantity of {item}: "))
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                continue
            item_title = item.title()
            order[item_title] = order.get(item_title, 0) + quantity
            total = cart_total(order, items)
            if total > 500:
                print(f"Budget limit reached! Your total is Rs. {total}. Please remove an item.")
                while cart_total(order, items) > 500:
                    del_item = input("Enter the item you want to remove: ").strip()
                    if del_item.title() in order:
                        del order[del_item.title()]
                        new_total = cart_total(order, items)
                        print(f"Item removed. New total: Rs. {new_total}")
                    else:
                        print("Item not in order. Please try again.")
        else:
            print("Invalid item. Please try again.")
    return order

items = dic_menu()

data = []
name = input("Enter the first student's name: ")
order = take_order(name, items)
total = cart_total(order, items)
print(f"{name}'s Cart: {order}")
print(f"Total: Rs. {total}")
data.append((name, order, total))

while True:
    response = input("Next student? (yes/no): ").lower()
    if response == "yes":
        name = input("Enter student name: ")
        order = take_order(name, items)
        total = cart_total(order, items)
        print(f"{name}'s Cart: {order}")
        print(f"Total: Rs. {total}")
        data.append((name, order, total))
    elif response == "no":
        break
    else:
        print("Enter valid response.")

def daily_report(data):
    if not data:
        print("No student data available.")
        return
    
    print("DAILY REPORT")
    
    total_revenue = sum(total for _, _, total in data)
    print(f"Total Revenue Collected: Rs. {total_revenue}")
    print(f"Number of Students Served: {len(data)}")
    
    max_spender = max(data, key=lambda x: x[2])
    print(f"Student who spent the most: {max_spender[0]} (Rs. {max_spender[2]})")
    
    item_counts = {}
    for _, cart, _ in data:
        for item, quantity in cart.items():
            item_counts[item] = item_counts.get(item, 0) + quantity
    
    if item_counts:
        max_count = max(item_counts.values())
        most_popular = [item for item, count in item_counts.items() if count == max_count]
        print(f"Most popular item(s): {', '.join(most_popular)}")
    else:
        print("Most popular item(s): None")
    
    big_spenders = [name for name, cart, _ in data if len(cart) >= 4]
    if big_spenders:
        print(f"Big Spenders (4+ different items): {', '.join(big_spenders)}")
    else:
        print("Big Spenders (4+ different items): None")
    
    print("DETAILED STUDENT REPORT")
    for name, cart, total in data:
        print(f"Student: {name}")
        print(f"  Items: {cart}")
        print(f"  Total: Rs. {total}")

daily_report(data)
