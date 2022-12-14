
# definitions for rules:  
#  statement such as x that can be true or false <- indeterminate
#  statement such as x || !x is always true 
#  statement such as x || y is indeterminate
#  statement such as x || x is indeterminate
#  statement such as x && x == x || x 
# precidence heirachy of symbols <- () brackets are most important then break into || and &&
def evaluateNode(nodeArray,operator):
    if(nodeArray[0] == nodeArray[1]):
        return mathematicalBooleanOperator(operator,-1,-1)
    
    return mathematicalBooleanOperator(operator,(nodeArray[0] == "!"+nodeArray[1]),(nodeArray[1] == "!"+nodeArray[0]))
 


# def conversion(operator,value1,value2):
#     if(operator=="OR"):
#         return (value1 or value2)
#     elif(operator=="SAME"):
#         return value1

def parseIntoNodes(inputStatement):
    # if(")" in inputStatement):
    #     nodeArray = inputStatement.split(")")
    #     for x in range(len(nodeArray)):

    if("||" in inputStatement):
        nodeArrayOr = inputStatement.split("||")
        if(len(nodeArrayOr)==2):
            return evaluateNode(nodeArrayOr,"OR")
        else:
            tmp = True
            for x in range(0,len(nodeArrayOr)-1):
                output = parseIntoNodes(nodeArrayOr[x]+"||"+nodeArrayOr[x+1])
                tmp = mathematicalBooleanOperator("OR",tmp,output)
            return tmp

def mathematicalBooleanOperator(booleanOpertor,value1, value2):
    #value(1,2) can hold 3 values 0<=false,1<=true,-1<=indeterminate
    # 0 OR 1 = 1 therefore ADD
    # 1 OR 1 = 1 therefore MULTIPLY
    # 0 OR 0 = 0 therefore ADD 
    if(booleanOpertor=="OR"):
        return max(value1,value2)*((value1+value2)%2 + (value1*value2))
    elif(booleanOpertor=="AND"):
        return (value1*value2)

if __name__ == "__main__":
    print(parseIntoNodes("x||x||x||x"))
    # print(mathematicalBooleanOperator("OR",-1,0))
    # print(mathematicalBooleanOperator("AND",0,1))
    # print(mathematicalBooleanOperator("AND",1,0))
    # print(mathematicalBooleanOperator("AND",1,1))
    # print(True * True)

# instead of || or && normally used in programming use some variation of 
# mathematics such as multiplication to get answer


