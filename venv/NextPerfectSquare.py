import math
class NextPerfectSquare:
    def find_next_square(sq):
        root = math.sqrt(sq)
        if int(root + 0.5) ** 2 == sq:
            root +=1
            return root ** 2
        else:
            prreturn -1

    def find_next_square_ken(sq):
        str = []
        x = 0
        ans = 0
        while x <= sq:
            i = 0
            sum = x * x
            str.append(sum)
            x += 1
            if sq in str:
                ans = str.index(sq)
        print(str[ans+1])




    print(find_next_square(121))
    print(find_next_square_ken(121))