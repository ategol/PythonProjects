class BinaryToNumber:
    def binary_array_to_number(arr):
        #(11111)₂ = (1 × 2⁴) + (1 × 2³) + (1 × 2²) + (1 × 2¹) + (1 × 2⁰) = (31)₁₀
        arr_length = len(arr) -1
        index = 0
        sum = 0
        for bin in arr:
            sum += arr[index] * 2**arr_length
            print(arr[index] * 2**arr_length)
            arr_length -= 1
            index += 1
        return sum

    print(binary_array_to_number([1,1,0,1,0]))