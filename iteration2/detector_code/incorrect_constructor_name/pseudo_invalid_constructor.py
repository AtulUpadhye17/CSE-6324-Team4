from slither.slither import Slither  
  
slither = Slither('./invalid_constructor_name.sol')  
  
for contract in slither.contracts:  
    #Get the function names
	print ('Contract: '+ contract.name)  
	for function in contract.functions:  
        	#Check if any function name matches with contract name
        	if function.name.lower() == contract.name.lower():
        		print('Invalid Constructor Name : {}'.format(function.name))
        