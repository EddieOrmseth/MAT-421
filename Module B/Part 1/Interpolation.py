import matplotlib.pyplot as plot

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
y = [ 1, 4, 7, 1, 2, 9, 1, 6, 4, 5 ]

plot.plot(x, y, marker='o', linestyle='None', color='r', label='Original Data')
plot.title("Raw Data")
plot.xlabel("X-axis")
plot.ylabel("Y-axis")
plot.legend()
plot.grid()
plot.show()
