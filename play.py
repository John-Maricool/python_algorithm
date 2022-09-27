from operator import countOf

def nth_most_rate(integers, n):
    listAsSet = set(integers)
    print(listAsSet)
    dict = {}
    for val in listAsSet:
        count_a = countOf(integers, val)
        dict.__setitem__(val, count_a)
    # print(dict)

    value = list(dict.values())
    value.sort(reverse= True)
    # print(value)

    item = value[n-1]
   # print(item)

    print(GetKey(item, dict))


def GetKey(val, dict):
    for key, value in dict.items():
      if val == value:
         return key
    return "key doesn't exist"

nth_most_rate([1,1,1,1,1,2,2,2,2,3,3,3,4,4], 4)

