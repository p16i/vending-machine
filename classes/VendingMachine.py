# Vending Machine Class
# By Pattarawat Chormai

class VendingMachine :

    # Init method
    def __init__(self):

        # Ex: stock = { $PRODUCT_OBJ : $LEFT }
        self.__stock = dict()

    # Sell method
    def sell( self, order, money ):
        res = dict()
        res['status'] = 1
        res['change'] = money - order[1]
        return res

    # Encapsulate Attr

    # Stock
    def stock():
        return self.__stock;

    def add_stock( self, product, amount ):
        self.__stock[product] = 10

