
from time import perf_counter
from time import sleep as pause
import matplotlib.pyplot as plt
from integer import Integer

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))

def runningtime_py(n):
	time_start = perf_counter()
	result = fib_py(n)
	print("fib_py("+str(n)+")=",result)
 	time_stop = perf_counter()
	execute_time = time_stop-time_start
	print("fib_py("+str(n)+") Elapsed time:",  execute_time, "seconds")
	return round(execute_time,6)


def runningtime_c(n):
	time_start = perf_counter()
	f=Integer(n)
	print("fib_cpp("+str(n)+")=",f.fib())
	time_stop = perf_counter()
	execute_time = time_stop-time_start
	print("fib_cpp("+str(n)+") Elapsed time:",  execute_time, "seconds")
	return execute_time



def plotting_py():
	i_py=[]
	running_time_py=[]
	for i in range (30,45):
		i_py.append(i)
		running_time_py.append(runningtime_py(i))
	plt.scatter(i_py,running_time_py)
	plt.title("plot of fibunnaci exacution time by python  ")
	plt.xlabel("i")
	plt.ylabel("excecution time  seconds")
	plt.savefig("timePy.png")
	plt.show()

def plottin_Cpp():
	i_c=[]
	running_time_c=[]
	for i in range (30,45):
		i_c.append(i)
		running_time_c.apppend(runningtime_c)
	plt.scatter(i_c,running_time_c)
	plt.title("plot of fibunnaci exacution time by python")
	plt.xlabel("i")
	plt.ylabel(" excecution time  seconds ")
	plt.savefig("timeCpp.png")
	plt.show()


defmain():
	plotting_py()
	plottin_Cpp()
	execute_cpp(47)
if __name__ == '__main__':
	main()
