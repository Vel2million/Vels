def echo_message(func):
    def inner(txt):
        func(txt)
        func(txt)
    return inner

@echo_message
def print_message(txt):
    print(txt)

print_message("WTF")
print(print_message.__name__)

def pretty_sumab(func):                                                                                     
    def inner(a,b):                                                                                         
        print(str(a) + " + " + str(b) + " is ", end="")                                              
        return func(a,b)                                                                                    
                                                                                                            
    return inner                                                                                            
                                                                                                            
@pretty_sumab                                                                                               
def sumab(a,b):                                                                                             
    summed = a + b                                                                                          
    print(summed)

sumab(5,7)

