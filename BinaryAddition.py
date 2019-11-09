class BinaryAddition:
    def add_binary(a, b):
        n = a + b
        str = ""
        if n == 1:
            return "1"
        while n > 0:
            number = n // 2
            if n % 2 == 0:
                str += "0"
            else:
                str += "1"
            n = number
        stringlength = len(str)  # calculate length of the list
        slicedString = str[stringlength::-1]  # slicing
        print(slicedString)  # print the reversed string

    print(add_binary(12,21))
