import pack.one
pack.one.fun()
cRef=pack.one.CA()

import  pack.one as O
O.fun()
cRef=O.CA()

# # from pack.one import *
#
# # incase of above statement everything is imported and functions can be used directly
# fun()
# cRef=CA()
from pack.one import fun

fun()  #ok
# cRef=CA()#error  as only fun() is imported and not all