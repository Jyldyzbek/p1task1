def f(number): return number % 2 == 0
def test_f():
    assert f(2) == True
    assert f(3) == False
    assert f(8) == True
    assert f(100) == True
    assert f(101) == False
print("YOUR CODE IS CORRECT!")

test_f()