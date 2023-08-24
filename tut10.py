# n=input("Enter your name: ")
# print("Hello",n)

str_seconds = input("Please enter the number of seconds you wish to convert :")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
print(secs_still_remaining)
minutes =  secs_still_remaining // 60
print(secs_still_remaining)
secs_finally_remaining = secs_still_remaining  % 60
print(secs_still_remaining)

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
print(524/60)
print(524%60)
print(60*8)
print(524-480)