hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate:")

h = float(hrs)
r = float(rate)

pay40hrs = payover40hrs = 0

if (h > 40):
    pay40hrs = 40 * r
    payover40hrs = (r*1.5) * (h-40)
else:
    pay40hrs = h * r

totalpay = pay40hrs + payover40hrs
print (totalpay)

