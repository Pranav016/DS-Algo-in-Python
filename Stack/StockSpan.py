# Afzal has been working with an organization called 'Money Traders' for the past few years. The organization is into the money trading business. His manager assigned him a task. For a given array/list of stock's prices for N days, find the stock's span for each day.

# The span of the stock's price today is defined as the maximum number of consecutive days(starting from today and going backwards) for which the price of the stock was less than today's price.

# For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85], then the stock spans will be [1, 1, 1, 2, 1, 4, 6].

# Explanation:
# On the sixth day when the price of the stock was 75, the span came out to be 4, because the last 4 prices(including the current price of 75) were less than the current or the sixth day's price.

# Similarly, we can deduce the remaining results.


def stockSpan(stock):
    if not stock:
        return 
    span=[]
    stack=[]
    i=0
    while i<len(stock):
        if not stack:
            stack.append(i)
            span.append(i+1)
        else:
            if stock[stack[-1]]>=stock[i]:
                span.append(i-stack[-1])
                stack.append(i)
            elif stock[stack[-1]]<stock[i]:
                while stack and stock[i]>stock[stack[-1]]:
                    stack.pop()
                if not stack:
                    span.append(i+1)
                else:
                    span.append(i-stack[-1])
                stack.append(i)
        i+=1
    
    return span


# main
n=int(input())
stock=[]
if n>0:
    ele=list(int(i) for i in input().split())
    for i in ele:
        stock.append(i)
    span=stockSpan(stock)
    print(*span)
