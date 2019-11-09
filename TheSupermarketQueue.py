class TheSupermarketQueue:
    def queue_time(customers, n):

        tills = [0]*n
        for time in customers:
            tills[0] += time
            print(tills)
            tills.sort()
            print(tills)
        return max(tills)

    tid = queue_time([5, 3, 10, 4, 4], 3)
    print("Minutes in the queue " + str(tid))