from error import Error

class Parser:
    def __init__(self, code: str):
        #Pass in code
        self.code = code
        #Parse code
        self.code = self.Parse(self.code)

    def Parse(self, code: str) -> str:
        #Parse code into normal python
        code = self.ParseInclude(code)
        code = self.ParseImport(code)
        code = self.ParseComments(code)
        code = self.ParseKeyWords(code)
        code = self.ParseEOL(code)
        code = self.ParseBraces(code)
        code = self.Parsesfaccimms(code)
        code = self.Parsesammente(code)
        code = self.Parsesi(code)
        code = self.Parsepe(code)
        code = self.Parseautrimenti(code)
        code = self.Parseco(code)
        code = self.Parsede(code)
        code = self.Parsesput(code)
        code = self.Parseturna(code)
        code = self.CleanCode(code)
        code = self.AddEntryPoint(code)

        #Dump code to file
        with open("output.py", "w") as f:
            f.write(code)
        return code
    def ParseComments(self, code: str) -> str:
        for line in code.splitlines():
            if "//" in line:
                if not self.IsInString("//", line):
                    if list(line)[0] == "/" and list(line)[1] == "/":
                        code = code.replace(line, "")
                    else:
                        newLine = line.partition("//")[0]
                        code = code.replace(line, newLine)
        return code

    def ParseInclude(self, code: str) -> str:
        includeName = ""
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if words[wordNo] == "from" and not self.IsInString(words[wordNo], line):
                    if words[wordNo + 1]== "native":
                        if words[wordNo + 2] == "fratm":
                            words[wordNo] = f"from {words[wordNo + 3]} import *"
        for line in code.splitlines():
            words = line.split()
            for wordNo, word in enumerate(words):
                if word == "fratm" and not self.IsInString(word, line):
                    includeName = words[wordNo + 1]
                    code = code.replace(line, "")
                    with open(includeName.removesuffix(";") + ".np", "r") as file:
                        code = file.read() + "\n" + code
        for line in code.splitlines():
            if "from native reference " in line:
                if self.IsInString("from native reference ", line, True):
                    continue
                code = code.replace(line, line.replace("from native reference ", "import "))
                words = line.split()
                newLine = ""
                for wordNo, word in enumerate(words):
                    if words[wordNo] == "from" and not self.IsInString(words[wordNo], line):
                        if words[wordNo + 1] == "native":
                            if words[wordNo + 2] == "reference":
                                words[wordNo] = "import"
                                words[wordNo] = ""
                                words[wordNo + 2] = ""
                                newLine = " ".join(words)
                if newLine != "":
                    code = code.replace(line, newLine)


        return code

    def ParseImport(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "mport" in line and not self.IsInString("mport", line):
                code = code.replace(line, line.replace("mport", "import"))
        return code

    def ParseKeyWords(self, code: str) -> str:
        for line in code.splitlines():
            if "chiste" in line and not self.IsInString("chiste", line):
                code = code.replace(line, line.replace("chiste", "self"))
        for line in code.splitlines():
            if "over" in line and not self.IsInString("over", line):
                code = code.replace(line, line.replace("over", "True"))
        for line in code.splitlines():
            if "fals" in line and not self.IsInString("fals", line):
                code = code.replace(line, line.replace("fals", "False"))
        for line in code.splitlines():
            if "nente" in line and not self.IsInString("nente", line):
                code = code.replace(line, line.replace("nente", "None"))
        for line in code.splitlines():
            if "si noni" in line and not self.IsInString("si noni", line):
                code = code.replace(line, line.replace("si noni", "elif"))
        return code

    def ParseEOL(self, code: str) -> str:
        code = "".join([s for s in code.splitlines(True) if s.strip("\r\n")])

        for line in code.splitlines():
            skipLine = False
            for token in ("sfaccimm", "ammente", "pe", "si", "autrimenti", "si noni", "co", "cata"):
                if token in line and not self.IsInString(token, line):
                    skipLine = True
            if ''.join(line.split()).startswith(("{", "}", "\n", "bastardo")):
                skipLine = True
            elif line.strip() == "":
                skipLine = True
            if skipLine:
                continue
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break

            elif line.endswith((":")):
                Error(f"Syntax error in: \n{line}")
            else:
                Error(f"Missing semicolon in: \n{line}")
            if line.endswith((":")):
                Error(f"Syntax error in: \n{line}")

        return code

    def Parsepe(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "ppe" in line and not self.IsInString("ppe", line):
                code = code.replace(line, line.replace("ppe", "for"))
        return code

    def Parsesi(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "si" in line and not self.IsInString("si", line):
                code = code.replace(line, line.replace("si", "if"))
        return code

    def Parseautrimenti(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "autrimenti" in line and not self.IsInString("autrimenti", line):
                code = code.replace(line, line.replace("autrimenti", "else"))
        return code

    def Parseco(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "co" in line and not self.IsInString("co", line):
                code = code.replace(line, line.replace("co", "with"))
        return code

    def Parsede(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "cata" in line and not self.IsInString("cata", line):
                code = code.replace(line, line.replace("cata", "from"))
        return code

    def Parseturna(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "turna" in line and not self.IsInString("turna", line):
                code = code.replace(line, line.replace("turna", "return"))
        return code



    def ParseBraces(self, code: str) -> str:
        leftBracesAmount = 0
        for line in code.splitlines():
            if "{" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "{":
                        if stringCount % 2 == 0 and stringCount != 0:
                            leftBracesAmount += 1
                            break
        rightBracesAmount = 0
        for line in code.splitlines():
            if "}" in line:
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == "}":
                        if stringCount % 2 == 0 and stringCount != 0:
                            rightBracesAmount += 1
                            break

        if leftBracesAmount != rightBracesAmount:
            Error(("Braces amount is not equal"))

        newCode = ""
        splitLines = code.splitlines();
        for line in splitLines:
            if ";" in line and not self.IsInString(";", line):
                lineChars = list(line)
                stringCount = 0
                for i in range(len(lineChars)):
                    if lineChars[i] == '"' or lineChars[i] == "'":
                        stringCount += 1
                    if lineChars[i] == ";":
                        if stringCount % 2 == 0:
                            lineChars[i] = "\n"
                            break
                line = "".join(lineChars)
            if "bastardo" in line:
                if not self.IsInString("bastardo", line):
                    line = line.replace("bastardo", "class")
                    line = "\n"+" ".join(line.split())
            if "sfaccimm" in line:
                if line.partition("sfaccimm")[0].count("\"") != 0 and line.partition("sfaccimm")[0].count("\"") % 2 == 0:
                    words = line.split()
                    for wordNo, word in enumerate(words):
                        if word == "sfaccimm":
                            speechCount = line.partition("sfaccimm")[2].count("\"")
                            otherCount = line.partition("sfaccimm")[2].count("'")
                            if speechCount % 2 == 0 and otherCount % 2 == 0:
                                words[wordNo] = "def"
                                break
                    line = " ".join(words)
            leftBraceExpression = ''.join(line.split())
            if not self.IsInString("{", leftBraceExpression):
                if ''.join(line.split()).startswith(("{")):
                    newCode += ":\n"
            if not self.IsInString("}", line):
                    line = line.replace("}", "#endindent")
            if not self.IsInString("{", line):
                line = line.replace("{", "#startindent")
            line += "\n"
            newCode += line
            line += "\n"

        return newCode

    def Parsesfaccimms(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "sfaccimm" in line and not self.IsInString("sfaccimm", line):
                code = code.replace(line, line.replace("sfaccimm", "def"))
        for line in code.splitlines():
            if "def Start" in line and not self.IsInString("def Start", line):
                code = code.replace(line, line.replace("def Start", "def __init__"))
        for line in code.splitlines():
            if ") is" in line and not self.IsInString(") is", line):
                code = code.replace(line, line.replace(") is", ") ->"))
        for line in code.splitlines():
            if "def" in line:
                if (line.partition("def")[0].strip() == ""):
                    code = code.replace(line, line.replace("(", "(self,"))
        return code

    def Parsesammente(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "ammente" in line and not self.IsInString("ammente", line):
                code = code.replace(line, line.replace("ammente", "while"))
        return code

    def Parsesput(self, code: str) -> str:
        code = code
        for line in code.splitlines():
            if "sput" in line and not self.IsInString("sput", line):
                code = code.replace(line, line.replace("sput", "print"))
        return code

    def CleanCode(self, code : str) -> str:
        #I'm not going to lie, I made a lot of mistakes. Let's hope these hacks fix it.

        splitLines = code.splitlines()
        for lineNo, line in enumerate(splitLines):
            if line.startswith(":"):
                splitLines[lineNo - 1] = splitLines[lineNo - 1] + ":"
                splitLines[lineNo] = ""
        newCode = ""
        for line in splitLines:
            newCode += line + "\n"
        code = newCode

        splitLines = code.splitlines()
        newCode = ""
        for lineNo, line in enumerate(splitLines):
            i = 0
            indentCount = 0
            while i <= lineNo:
                if "#endindent" in splitLines[i]:
                    if not self.IsInString("#endindent", splitLines[i], True):
                        indentCount -= 1
                elif "#startindent" in splitLines[i] and not self.IsInString("#startindent", splitLines[i], True):
                    if not self.IsInString("#startindent", splitLines[i]):
                        indentCount += 1
                i += 1
            newCode += ("    " * indentCount) + line + "\n"
        code = newCode

        #Remove indent helpers
        newCode = ""
        for line in code.splitlines():
            if "#endindent" in line:
                if not self.IsInString("#endindent", line):
                    line = line.replace(line, "")
            if "#startindent" in line:
                if not self.IsInString("#startindent", line):
                    line = line.replace(line, "")
            newCode += line + "\n"
        code = newCode

        #Tidy code by removing empty lines
        newCode = ""
        for line in code.splitlines():
            if line.strip("\t\r\n") == "":
                line = line.replace(line, line.strip("\t\r\n"))
                newCode += line
            else:
                newCode += line + "\n"
        code = newCode

        code = "\n".join([ll.rstrip() for ll in code.splitlines() if ll.strip()])

        return code

    def AddEntryPoint(self, code: str) -> str:
        code += "\n"
        code += '''
if __name__ == "__main__":
    main = Main()
    main.Main()
        '''

        return code

    def IsInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True
