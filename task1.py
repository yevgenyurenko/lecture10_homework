
# In this case the exception is not handled by except block, so it will propagate throughout the program
def oops():
    raise KeyError("This is a KeyError")

def catch_oops():
    try:
        oops()
    except IndexError as e:
        print("Caught the IndexError:", e)
catch_oops()


