# The question provides us a all integer list, and ask for the one number that appear odd times while the other all appear even times.
# Eg: Input:[1,3,2,4,2,4,1], we can see that only 3 appears odd times, we need to find this number from the input.
# Time Complextity Requirement: O(n)
a = [1,3,2,4,2,4,1]

# To find this number, we can use the eor operation,
# since a number eor itself becomes 0, and 0 eor any number
# will become the number itself, we just need to eor every number
# in the list. The result will be what we want

def NumbersAppearOddTime(input):
    eor = 0
    for val in input:
        eor ^= val
    return eor

print(NumbersAppearOddTime(a))

# Extra: what if there are 2 numbers that appear odd times?

b = [1,5,3,7,1,9,5,7]

def NumbersAppearOddTimeVerB(input):
    eor = 0
    for val in input:
        eor = val ^ eor
    
    # Since the 2 numbers are different, they must have 1 bit 
    # where there are different, eg: at 8bits, one is 1, the other
    # is 0. Then we can categorize the all the int into 2 cates,
    # we can then find the rightmost one.
    rightOne = eor & (~eor + 1)
    firstNum = 0
    for val in input:
        # if the val is belong to first category:
        print(rightOne&val)
        if (rightOne & val) == 1:
            # eor the first category to get first odd number
            firstNum = val ^ firstNum
            print(firstNum)
    # since we have eor and firstNum, and eor = firstNum ^ secondNum,
    # therefore:
    print(eor, firstNum)
    secondNum = eor ^ firstNum
    return firstNum, secondNum

print("The two numbers appear odd times are: ",NumbersAppearOddTimeVerB(b))