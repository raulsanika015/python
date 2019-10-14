class PowTwo: 
    
             def __init__(self, max = 0):        
                                         self.max = max
                                         self.n = 0   
            
             def __next__(self):        
                              if self.n <= self.max:   
                                                    result = 2 ** self.n            
                                                    self.n += 1            
                                                    return result        
                              else:            
                                   raise StopIteration
