import math
# Radix sort for numbers in base 10
def radixSortNumbers(array):
    maxLen = -1
    for number in array: # Find longest number, in digits
        numLen = int(math.log10(number)) + 1
        if numLen > maxLen:
            maxLen = numLen
    buckets = [[] for i in range(0, 10)] # Buckets for each digit
    for digit in range(0, maxLen):
        for number in array:
            buckets[number / 10**digit % 10].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array
print radixSortNumbers([1,5,30,5,9,2,1,8])
