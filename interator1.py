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

a=PowTwo(6)
i=next(a)
print(i)
i=next(a)
print(i)
i=next(a)
print(i)


class Alpha: 
    
             def __init__(self, max = 'a'):        
                                         self.max = max
                                         self.n = 'a'
            
             def __next__(self):        
                              if self.n <= self.max:   
                                                    result = char(self.n)+1            
                                                       
                                                    self.n += 1
                                                  
                                                    return result        
                              else:            
                                   raise StopIteration

for i in PowTwo(5):
     print(i)
