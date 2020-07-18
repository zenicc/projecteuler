'''
Created on 28 April 2020
@author: Campbell



If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain.

'''
################################################################################################################
# Took the following from https://www.mathblog.dk/project-euler-100-blue-discs-two-blue/ when I couldn't solve the
# floating point problems on my original attempt
################################################################################################################
#We want to solve the following equation
#
#   (b/n)*((b-1)/(n-1)) = 1/2
#
#where n is the total number of discs and b is the number of blue discs.  The  equation can be rearranged as
#
#     b^2 - b = 1/2(n^2 - n)
#
#     b^2 - 2b - n^2 + n = 0
#
#Finding an integer solution to this thing? Doesn’t it look like a diophantine equation to you? It has two variables and
#we are looking for an integer solution. My best guess was to search google for a “quadratic diophantine equation”, and
#that result turned up Dario Alpern’s Generic two integer variable equation solver.
#
#That site can give you the detailed step to give you a basic solution to the equation, which we already have through the
#problem statement. As well as an algorithm for all other solutions to the equation. You should really go on to study the
#solutions for these as I wont go through them. I can’t give you better explanations than he does. The site gives us that
#
#    b_{k 1} = 3b_{k} +  2n_{k} - 2
#
#    n_{k 1} = 4b_{k} + 3n_{k} -3
#
#From there on, it is just to iterate solutions until you hit an n which is larger than the minimum value.
# 756872327473 is the answer
################################################################################################################


import time, numpy, math

st = time.time()

b = 15
n = 21
target = 10**12

while n < target: # so the last iteration done below will be the first one > target
    btemp = 3 * b + 2 * n - 2
    ntemp = 4 * b + 3 * n - 3

    b = btemp
    n = ntemp

print(n, b)

print("euler100 took %f seconds" % (time.time() - st))
