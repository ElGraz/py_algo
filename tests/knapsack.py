# Unbounded Knapsack Problem
def UnboundedKnapsack(Capacity,n,weight,val):
    dp=[]
    for i in range(Capacity+1):
        dp.append(0)
    for i in range(0,Capacity+1):
        for j in range(0,n):
            if weight[j] < i:
                dp[i] = max(dp[i] , dp[i-weight[j]]+val[j])

    print(dp)
    return dp[Capacity]
''' No. of items '''
n = 4
''' Weights of all items '''
weight = [5,10,8,15]
''' Values of all items '''
val = [40,30,50,25]
''' Capacity of Knapsack '''
Capacity = 120
print("The maximum value possible is ",UnboundedKnapsack(Capacity,n,weight,val))

