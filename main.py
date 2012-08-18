from classes.VendingMachine import *
from classes.Goods import *

## Intial data ##
v = VendingMachine()

pepsi = Goods( 'PEPSI' ,10 )
oishi = Goods( 'OISHI' ,20 )

v.add_stock( pepsi, 10 )
v.add_stock( oishi, 0 )

v.running() # Run the machine


