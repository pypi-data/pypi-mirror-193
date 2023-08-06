class Calculator:
    """Class Calculator with methods as operatins"""
    memory = [0]

    def __init__(self, add: float, substract: float, multiply: float,
                divide: float, nr: float):
        self.add = add
        self.substract = substract
        self.multiply = multiply
        self.divide = divide
        self.nr = nr

    def show_memory() -> int:
        """This method returns the current calculator memory value"""
        print(f"Calculator memory is: {Calculator.memory[0]}")

    def clear_memory() -> int:
        """This method resets calculator memory to 0"""
        Calculator.memory[0] = 0
        print(f"Calculator memory cleared, Memory is: {Calculator.memory[0]}")

    def add(x=0, y=0) -> float:
        """This method adds up to two numbers togeather"""
        result = Calculator.memory[0] = x+y
        print(result)

    def substract(x=0, y=0) -> float:
        """This method substracts two numbers"""
        if y == 0:
            result = Calculator.memory[0] = -x-y
            print(result)
        else:
            result = Calculator.memory[0] = x-y
            print(result)

    def multiply(x=0, y=0) -> float:
        """This method multiplies two numbers togeather"""
        result = Calculator.memory[0] = x*y
        return(result)

    def divide(x=0, y=1) -> float:
        """This method divides two numbers"""
        assert y != 0, "Cannot divide by zero :("
        result = Calculator.memory[0] = x/y
        return(result)

    def nr(y=1, x=0) -> float:
        """This method returns y-th root of x"""
        assert x >= 0, "X has cannot be negative"
        result = Calculator.memory[0] = (abs(x)**(1/y))
        return(result)


