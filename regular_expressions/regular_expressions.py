from engine import MyRegex

if __name__ == "__main__":
    inp = input("Input: ")
    regex, string = inp.split("|")
    re = MyRegex(regex)
    result = re.find(string)
    print("Output: ", "True" if result else "False")
    more_info = list(re.find_all(string))
    print("More info: ", more_info)