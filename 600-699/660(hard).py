t = int(input())
for values in range(t):
    n = int(input())
    chars = map(str,input())
    mapping = {
        "A" : "T",
        "C" : "G",
        "T" : "A",
        "G" : "C"
    }
    result = ""
    for ch in chars:
        result += mapping[ch]
    print(result)

# learnt how to use dictionary, and how we can just leave a variable blank before our for loop, and then add values to it.