def isBalanced(s, dict_symbol):
    print("s:", s)
    print("type s:",type(s))
    li = list(s)
    stack = []
    print("li:", li)
    
    for i in range(len(li)):
        if li[i] in dict_symbol:
            stack.append(li[i])
        
        if li[i] in dict_symbol.values():
            key = [k for k, v in dict_symbol.items() if v == li[i]][0]
            print("value:{} , found key: {}".format(li[i], key)) 
            print("curr_stack:", stack)
            if stack[-1] == key:
                del stack[-1]
            else:
                print("Stack: {}, key: {}".format(stack, key))
                break
                
            
    if len(stack) == 0:
        print("Yes")
        return "YES"
    else:
        print("No")