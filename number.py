def get_int():
    while True:    
        try:
                x = int(input("what's x?" ))
        except ValueError:
                print("x is string")
        else:
             break 
    return x 
        
  