

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

    def validate_id(self, productid):
        if not isinstance(productid, int):
            return True
        return False

    def validate_new_record(self, date, items, sale_quantity, total_price):
        try:
            if date == "" and items == "":
                return "please input date or items"
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

    def validate_user(self, username, password, role):
        try:
            if username == "":
                return "username cannot be empty"
            if password == "":
                return "password cannot be empty"
            if role == "":
                return "role cannot be empty"
            if not isinstance(username, str):
                return "username must be a string of characters"

        except KeyError:
            return "please input all fields"

    def validate_login(self, username, password):
        try:
            if username == "":
                return "username cannot be empty"
            if password == "":
                return "password cannot be empty"
            if not isinstance(username, str):
                return "username must be a string of characters"

        except KeyError:
            return "please input all fields"
