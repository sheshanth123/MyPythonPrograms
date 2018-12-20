# In general, if you know the year, you add 1 to the first two digits to get the century, unless it ends in double-zero (00). 
# Thus, 1997 is in the 19+1 century, or the 20th century. 1800 is in the 18th century.
p = input()
def centuryFromYear(year):
    if(year%10 == 0):
        return year/100;
    return int((year/100) +1)
centuryFromYear(p)
