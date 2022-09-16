import sys

input = sys.argv

def pairs(lst, n):
    min, max = 0, len(lst)-1
    res = []
    if n <= lst[min]:
        return []
    while min < max: ## O(n)
        if lst[min] + lst[max] > n:
            max -= 1
        if lst[min] + lst[max] < n:
            min += 1
        if lst[min] + lst[max] == n:
            res.append([lst[min], lst[max]])
            max -= 1
            min += 1
    return res

def normalizeInput(lst, n):
    lst = lst.split(',')
    lst = [int(x) for x in lst] # O(n)
    lst.sort() ## O(n log n)
    n = int(n)
    
    return lst, n

if len(input) == 3:
    lst, n = normalizeInput(input[1], input[2])
    print(pairs(lst, n))
    
elif len(input) == 2:
    file = open(str(input[1]), 'r').read()
    f = file.split(' ')
    lst, n = normalizeInput(f[0], f[1])
    print(pairs(lst, n))

else: print('Please correct your input')
