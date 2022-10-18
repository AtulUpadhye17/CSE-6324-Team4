from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification


class IncorrectConstructorOrder(AbstractDetector):
    """
    Detect Constructor not in sequence with functions
    """

    ARGUMENT = 'incorrect-constructor-order' # slither will launch the detector with slither.py --detect incorrect-constructor-order
    HELP = 'constructor not in sequence with functions'
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = ''
    WIKI_TITLE = 'Incorrect Constructor Order'
    WIKI_DESCRIPTION = 'Detect Constructor not in sequence with functions'
    WIKI_EXPLOIT_SCENARIO = ''
    WIKI_RECOMMENDATION = ''

    def _detect(self):
        results = []

        for contract in self.slither.contracts_derived:
            
            list_of_methods=contract.functions

            for x in range(len(list_of_methods)):
                #Check if constructor is present and placed before the functions
                if str(list_of_methods[x]).lower == "constructor" and list_of_methods[x]!=list_of_methods[0]:

                    #info to be printed
                    info = ['Incorrect constructor Order found in ',contract,"\n"]

                    res = self.generate_result(info)

                    results.append(res)

        return results


