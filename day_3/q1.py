class Parser():
    def __init__(self):
        self.possible = set("mul()")
        self.state = ""
        self.cur_num = ""
        self.cur_num_2 = ""

    def parse(self, s: str):
        result = 0
        for char in s: # numbers are 1-3 digit long
            if char == "m" and self.state == "":
                self.state = "m"
            elif char == "u" and self.state == "m":
                self.state = "mu"
            elif char == "l" and self.state == "mu":
                self.state = "mul"
            elif char == "(" and self.state == "mul": # immediately jump to and check all next possibilities?
                self.state = "rn"
            elif self.state == "rn" and char.isnumeric():
                self.cur_num += char
            elif self.state == "rn" and char == ",":
                self.state = "rn2"
            elif self.state == "rn2" and char.isnumeric():
                self.cur_num_2 += char
            elif self.state == "rn2" and char == ")":
                self.state = ""
                result += int(self.cur_num) * int(self.cur_num_2)
                self.cur_num = ""
                self.cur_num_2 = ""
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
