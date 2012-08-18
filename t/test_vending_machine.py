# Test for class `VendingMachine`

import unittest
import os.path
from classes.VendingMachine import *
from classes.Goods import *

class TestVendingMachine( unittest.TestCase ):

    def setUp( self ):
        self.my_machine = VendingMachine()

        self.assertIsNotNone( self.my_machine )

    def test_buy( self ):
        # Add stock
        product = Goods( 'PEPSI', 20 );
        self.my_machine.add_stock( product, 10 )

        # Buy PEPSI
        result = self.my_machine.sell( product, 100 )
        self.assertTrue( result['status'], "Machine can sell" )
        self.assertEqual( result['change'], 80, "Got collect change" )

        # Check Stock
        stock = self.my_machine.stock()
        self.assertEqual( stock[product], 9, "Got collect stock amount" )

    def test_buy_empty_product( self ):
        # Add stock
        product = Goods( 'OISHI', 20 );
        self.my_machine.add_stock( product, 0 )

        # Buy OISHI
        result = self.my_machine.sell( product, 100 )
        self.assertFalse( result['status'], "Machine can not sell " )



if __name__ == '__main__':
    unittest.main()
