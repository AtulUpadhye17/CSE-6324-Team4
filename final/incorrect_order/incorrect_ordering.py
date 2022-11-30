from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
import slither


class IncorrectOrdering(AbstractDetector):

    ARGUMENT = 'ordering'
    HELP = 'Check order of elements in file and inside each contract, according to the style guide.'
    IMPACT = DetectorClassification.OPTIMIZATION
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = 'https://github.com/trailofbits/slither/wiki/Adding-a-new-detector'
    WIKI_TITLE = 'Ordering'
    WIKI_DESCRIPTION = 'Check order of elements in file and inside each contract, according to the style guide.'
    WIKI_EXPLOIT_SCENARIO = '...'
    WIKI_RECOMMENDATION = 'Add the correct order of elements in the file and inside each contract.'
    
    def _detect(self):
        results = []
        elements_list = []
        for n in self.slither.crytic_compile.filenames:     
            rootFileName = n.absolute
            with open(rootFileName, 'r') as f:
                for line in f:
                    elements_list.append(line)

            # check if the order of the constructor is correct or not               
            for contract in self.slither.contracts_derived:
                
                list_of_methods=contract.functions

                for x in range(len(list_of_methods)):
                    #Check if constructor is present and placed before the functions
                    if str(list_of_methods[x]).lower == "constructor" and list_of_methods[x]!=list_of_methods[0]:

                        #info to be printed
                        info = ['Incorrect constructor Order found in ',contract,"\n"]

                        res = self.generate_result(info)

                        results.append(res)
            
            # check if the order of elements is correct or not
            for contract in self.slither.contracts_derived:
                for function in contract.functions:
                    for element in elements_list:
                        if function.name in element:
                            if element.index(function.name) > elements_list.index(element):
                                info = ["The function {} is declared before the variable declaration.".format(function.name),"\n"]
                                res = self.generate_result(info)
                                results.append(res)
                                
            # check if the library is declared before the contract or not
            # if the library is declared after the contract, print the line number and the error message.
            library_index = 0
            contract_index = 0

            for i in range(len(elements_list)):
                if elements_list[i].startswith("contract"):
                    contract_index = i
                if elements_list[i].startswith("library"):
                    library_index = i
            if library_index > contract_index:
                info = [f"The library is declared after the contract.","\n"]
                res = self.generate_result(info)
                results.append(res)

            # check if the interface is declared after the library or not
            # if the interface is declared before the library, print the line number and the error message.

            interface_index = 0
            library_index = 0

            for i in range(len(elements_list)):
                if elements_list[i].startswith("library"):
                    library_index = i
                if elements_list[i].startswith("interface"):
                    interface_index = i
                    
            if interface_index < library_index:
                info = ["The interface is declared before the library.","\n"]
                res = self.generate_result(info)
                results.append(res)
        return results
        