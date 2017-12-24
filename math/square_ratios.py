#!/usr/bin/python3

# Ratios of consecutive squared integers to the prior interation
# All ratios converge on 1.00 (i.e. two decimals, since thet never
# truly reaches 1) at 403 iterations
#
# To view out to this width direct output to a file and view in
# vi without word wrap.  For console display keep iterations
# around 15 to 30 depending on screen width

# set to 403 for convergence on 1.00
iterations = 30

# store the results in matrix
ws = [[], [], [], [], [], []]
for i in range(iterations):
    ws[0].append(i)
    # the squares to evaluate
    ws[1].append(i**2)
    # prior / current ratio which is < 0
    if i > 0:
        ws[2].append(((i-1)**2)/(i**2))
    else:
        ws[2].append(0.0)
    #current / prior ratio which is > 0
    if i > 1:
        ws[3].append((i**2)/((i-1)**2))
    else:
        ws[3].append(0.0)
    # ratio of the ratios
    if i != 0 and ws[2][i-1] != 0:
        # these two ratios of ratios should be equal
        ws[4].append(ws[2][i-1]/ws[2][i])
        ws[5].append(ws[3][i]/ws[3][i-1])
    else:
        ws[4].append(0.0)
        ws[5].append(0.0)

# print stored values
for i in range(6):  # rows
    for j in range(iterations):
        if i == 0 or i == 1: # iterations(0) and squared integers(1)
            print("{:6} ".format(ws[i][j]), end="")
        if i > 1 and ws[i][j] >= 1:
            print("{:6.3} ".format(ws[i][j]), end="")
        elif i > 1:
            print("{:6.2} ".format(ws[i][j]), end="")
    print("")
