count = 0
p1, p2, p3, p4 = map(int, input().split())
if p1 >= 10:
    count += 1
if p2 >= 10:
    count += 1
if p3 >= 10:
    count += 1
if p4 >= 10:
    count += 1
print(count)

# you should use if only if u want to check each week independentyl, if u use elif then it wont check the other conditions and wont take them into account if one condition is true.