from datetime import date
import time
with open("dates.txt","a") as f:
    x = (str(date.today()))
    x = (x + " you accesed new.py")
    f.write(x)
    f.write("\n")
    
