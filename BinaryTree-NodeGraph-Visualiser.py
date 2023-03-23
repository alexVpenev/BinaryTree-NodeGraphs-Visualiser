import math

# def getMiddle(array):
#     return array[len(array)//2]

# for i in range(0, len(arr)):
#     print(getMiddle(arr))





def print_tree(arr):
    # calculate the height of the tree
    height = 0
    while 2**height - 1 < len(arr):
        height += 1

    # print the tree row by row
    for i in range(height):
        level = 2**i
        offset = 2**(height - i - 1) - 1
        print(' ' * offset, end='')
        for j in range(level):
            index = level - 1 + j
            if index < len(arr):
                print(f'{arr[index]:^2}', end='')
                print(' ' * (2 * offset + 1), end='')
        print()

# example usage
# input_arr = [1, 2, 3]
# print_tree(input_arr)






def print_treee(arr):
    # calculate the height of the tree
    height = 0
    while 2**height - 1 < len(arr):
        height += 1

    # print the tree row by row
    for i in range(height):
        level = 2**i
        offset = 2**(height - i - 1) - 1
        print(' ' * offset, end='')
        for j in range(level):
            index = level - 1 + j
            if index < len(arr):
                print(f'{arr[index]:^2}', end='')
                print(' ' * (2 * offset + 1), end='')
            else:
                print('  ', end='')
                print(' ' * (2 * offset + 1), end='')
        print()

        # print the arrows for the next level
        if i < height - 1:
            next_offset = 2**(height - i - 2) - 1
            print(' ' * next_offset, end='')
            for j in range(level):
                index = level - 1 + j
                if index < len(arr):
                    print('/' + ' ' * (2 * offset - 1) + '\\', end='')
                    print(' ' * (2 * next_offset + 1), end='')
                else:
                    print(' ' * (2 * offset + 1), end='')
        print()



# input_arr = [1, 2, 3, 4, 5, 6, 7, 8]
# print_treee(input_arr)

def calcLevel(array):
    return 1 + int(math.log2(len(array)))

def mine(array):

    k = 0

    for i in range(1, calcLevel(arr)):
        for f in range(0, len(array), len(arr) //  i):
            print(str(array[k]), end=' ')
            k+=1
        print()
        




arr = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16]
mine(arr)

#     3
#    /  \
#   1    2
#  / \  / \
# 4   5 6   7
# 8 9 10111213 1415
#16

# print(calcLevel(arr))      
            # print("level" + str(i) + ": " + str(array[k]), end=' ')