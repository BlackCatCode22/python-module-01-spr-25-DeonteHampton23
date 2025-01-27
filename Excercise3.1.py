hrs = input("Enter Hours:")
rt = input("Enter Rate:")
fhs = float(hrs)
frt = float(rt)
if fhs > 40 :
       # print("Overtime")
        reg = frt * fhs 
        otp = (fhs - 40.0) * (frt * 0.5)
        #print(reg, otp)
        xp = (reg + otp)
print(xp)