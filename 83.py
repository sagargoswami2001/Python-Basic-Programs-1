# Write a Python Program to Convert Seconds to Day,Hour,Minutes and Seconds.

time = float(input("Input Time in Seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
Seconds = time
print("D:H:M:S-> %d:%d:%d:%d" % (day, hour, minutes, Seconds))