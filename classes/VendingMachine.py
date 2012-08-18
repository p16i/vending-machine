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

    # End Sell

    def running( self ):
        stock = self.__stock

        flag = 1

        print '#####################################'
        print '##   Welcome to Vending Machine    ##'
        print '#####################################'

        while flag :
            print '## Would you like to drink today ? ##'
            print '#####################################'

            for i in range( 0, len(stock) ):
                text = '# ['+str(i+1)+'] '+stock.keys()[i].name()
                text += '\t'+'$'+str(stock.keys()[i].price())

                if( stock.values()[i] == 0 ):
                    text += '\t*Out of Stock'

                print text

            command = raw_input('# Please choose your goods no.\n or type `x` to exit | ') #Get Input

            # Check input
            if( is_int_try(command) and int(command) in range( 1, len(stock)+1 ) ):
                # Sell Goods
                i = int(command)
                product = stock.keys()[i-1]
                flag = 1
                total_money = 0

                print '## Your order '+product.name() + ' ##'
                print '## Please insert money $' + str( product.price() )+ ' or'
                print '## Press `b` to buy or'
                print '## Press `x` to exit'
                while flag:

                    c = raw_input('Total : '+ str(total_money)+ ' | ')

                    if( is_int_try(c) ):
                        total_money += int(c)
                    elif( c == 'b' ):
                        res = self.sell( product, total_money)
                        if( res.get('status') ):
                            print '#####################################'
                            print '#####################################'
                            print '##       Have a Nice day           ##'
                            print 'Return | '+ str(res.get('change'))
                            print '#####################################'
                            print '#####################################'
                            break
                        else:
                            print '!! Something wrong'

                    elif( c == 'x' ):
                        print '#####################################'
                        print '##       Return money              ##'
                        print '#####################################'
                        break


            elif( command == 'x' ):
                # Exit
                print '##      Machine Closed      ##'
                flag = 0
            else:
                print '#####################################'
                print '##       Invalid Command           ##'
                print '#####################################'

    #End Running

## Encapsulate Attr

    # Stock
    def stock( self ):
        return self.__stock;

    def add_stock( self, product, amount ):
        self.__stock[product] = amount


# Helper method
def is_int_try( str ):
    try:
        int(str)
        return True
    except ValueError:
        return False
