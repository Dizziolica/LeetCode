def countparents(parentese):


    if "()" in parentese:
        result = parentese.count("()")
      
    print(result)
    
countparents("()()()))")
