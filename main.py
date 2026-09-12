import all_modules

def main():
    all_modules.log("เริ่มต้นระบบ Smart Store")

    if not all_modules.authenticate("admin", "1234"):
        all_modules.log("เข้าสู่ระบบไม่สำเร็จ")
        return

    my_cart = all_modules.Cart()
    my_cart.add_item(all_modules.get_product("P01"), 1)
    
    all_modules.update_stock("P01", 1)
    
    final_price = all_modules.apply_discount(my_cart.get_total(), "SAVE10")
    
    if all_modules.process_payment(final_price, "PromptPay"):
        all_modules.print_receipt(my_cart, final_price)
        all_modules.report_sale(final_price)

if __name__ == "__main__":
    main()