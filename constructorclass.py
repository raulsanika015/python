class A:
     def __init__(self):
          print("A's constructor called")
     def print_A(self):
          print("Print of A called:")
          

class B(A):
     def __init__(self):
          super().__init__()
          print("B's constructor called")
     def print_B(self):
          print("Print of B called:")
