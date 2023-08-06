from calculator.calculator import Calculator

def test_add():
    """Testing .add() method for addition of up to two numbers"""
    Calculator.add(3,5)
    assert Calculator.memory[0] == 8
    Calculator.add(1)
    assert Calculator.memory[0] == 1
    Calculator.add()
    assert Calculator.memory[0] == 0
    Calculator.add(-10)
    assert Calculator.memory[0] == -10
    Calculator.add(-10.5)
    assert Calculator.memory[0] == -10.5

def test_substract():
    """Testing .substract() method for substraction of two numbers"""
    Calculator.substract(6,3)
    assert Calculator.memory[0] == 3
    Calculator.substract(3)
    assert Calculator.memory[0] == -3
    Calculator.substract()
    assert Calculator.memory[0] == 0
    Calculator.substract(-10)
    assert Calculator.memory[0] == 10
    Calculator.substract(5.45)
    assert Calculator.memory[0] == -5.45
    Calculator.substract(-3)
    assert Calculator.memory[0] == 3

def test_multiply():
    """Testing .multiply() method for multiplication of two numbers"""
    Calculator.multiply(6,3)
    assert Calculator.memory[0] == 18
    Calculator.multiply(3)
    assert Calculator.memory[0] == 0
    Calculator.multiply()
    assert Calculator.memory[0] == 0
    Calculator.multiply(-10)
    assert Calculator.memory[0] == 0
    Calculator.multiply(5.45,4.123)
    assert Calculator.memory[0] == 5.45*4.123

def test_divide():
    """Testing .divide() method for division of two numbers"""
    Calculator.divide(6,3)
    assert Calculator.memory[0] == 6/3
    Calculator.divide(3)
    assert Calculator.memory[0] == 3
    Calculator.divide()
    assert Calculator.memory[0] == 0
    Calculator.divide(5.45,4.123)
    assert Calculator.memory[0] == 5.45/4.123

def test_nr():
    """Testing .nr() method for returning y-th root of x"""
    Calculator.nr(3,4)
    assert Calculator.memory[0] == 4**(1/3)
    Calculator.nr(3)
    assert Calculator.memory[0] == 0**(1/3)
    Calculator.nr()
    assert Calculator.memory[0] == 0**(1/1)
    Calculator.nr(5.45,4.123)
    assert Calculator.memory[0] == 4.123**(1/5.45)

def test_show_memory():
    """Testing the .show_memory() method for returning memory value"""
    Calculator.add(1,2)
    assert Calculator.add(1,2) == Calculator.show_memory()

def test_clear_memory():
    """Testing the .clear_memory() method for reseting memory value to 0"""
    Calculator.add(1,2)
    assert Calculator.add(1,2) == Calculator.show_memory()
    Calculator.clear_memory()
    assert Calculator.memory[0] == 0



























