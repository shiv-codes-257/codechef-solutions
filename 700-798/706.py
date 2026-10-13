t = int(input())
for values in range(t):
    n,a,b = map(int,input().split())
    total_odd_eps = n-(n//2)
    total_even_eps = n//2
    print((a*total_even_eps)+(b*total_odd_eps))