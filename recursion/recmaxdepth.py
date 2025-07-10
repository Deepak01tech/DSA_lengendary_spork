i=0
def g():
    global i
    print(i)
    i+= 1
    g()
# This code will raise an UnboundLocalError because 'i' is referenced before it is assigned within the function.