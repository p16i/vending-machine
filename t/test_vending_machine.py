# Test for class `VendingMachine`

import unittest
import os.path
from classes.VendingMachine import VendingMachine

class TestVendingMachine( unittest.TestCase ):
    def test_can_use_vending_machine( self ):
        my_machine = VendingMachine();
        self.assertTrue( my_machine.sell, "We can sell" );

if __name__ == '__main__':
    unittest.main()
