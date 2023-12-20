def total_with_tips (bill, percentage) :
    tip = bill*percentage/100
    tip = min(tip, 500)
    total = bill + tip 
    total = round(total, 2)
    return max(total, 5)