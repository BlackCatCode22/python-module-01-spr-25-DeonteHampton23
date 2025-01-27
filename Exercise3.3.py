score = input("Enter Score: ")
fsc = float(score)
if fsc > 1.0 :
    print('Please enter a score greater than zero but less than 1')
    
elif fsc >= 0.9 :
    print('A')
    
elif fsc >= 0.8 :
    print('B')
    
elif fsc >= 0.7 :
    print('C')
    
elif fsc >= 0.6 :
    print('D')
    
else :
    print('F')