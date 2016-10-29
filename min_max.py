largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
       print "Maximum is", largest
       print "Minimum is", smallest

       break
    try:
        num = int(num)
    except:
        print 'Invalid input' 
        continue

    if (smallest == None or num < smallest):
        smallest = num
    if (largest == None or num > largest):
        largest = num
