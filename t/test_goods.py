# Test for class `Goods`

import unittest
import os.path
from classes.Goods import *

class TestVendingMachine( unittest.TestCase ):

    def setUp( self ):
        self.my_goods = Goods( 'PEPSI' , 20 );

    def test_object( self ):
        self.assertIsNotNone( self.my_goods )

if __name__ == '__main__':
    unittest.main()
