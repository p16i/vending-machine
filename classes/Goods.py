# Goods
# by Pattarawat Chormai

class Goods :
    def __init__( self, n, p ):
        self.__name = n
        self.__price = p


    #Encapsulate

    # Name
    def name( self ):
        return self.__name

    # Price
    def price( self ):
        return self.__price
