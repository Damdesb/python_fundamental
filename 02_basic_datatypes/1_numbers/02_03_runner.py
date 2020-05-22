'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
#convert 10 miles in km
km = 1.6
run_miles = 10
run_km = (run_miles * km)
print("distance run in km is : ", (run_km))

#convert running time in hour
hour = 1
minute = 60
second = 3600
run_time_hour = (30 / minute) + (30 /second)

#find average speed
print("the average speed is :", (run_km / run_time_hour), ("km"))
