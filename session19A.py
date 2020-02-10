
#  every python program is a Module

# import one module in other

#   main would be of present module only

import session19
#  or this statement can be written.. then S19.fun() and cRef=S19.CA()


# import session19 as S19
print("This is session19A")
print("Session19A __name__ is",__name__)
# fun() error

#  for using the funs from session 19
# module name dot operator and members in module


session19.fun()
# session19.main()
cRef=session19.CA()


#############################################
# Error
# fun()

# Use Module Name than . operator to access members in Module
# Session19.fun()
# Session19.main()

# cRef = Session19.CA()
