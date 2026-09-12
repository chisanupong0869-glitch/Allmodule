# ==========================================
# MODULE 1: Logger
# ==========================================
def log(message):
    print(f"[LOG]: {message}")

# ==========================================
# MODULE 2: Database
# ==========================================
DB = {
    "users": {"admin": "1234"},
    "products": {
        "P01": {"name": "Laptop", "price": 25000, "stock": 5},
        "P02": {"name": "Mouse", "price": 500, "stock": 20}
    }
}

# ==========================================
# MODULE 3: Auth
# ==========================================
def authenticate(username, password):
    return DB["users"].get(username) == password

# ==========================================
# MODULE 4: Product
# ==========================================
def get_product(prod_id):
    return DB["products"].get(prod_id)

# ==========================================
# MODULE 5: Inventory
# ==========================================
def update_stock(prod_id, quantity):
    if prod_id in DB["products"]:
        DB["products"][prod_id]["stock"] -= quantity
        return True
    return False

# ==========================================
# MODULE 6: Cart
# ==========================================
class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, qty):
        self.items.append({"product": product, "qty": qty})

    def get_total(self):
        return sum(item["product"]["price"] * item["qty"] for item in self.items)

# ==========================================
# MODULE 7: Discount
# ==========================================
def apply_discount(total_amount, code):
    if code == "SAVE10":
        return total_amount * 0.90
    return total_amount

# ==========================================
# MODULE 8: Payment
# ==========================================
def process_payment(amount, method="Credit Card"):
    print(f"ชำระเงินจำนวน {amount:,.2f} บาท ผ่าน {method} สำเร็จ!")
    return True

# ==========================================
# MODULE 9: Receipt
# ==========================================
def print_receipt(cart, final_amount):
    print("\n--- ใบเสร็จรับเงิน ---")
    for item in cart.items:
        p = item["product"]
        print(f"- {p['name']} x {item['qty']} = {p['price'] * item['qty']:,} บาท")
    print(f"ราคาสุดธิ: {final_amount:,.2f} บาท")
    print("----------------------")

# ==========================================
# MODULE 10: Analytics
# ==========================================
def report_sale(total_sales):
    print(f"[ANALYTICS] บันทึกยอดขายวันนี้เพิ่มเติม: {total_sales:,.2f} บาท")

# ==========================================
# MAIN FUNCTION (ส่วนการทำงานหลัก)
# ==========================================
def main():
    log("เริ่มต้นระบบ Smart Store")

    if not authenticate("admin", "1234"):
        log("เข้าสู่ระบบไม่สำเร็จ")
        return
    log("เข้าสู่ระบบสำเร็จ")

    my_cart = Cart()
    p1 = get_product("P01")
    p2 = get_product("P02")

    my_cart.add_item(p1, 1)
    my_cart.add_item(p2, 2)

    update_stock("P01", 1)
    update_stock("P02", 2)

    subtotal = my_cart.get_total()
    final_price = apply_discount(subtotal, code="SAVE10")

    if process_payment(final_price, method="PromptPay"):
        print_receipt(my_cart, final_price)
        report_sale(final_price)

    log("จบการทำงาน")

if __name__ == "__main__":
    main()