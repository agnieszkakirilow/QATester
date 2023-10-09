def my_test1():
    assert 1 * 8 == 8

def my_test2():
    assert 1 * 7 == 7

def my_test3():
    assert 1 - 1 == 0  

def my_test4():
    assert 3 * 8 == 24  

def my_test5():
    assert 1/1 == 1 
 
def my_test6():
    assert 1 - 10 == -9

def my_test7():
    assert 1 + 10 == 11

def my_test8():
    assert 1 + 1 == 2 

def my_test9():
    assert 1 * 1 == 2 

if __name__ == "__main__":
    my_test()
    print("Everything passed")

