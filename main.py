from matplotlib import pyplot as plt

# plt.subplots()
# plt.show()

x

# x reiksmes
x= [1,2,3,4,5,6,7,8,9]
a = 30
x2 =[i*i for i in x]
x3 = [i**3 for i in x]
xa = [i**a for i in x]
fig,(ax1,ax2,ax3) = plt.subplots(1,3)
ax1.plot(x,x2,color="red",linestyle="-",marker="o")
ax2.plot(x,x3,color="blue",linestyle="-",marker="x")
ax3.plot(x,xa,color="purple",linestyle="-",marker="s")
plt.legend()
plt.show()