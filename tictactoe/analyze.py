import matplotlib.pyplot as plt

results = []
with open("res/results.txt", "r") as result_file:
    for line in result_file:
        if "Player 1" in line:
            results.append(1)
        elif "Player 2" in line:
            results.append(-1)
        else:
            results.append(0)

draw_rate = []
lose_rate = []
win_rate = []
for i in range(0, len(results) - 100):
    result_window = results[i: i + 100]
    draw_rate.append(len([i for i in result_window if i == 0]))
    lose_rate.append(len([i for i in result_window if i == -1]))
    win_rate.append(len([i for i in result_window if i == 1]))

plt.plot(draw_rate, label="draw")
plt.plot(lose_rate, label="lose")
plt.plot(win_rate, label="win")
plt.legend()
plt.show()
