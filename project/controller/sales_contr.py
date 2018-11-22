from project.models import SaleRecord, sales_records


class SalesController:
    def add_sale_record(self, record_id,  date, items, sale_quantity, total_price):

        new_record = dict(
            record_id=record_id,
            date=date,
            items=items,
            sale_quantity=sale_quantity,
            total_price=total_price
        )

        sales_records.append(new_record)
        return sales_records

    def get_sales_records(self):
        if len(sales_records) > 0:
            return sales_records

    def single_record(self, record_id):
        # if isinstance(record_id, int):
        for record in sales_records:
            if record["record_id"] == record_id:
                return record
        return "record_id should be an integer"

    def delete_single_product(self, record_id):
        for sale in sales_records:
            if sale["record_id"] == record_id:
                sales_records.remove(sale)
                return sales_records
