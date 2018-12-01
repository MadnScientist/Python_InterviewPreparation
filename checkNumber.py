class Solution:
    def __init__(self):
        self.li = ['-','1','2','3','4','5','6','7','8','9','0','+', '.', 'e']
        self.neg_val = -2147483648
        self.pos_val = 2147483647
        

    def isNumber(self, str_val):
        str_val = str_val.lstrip().rstrip()
        
        arr = str_val.split('e')            
        val = ["float","int"]
        is_num = False
        i = 0
        if len(arr) <= 2: 
            for item in arr:
                print("item: {} , val[i]: {}".format(item, val[i]))
                if val[i] == 'int' and ('e' in str_val):
                    if '.'  in item:
                        is_num= False
                        break
                is_num = self.myAtoi(item, val[i])
                if is_num == False:
                    break
                i += 1
                
        return is_num
                    
            
    def myAtoi(self, str_val, var_type):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        ret = False
        
        
        try:
            li_char = [] 
            char_arr = list(str_val)
            print("arr:", char_arr)
            for char in char_arr:
                print("char:", char)
                if char in self.li:
                    if ((char == '-') or (char == '+')) and (len(li_char) == 0):
                        li_char.append(char)

                    elif (char != '-') and (char != '+'):
                        li_char.append(char)

                    else: 
                        ret = False
                        break
                    ret = True
                else:
                    print("broke at a:", char)
                    ret = False
                    break
                    
            print("ret:", ret)
            if ret == True:
                if var_type == 'float':
                    num = float(('').join(li_char))
                elif var_type == 'int':
                    num = int(float(('').join(li_char)))
            
            if num > self.pos_val:
                num = self.pos_val
            elif num < self.neg_val :
                num = self.neg_val    
            
        except:
            ret = False
            pass

        return ret


sol = Solution()
val =  ". 1"
sol.is_number(val)