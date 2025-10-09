# def concat(a, b):
  #  return a + " " + b

#print(f"\n Hello {concat("Robbie","Ladd")}")

class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"
    
a = Greeter()
print(a.greet("Robbie"))  # Method call
print(a.name)
