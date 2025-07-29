import time

print("Section 1\n")
print("Reference time(epoch)")
reference_time=time.time()               # returns time elapsed since Jan 1, 1970 in seconds.
print(reference_time)
# We can also calculate run time of different programs using operators between time stamps
print("\nSection 2")
print("Time Difference")
print("\n Method 1")
start_time=time.time()                  #Timestamp at start
k=0
while k<=100:
   print(f"{k}- instance")
   k += 1
end_time=time.time()                    # Timestamp at end

print("time take for the while loop to run: ",end_time - start_time,"seconds")
print()
print("\nMethod 2")
start = time.perf_counter()             # Performance time

for _ in range(1000000):
    pass

end = time.perf_counter()
print("Execution time:", end - start, "seconds")


print("\nSection 3")
print("timestamp conversions")

print(time.ctime())         # Prints human-readable time


local_time=time.localtime(time.time())      #This returns a tuple with all the details like year, month,date etc
print(local_time)
print()
current_time=time.asctime(local_time)
print(current_time)

x=time.time()                  # Gives a timestamp from unix epoch
print(time.ctime(x))           # Converts time stamp to readable time

y=time.localtime()
print(y)
print(time.strftime("%a %d %b %Y %H:%M:%S", y)) # refer to the datetime module file for strftime args

z=time.strptime("21/01/2015","%d/%m/%Y") #Converts string to time tuple
# make sure separator syntax is same in the string '/' in the z string
print(z)
print("\nSection 4")
print("Pause Executions")
i=0
while i<=3:
    start=time.time()
    print(f"{i}- instance, started at: {start}s ")
    time.sleep(2)                           # Used to pause execution for defined time, takes seconds as arguments
    end=time.time()
    print(f"{i}- instance, ended at: {end}s")
    print("Time difference",end-start)
    print()
    i += 1







