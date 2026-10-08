resources = [
    {"id" : "R001", "name" : "Laptop", "category" : "electronics", "total" : 10, "available" : 10},
    {"id" : "R002", "name" : "Keyboard", "category" : "electronics", "total" : 5, "available" : 5},
    {"id" : "R003", "name" : "Headset", "category" : "electronics", "total" : 3, "available" : 3}


]

fellows = {
    "F001" : "Ada",
    "F002" : "John",
    "F003" : "Grace"
}

borrow_records = []



def list_items():
    print("\n--- Current Inventory ---")
    for item in resources:
        print(f"ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Total: {item['total']} | Available: {item['available']}")


def add_item(item_id, name, category, total):
    for item in resources:
        if item['id'] == item_id:
            print("ERROR: This ID already exists!")
            return False
 
    new_item = {
        "id": item_id,
        "name": name,
        "category": category,
        "total": int(total),
        "available": int(total) 
    }
    
    resources.append(new_item)
    print("SUCCESSFUL: Item added to inventory.")
    return True

def search_items(search_name, filter_category):
    print("\n Search Results")

    clean_search = search_name.lower().strip()
    clean_category = filter_category.lower().strip()

    for item in resources:
        name_match = True
        if clean_search != "":
            if clean_search not in item["name"].lower():
                name_match = False

        # category_match = True
        # if clean_search != "":
        #     if clean_search != item[""].lower():
        #         category_match = False

        category_match = True
        if clean_category != "":
            if clean_category != item["category"].lower():
                category_match = False

        if name_match == True and category_match == True:
            print(f"ID: {item['id']} | Name: {item['name']} | Category: {item['category']} | Total:{item['total']} | Available: {item['available']}")


def borrow_item(fellow_id, item_id, quantity):
    """Handles checking out items to fellows."""
    f_id = fellow_id.strip().upper()
    i_id = item_id.strip().upper()
    
    if f_id not in fellows:
        print("ERROR: Fellow ID not found!")
        return False
        
    if quantity <= 0:
        print("ERROR: Quantity must be greater than zero")
        return False

    target_item = None
    for item in resources:
        if item["id"] == i_id:
            target_item = item
            break
            
    if target_item is None:
        print("ERROR: Item ID not found!")
        return False
        
    if quantity > target_item["available"]:
        print("ERROR: Not enough stock available")
        return False
        
    target_item["available"] -= quantity  
    new_record = {
        "fellow_id": f_id,
        "item_id": i_id,
        "quantity": quantity
    }
    borrow_records.append(new_record)
    
    print(f"SUCCESSFUL: {fellows[f_id]} borrowed {quantity} {target_item['name']}(s).")
    return True


def return_item(fellow_id, item_id, quantity):
    f_id = fellow_id.strip().upper()
    i_id = item_id.strip().upper()

    if quantity <= 0:
        print("Error")
        return False

    borrowed_quantity = 0
    for record in borrow_records:
        if record["fellow_id"] == f_id and record["item_id"] == i_id:
            borrowed_quantity += record["quantity"]

    if quantity > borrowed_quantity:
        print("Error, request is more than what you have")
        return False

    for item in resources:
        if item["id"] == i_id:
            item["available"] += quantity
            break

    return_record = {
        "fellow_id": f_id,
        "item_id": i_id,
        "quantity": -quantity  
    }
    borrow_records.append(return_record)

    print(f"SUCCESSFUL: Returned {quantity} unit(s) successfully.")
    return True


def generate_report():
    total_inventory_units = 0
    total_available_units = 0
    total_borrowed_units = 0
    low_stock_items = []
    most_borrowed_qty = -1
    most_borrowed_leaders = []

    for item in resources:
        total_inventory_units += item["total"]
        total_available_units += item["available"]
        
        current_item_borrowed = item["total"] - item["available"]
        total_borrowed_units += current_item_borrowed

        if item["available"] < 3:
            low_stock_items.append(f"{item['name']} ({item['available']})")

        if current_item_borrowed > most_borrowed_qty:
            most_borrowed_qty = current_item_borrowed
            most_borrowed_leaders = [item["name"]]
        elif current_item_borrowed == most_borrowed_qty and current_item_borrowed > 0:
            most_borrowed_leaders.append(item["name"])

    print("\nCAMPUS SYSTEM REPORT")
    print(f"Overall Units in Inventory : {total_inventory_units}")
    print(f"Available Units on Shelf   : {total_available_units}")
    print(f"Units Currently Borrowed   : {total_borrowed_units}")
    
    if low_stock_items:
        print(f"Low Stock Items (<3)       : {', '.join(low_stock_items)}")
    else:
        print("Low Stock Items (<3)       : None")
        
    if most_borrowed_qty > 0:
        leaders_str = ", ".join(most_borrowed_leaders)
        print(f"Most Borrowed Resource     : {leaders_str} ({most_borrowed_qty} borrowed)")
    else:
        print("Most Borrowed Resource     : No items are currently borrowed")
    print("Nice Job!")


def main_menu():
    while True:
        print("\nWelcome to Campus Resource Management System")
        print("1. List All Items")
        print("2. Add New Item")
        print("3. Search/Filter Items")
        print("4. Borrow an Item")
        print("5. Return an Item")
        print("6. Generate Report")
        print("7. Exit System")
        
        choice = input("select one option: ").strip()
        
        if choice == "1":
            list_items()
            
        elif choice == "2":
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            category = input("Enter Item Category: ")
            total_input = input("Enter Total Units: ")
            
            if total_input.isdigit():
                add_item(item_id, name, category, int(total_input))
            else:
                print("Error: Total units must be a valid number.")
                
        elif choice == "3":
            search_name = input("Enter name to search")
            filter_category = input("Enter category to filter")
            search_items(search_name, filter_category)
            
        elif choice == "4":
            fellow_id = input("Enter Fellow ID: ")
            item_id = input("Enter Item ID: ")
            qty_input = input("Enter Quantity to Borrow: ")
            
            if qty_input.isdigit():
                borrow_item(fellow_id, item_id, int(qty_input))
            else:
                print("Error: Quantity must be a valid number.")
                
        elif choice == "5":
            fellow_id = input("Enter Fellow ID: ")
            item_id = input("Enter Item ID: ")
            qty_input = input("Enter Quantity to Return: ")
            
            if qty_input.isdigit():
                return_item(fellow_id, item_id, int(qty_input))
            else:
                print("Error: Quantity must be a valid number.")
                
        elif choice == "6":
            generate_report()
            
        elif choice == "7":
            print("Exiting system. Goodbye!")
            break
            
        else:
            print("Invalid selection!")
main_menu()
