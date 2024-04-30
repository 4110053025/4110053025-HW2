# During our class, we discussed how to calculate the n-th
# Fibonacci Number, denoted as F(n), using top-down
# ( divide and conquer/ pure recursive) and bottom-up
# (dynamic-programming-like) methods.
# For this exercise, please complete the following tasks:

# 1. Write code to measure the execution time of
# F(1), F(2), ..., F(100) using both methods.
# Plot the results as a line chart.
# (if your program crashes during computation F(n+1) or takes
# too much time (>12hours) to compute one value, you can just
# stop and report the maximum value of n.)

# 2. Let's measure the degree of overlapping subproblem.
# Calculate the times are F(4) computed when we compute
# F(5),F(6),.....,F(50). Plot the results into line chart.

# Please submit your code and the answers to these questions,
# along with a link to your code repository on GitHub.

import matplotlib.pyplot as plt


def f_top_down(n):
    # f(n) == 計算第n個費波那契數所需要計算f(4)的次數
    if n == 4 or n == 5:
        return 1
    # 計算第4或第5個費波那契數僅需計算一次f(4)
    else:
        return f_top_down(n - 1) + f_top_down(n - 2)
    # 計算第n個費波那契數所需的f(4) = 第n-1個跟第n-2個的總和


# main
top_d = []  # overlapping subproblem of top_down


for i in range(4, 51):
    top_d.append(f_top_down(i))

    if i % 5 == 4 and i != 4:
        print("* ", end="")
    if i % 5 != 4:
        print("*", end="")
    # 進度條

x = []
for i in range(4, 51):
    x.append(i)
# 折線圖的x軸


print("\n\n""Degree of overlapping subproblem:")
for i in range(4, 51):
    print(str(i) + " " + str(top_d[i-4]) + "(degree)")
# 將第4個到第50個費波那契數的子問題數量依序print出來

plt.plot(x, top_d, 'ro-')
plt.title('Degree of overlapping subproblem of top-down method')
plt.xlabel('number of Fibonacci ')
plt.ylabel('overlapping subproblem')
plt.legend(loc='upper left')
plt.show()
# 折線圖繪製
