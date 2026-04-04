class Outer:
  def __init__(self):
    self.name = "ranjan"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"hi my name is {self.outer.name}")
    
outer = Outer()
inner = outer.Inner(outer)

inner.display()

#Pass the outer class instance to the inner class:

