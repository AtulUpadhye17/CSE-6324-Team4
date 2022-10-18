from slither.slither import Slither  
  
slither = Slither('constructor.sol')  
  
    
for contract in slither.contracts:
    li=contract.functions
    print ('Contract: '+ contract.name)
    
    for x in range(len(li)):
        #Check if constructor is present and placed before the functions
        if str(li[x]) == "constructor" and li[x]!=li[0]:
            print("Incorrect constructor Order") 

