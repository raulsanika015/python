import matplotlib.pyplot as plt 

plt.bar([1,3,5,7,9],[5,2,7,8,2], label="student 1",color='y')
plt.bar([1.5,3.5,6,8,10],[8,6,2,5,6], label="student 2", color='b')
plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Wow! We Got Our First Bar Graph')
plt.show()
