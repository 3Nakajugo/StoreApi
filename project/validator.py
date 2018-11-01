

class Validator:

    def valid_add_product(self, product_name, quantity, unit_price, category):
        try:
            if product_name == "":
                return "please enter product name"
            if quantity == "":
                return "please enter product quantity"
            if not isinstance(quantity, int):
                return "quantity must be an integer"
            if int(quantity) < 0:
                return "quantity mmust not be less than 1"
            if unit_price == "":
                return "please enter product price"
            if not isinstance(unit_price, int):
                return "unit price must be an integer"
            if int(unit_price) < 0:
                return "product price cannot be less than zero"
            if category == "":
                return "please enter product category"
            if isinstance(category, int):
                return "category should be characters"

        except KeyError:
            return "please enter all fields"

    def validate_id(self, product_id):
        if not isinstance(product_id, int):
            return True
        return False

    def validate_new_record(self, date, items, sale_quantity, total_price):
        try:
            if date == "":
                return "please input date"
            if items == "":
                return"please input items sold"
            if not isinstance(items, str):
                return "items must be in a string"
            if sale_quantity == "":
                return "please input string"
            if not isinstance(sale_quantity, int):
                return "sale_quantity must be an integer"
            if total_price == "":
                return "please input total price"
            if not isinstance(total_price, int):
                return "total price must be an integer"
        except KeyError:
            return "please input all fields"
