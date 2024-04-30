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

import time
import matplotlib.pyplot as plt


def f_top_down(n):
    if n == 0 or n == 1:
        return n
    else:
        return f_top_down(n - 1) + f_top_down(n - 2)


def f_bottom_up(n):
    if n == 0 or n == 1:
        return n
    else:
        table = []
        for i in range(n+1):
            if i == 0 or i == 1:
                table.append(i)
            if i >= 2:
                table.append(table[i-2] + table[i-1])
        return table[n]


# main
top_d = []  # run time of top_down
bot_u = []  # run time of bottom_up

total_time_t = 0
last_n = 0

for i in range(101):
    start_time_t = time.time()
    f_top_down(i)
    run_time_t = time.time() - start_time_t
    # running time of ith Fibonacci num with top_down
    top_d.append(run_time_t)

    if i % 5 == 0 and i != 0:
        print(" *", end="")
    if i % 5 != 0:
        print("*", end="")
    # 進度條，每增加一個星星代表跑完一個費波那契數

    if run_time_t >= 43200:
        last_n = i
        print("\n""running too much time, end up at %sth Fibonacci number" % last_n)
        break
    else:
        last_n = i
    # 當計算單個費波那契數的時間過長，就中止for loop，並記錄最後一個費波那契數


print("\n")


for i in range(last_n + 1):
    # 為了讓折線圖的項數一樣多，就以top-down最後跑到的項次當作bottom-up的終點
    start_time_b = time.time()
    f_bottom_up(i)
    run_time_b = time.time() - start_time_b
    # running time of ith Fibonacci num with bottom_up
    bot_u.append(run_time_b)

    if i % 5 == 0 and i != 0:
        print(" *", end="")
    if i % 5 != 0:
        print("*", end="")
    # 進度條


x = []
for i in range(last_n + 1):
    x.append(i)
# 折線圖的x軸


print("\n\n""time for calculate each Fibonacci num with top-down:")
for i in range(last_n + 1):
    print(str(i) + "  " + str(top_d[i]) + "(sec)")
print("\n""time for calculate each Fibonacci num with bottom-up:")
for i in range(last_n + 1):
    print(str(i) + "  " + str(bot_u[i]) + "(sec)")
# print每個費波那契數的計算時間


plt.plot(x, top_d, 'ro-', label='top-down')
plt.plot(x, bot_u, 'go-', label='bottom-up')
plt.title('Comparison of Fibonacci number calculation speed')
plt.xlabel('number of Fibonacci')
plt.ylabel('Calculation speed(sec)')
plt.legend(loc='upper left')
plt.show()
# 折線圖繪製
