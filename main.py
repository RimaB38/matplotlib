from matplotlib import pyplot as plt

# plt.subplots()
# plt.show()



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

x =[1,2,3,4,5]
y1 = [2,2,0,0,2]
y2 = [4,3,2,1,-1]
y3 = [2,4,9,16,25]
y4 = [-1,1,-1,1,-1]
fig,axs = plt.subplots(2,2,figsize=(10,6))

axs[0,0].plot(x,y1,color="red")
axs[0,0].plot.set_title("x ir y1(linija)")

axs[0,1].scatter(x,y2,color='green')
axs[0,1].set_tittle("x,y2,(taskai)")

axs[1,0].plot(x,y3,color='purple',marker='o')
axs[1,0].set_title("x ir y3,(linija + taskai)")

axs[1,1].plot(x,y4,color='black',linestyle='--')
axs[1,1].set_title("x,y4,(bruksnine linija)")

plt.tight_layout()
plt.show()

