class Parser():
    def __init__(self):
        self.possible = set("mul()")
        self.state = ""
        self.cur_num = ""
        self.cur_num_2 = ""
        self.do = True

    def parse(self, s: str):
        result = 0
        for char in s: # numbers are 1-3 digit long
            if char == "m" and self.state == "" and self.do:
                self.state = "m"
            elif char == "u" and self.state == "m" and self.do:
                self.state = "mu"
            elif char == "l" and self.state == "mu" and self.do:
                self.state = "mul"
            elif char == "(" and self.state == "mul" and self.do: # immediately jump to and check all next possibilities?
                self.state = "rn"
            elif self.state == "rn" and char.isnumeric() and self.do:
                self.cur_num += char
            elif self.state == "rn" and char == "," and self.do:
                self.state = "rn2"
            elif self.state == "rn2" and char.isnumeric() and self.do:
                self.cur_num_2 += char
            elif self.state == "rn2" and char == ")" and self.do:
                self.state = ""
                result += int(self.cur_num) * int(self.cur_num_2)
                self.cur_num = ""
                self.cur_num_2 = ""
            elif self.state == "" and char == "d":
                self.state = "d"
            elif self.state == "d" and char == "o":
                self.state = "do"
            elif self.state == "do" and char == "(":
                self.state = "do("
            elif self.state == "do(" and char == ")":
                self.state = ""
                self.do = True
            elif self.state == "do" and char == "n":
                self.state = "don"
            elif self.state == "don" and char == "'":
                self.state = "don'"
            elif self.state == "don'" and char == "t":
                self.state = "don't"
            elif self.state == "don't" and char == "(":
                self.state = "don't("
            elif self.state == "don't(" and char == ")":
                self.state = ""
                self.do = False
            else:
                self.state = ""
                self.cur_num = ""
                self.cur_num_2 = ""

        return result
    
if __name__ == "__main__":
    f = open("input.txt", "r")
    
    s = []
    for line in f:
        s.append(line.strip())

    s = "".join(s)
    p = Parser()
    print(p.parse(s))
