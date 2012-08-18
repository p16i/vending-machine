# Test for class `VendingMachine`

import unittest
import os.path
from classes.VendingMachine import *
from classes.Goods import *

class TestVendingMachine( unittest.TestCase ):

    def setUp( self ):
        self.my_machine = VendingMachine()

        self.assertIsNotNone( self.my_machine );

    def test_buy( self ):
        # Add stock
        product = Goods( 'PEPSI', 20 );
        self.my_machine.add_stock( product, 10 );

        # By PEPSI
        result = self.my_machine.sell( product, 100 )
        self.assertTrue( result['status'], "Machine can sell" );
        self.assertEqual( result['change'], 80, "Got collect change" );


if __name__ == '__main__':
    unittest.main()
