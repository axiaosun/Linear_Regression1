#!/usr/bin/env python3

# Determine the equation of the best-fit line using the least squared method
# Calculate expected y when x = test_x, given n numer of lines of sets of x and y

n = int(input())
x_ = []
y_ = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    x_.append(x)
    y_.append(y)

test_x = 80

b = (n*sum([x_[i]*y_[i] for i in range(n)])-sum(x_)*sum(y_)) / (n*sum([x_[i]**2 for i in range(n)])-sum(x_)**2)

a = sum(y_) / n - b*(sum(x_)/n)

regression_line = a+b*test_x

print(round(regression_line, 3))
