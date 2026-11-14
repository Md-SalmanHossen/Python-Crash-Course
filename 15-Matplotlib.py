import matplotlib.pyplot as plt

x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]

plt.plot(x,y)

plt.title("Simple line plot")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()


# practice plot line:
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,4,8,12]

plt.plot(x,y,color='red',linestyle="--",marker='o')

plt.title("Customize plot")
plt.grid(True)

plt.show()

# singe and cos
import matplotlib.pyplot as plt
import numpy as np

# x-axis value
x=np.linspace(-np.pi,np.pi,100)

# yaxis values
y_sine=np.sin(x)
y_cos=np.cos(x)

# make plot
plt.plot(x,y_sine, label="sine (sin x)", color="red" , linestyle="--")
plt.plot(x,y_cos, label="cosine (cosine x)", color="blue", linestyle="--")

# Graph styling
plt.title("Sine and Cosine Waves")
plt.xlabel("X-axis (Radians)")
plt.ylabel("Y-axis")

# x axis line
plt.axhline(0, color="black",)
# y axis line
plt.axvline(0, color="black",)

plt.legend()
plt.grid()

plt.show

# y=mx+c
import matplotlib.pyplot as plt
import numpy as np;

# parameter for y=mx+c
m=2
c=3

# x values
x=np.linspace(-10,10,100)

# forumula
y=m*x+c

# make plot
plt.plot(x,y,label=f"y={m}x+c{c}",color="green")

# graph style
plt.title("linear equation: y=mx+c")
plt.xlabel("X-axis")
plt.ylabel("y-label")

plt.axhline(0,color="black")
plt.axvline(0,color="red")
plt.legend()
plt.grid(True)

plt.show()


