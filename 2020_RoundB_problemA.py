
"""
Problem

Li has planned a bike tour through the mountains of Switzerland. His tour
consists of N checkpoints, numbered from 1 to N in the order he will visit
them. The i-th checkpoint has a height of Hi.

A checkpoint is a peak if:
It is not the 1st checkpoint or the N-th checkpoint, and
The height of the checkpoint is strictly greater than the checkpoint
immediately before it and the checkpoint immediately after it.

Please help Li find out the number of peaks.

Input
The first line of the input gives the number of test cases, T. T test cases
follow. Each test case begins with a line containing the integer N. The second
line contains N integers. The i-th integer is Hi.

Output
For each test case, output one line containing Case #x: y, where x is the test
case number (starting from 1) and y is the number of peaks in Li's bike tour.
"""


#read in number of test cases
t = input()

#loop through test cases
for i in range(0,int(t)):
    #read in number of checkpoints
    n = input()
    #read in heights
    h = [int(h) for h in input().split()]

    #reset number of peaks found
    peaks = 0
    #loop through checkpoints to find peaks
    for j in range (1,int(n)-1):
        #if current height is greater than the height immediately before
        #    and after it, count it as a peak
        if h[j] > h[j-1] and h[j] > h[j+1]:
            peaks += 1
    
    #print number of peaks found    
    print("Case #{}: {}".format(i+1, peaks))