# Our function will take three parameters:
# last - The Date object with the date of the last period
# today - The Date object with the date of the check
# cycleLength - Integer representing the length of the cycle in days
# Return true if the number of days passed from last to today is greater than cycleLength. 
# Otherwise, return false.

def period_is_late(last,today,cycle_length):        
    actual_length = today - last   
    if actual_length.days > cycle_length:
        return True
    else:
        return False