#There is a bookstore owner that has a store open
# for n minutes. Every minute, some number of
# customers enter the store. You are given an integer array customers of length n where
# customers[i] is the number of the customer that enters the store at the start of the ith minute
# and all those customers leave after the end of that minute.

# On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where
# grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise,
# they are satisfied.
#
# The bookstore owner knows a secret technique to keep themselves not grumpy for minutes
# consecutive minutes, but can only use it once.
#
# Return the maximum number of customers that can be satisfied throughout the day.

# Example 1:
#
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
# Example 2:
#
# Input: customers = [1], grumpy = [0], minutes = 1
# Output: 1
# Topic
# Array
# Sliding Window

def maxSatisfied(customers,grumpy,minutes):
    #T.C= O(N)
    #S.C = O(1)
    # initial_satisfaction = 0
    # max_extra_satisfaction = 0
    # current_window_satisfaction = 0
    #
    # for i in range(len(customers)):
    #     if grumpy[i] == 0:
    #         initial_satisfaction += customers[i]
    #     elif i < minutes:
    #         current_window_satisfaction += customers[i]
    #
    # max_extra_satisfaction = current_window_satisfaction
    #
    # for i in range(minutes, len(customers)):
    #     current_window_satisfaction += customers[i] * grumpy[i]
    #     current_window_satisfaction -= customers[i - minutes] * grumpy[i - minutes]
    #     max_extra_satisfaction = max(max_extra_satisfaction, current_window_satisfaction)
    #
    # return initial_satisfaction + max_extra_satisfaction
    l = 0
    window = 0
    max_window = 0
    satisfied = 0

    for r in range(len(customers)):
        # If the owner is grumpy at minute r, consider these customers for the window
        if grumpy[r] == 1:
            window += customers[r]
        else:
            # Directly add to satisfied if the owner is not grumpy
            satisfied += customers[r]

        # If the window exceeds the allowed minutes, adjust from the left
        if r - l + 1 > minutes:
            # Only subtract from window if the owner was grumpy at minute l
            if grumpy[l] == 1:
                window -= customers[l]
            l += 1

        # Update the maximum possible additional satisfaction from a grumpy period
        max_window = max(max_window, window)

    return satisfied + max_window


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

print(maxSatisfied(customers,grumpy,minutes))


