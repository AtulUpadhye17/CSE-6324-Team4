from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification

class IncorrectConstructorName(AbstractDetector):
    """
    Detect Incorrect Constructor Name
    """

    ARGUMENT = "incorrect-constructor-name"  
    HELP = "Incorrect Constructor Name should be proper."
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = ""
    WIKI_TITLE = "Incorrect Constructor Name"
    WIKI_DESCRIPTION = "Detect Incorrect Constructor Name"
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = ".."

    def _detect(self):
        results = []

        for contract in self.slither.contracts_derived:
            for f in contract.functions:
                #Check if any function name matches with contract name
                if f.name.lower() == contract.name.lower():
                    
                    # Info to be printed
                    info = ["Incorrect Constructor Name found in ",f,"\n"]
                    
                    res = self.generate_result(info)

                    results.append(res)

        return results

        