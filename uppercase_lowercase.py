#python function that a calculate uppercase and loercase leeter in string
def string_test(s):
    a={"upper_case":0, "lower_case":0}
    for x in s:
        if x.isupper():
            a["upper_case"]+=1
        elif x.islower():
            a["lower_case"]+=1
        else:
            pass
    print("original string", s)
    print("no. of upper case characters:", a["upper_case"])
    print("no. of lower case characters:", a["lower_case"])

string_test("The quick Brown Fox")