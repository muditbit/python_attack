def validate_parantheses(paran):
    stack =[]
    for paran in paran:
        if paran == "{" or paran == "[" or paran == "(":
            stack.append(paran)
        else:
            if not stack:
                return False
            curr = stack.pop()
            if curr == "(":
                if paran!=")":
                    return False
            if curr =="{":
                if paran!="}":
                    return False
            if curr == "[":
                if paran!="]":
                    return False
    if stack:
        return False
    return True

if __name__ == "__main__":

    paran = "[][([])]"
    if validate_parantheses(paran)==True:
        print("Valid")
    else:
        print("Invalid")
