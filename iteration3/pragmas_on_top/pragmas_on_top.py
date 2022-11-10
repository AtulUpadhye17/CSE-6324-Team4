from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification

class PragmasOnTop(AbstractDetector):
    """
    Detect if pragma statements are placed at the top of the file.
    """

    ARGUMENT = "pragme-on-top"  
    HELP = "pragma statements should always be placed at the top of the file."
    IMPACT = DetectorClassification.OPTIMIZATION
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/trailofbits/slither/wiki/Adding-a-new-detector"
    WIKI_TITLE = "pragma On Top"
    WIKI_DESCRIPTION = "Detect if pragma statements are placed at the top of the file."
    WIKI_EXPLOIT_SCENARIO = ".."
    WIKI_RECOMMENDATION = "pragma Statement should always be placed at top of the file."

    def _detect(self):
        results = []
        
        for n in self.slither.crytic_compile.filenames:
            rootFileName = n.absolute
            word = 'pragma'
            word_number = 0
            contract_num = 0
            contract_list = []
            with open(rootFileName, 'r') as fp:
                # read all lines in a list
                lines = fp.readlines()
                for line in lines:
                    # check if string present on a current line
                    if line.find(word) != -1:
                        word_number = lines.index(line)
                    elif line.startswith('contract') or line.startswith('struct') or line.startswith('library'):
                        contract_list.append(lines.index(line))
                if not len(contract_list) == 0:        
                    contract_num = min(contract_list)
            if word_number > contract_num:
                info = ["pragma statement should be on top : "+rootFileName,"\n"]
            
                res = self.generate_result(info)

                results.append(res) 
        
        return results

        