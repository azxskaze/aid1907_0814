def myadd(num1):
    """
111
    :param num1:
    :return:
    """
    return num1%10+num1//10%10+num1//100%10+num1//1000
print(myadd(1234))
