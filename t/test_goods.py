# Test for class `Goods`

import unittest
import os.path
from classes.Goods import *

class TestGoods( unittest.TestCase ):

    def setUp( self ):
        self.name = "PEPSI"
        self.price = 20

        self.my_goods = Goods( self.name, self.price );

    def test_object( self ):
        self.assertIsNotNone( self.my_goods )
        self.assertEqual( self.my_goods.name(), self.name )
        self.assertEqual( self.my_goods.price(), self.price )

if __name__ == '__main__':
    unittest.main()
