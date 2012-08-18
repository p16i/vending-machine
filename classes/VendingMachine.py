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
        stock = self.__stock
        if( stock[order] > 0 ):
            # Decrease stock
            self.__stock[order] = self.__stock[order] - 1

            res['status'] = 1
            res['change'] = money - order.price()
        else:
            res['status'] = 0
        return res

    # Encapsulate Attr

    # Stock
    def stock( self ):
        return self.__stock;

    def add_stock( self, product, amount ):
        self.__stock[product] = amount

