r,o,c = map(int,input().split())
average_run_over = c/o
over_left = 20-o
if average_run_over * over_left > r:
    print 