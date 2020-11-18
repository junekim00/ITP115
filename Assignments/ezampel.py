"""
    Assignment 2: Fibonacci Numbers

    Description: Basically first calculate Fibonacci numbers iteratively,
                    then use the numbers to draw the Fibonacci squares using
                    ASCII art. These in turn can be used for drawing Fibonacci
                    spiral, but we will leave it at that :)

    Fun excerise: Use the squares to then draw the spiral :)
"""

n = int(input("What Fibonacci number do you want ?: "))
x = 0
y = 1

if n == 1:
    fib_num = 0
    print("Fibonacci number " + str(n) + " is: " + str(fib_num))
elif n == 2:
    fib_num = 1
    print("Fibonacci number " + str(n) + " is: " + str(fib_num))
else:
    for i in range(3, n+1):
        z = x + y
        x = y
        y = z
        fib_num = z
        if i == n:
            print("Fibonacci number " + str(n) + " is: " + str(fib_num))

fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(str(n), "th Fibonacci Square")
side_length = fib_list[n - 1]

for i in range(n,0,-1):
  print(str(i),"th Fibonacci Square")
  side_length = fib_list[n-1]
  for idy in range(0,side_length):
    for idx in range(0,side_length):
      if idx == 0 or idx == side_length-1 or idy == 0 or idy == side_length-1:
      	print("*", end = "")
      else:
      	print(" ", end = "")
    print()