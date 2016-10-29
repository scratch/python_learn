def computepay(h, r):
    h = float(hrs)
    r = float(rate)

    if (h > 40):
        totalpay = (40 * r) + ((1.5 * r) * (h-40))
    else:
        totalpay = h * r

    return totalpay;


hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate:")

totalpay = computepay(hrs, rate)

print (totalpay)

