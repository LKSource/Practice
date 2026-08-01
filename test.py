#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    # Write your code here
    if len(expenditure) <= d:
        return 0
        
    notifications = 0
    # The problem specifies max expenditure is 200 (adjust if different)
    MAX_EXPENDITURE = 201 
    count = [0] * MAX_EXPENDITURE
    
    # Initialize the frequency array for the first 'd' elements
    for i in range(d):
        count[expenditure[i]] += 1
        
    # Helper function to find 2x median from the frequency array
    def get_double_median(count, d):
        if d % 2 != 0:
            # Odd number of elements: find the middle element
            target = d // 2 + 1
            current_sum = 0
            for val in range(MAX_EXPENDITURE):
                current_sum += count[val]
                if current_sum >= target:
                    return val * 2
        else:
            # Even number of elements: find the average of two middle elements
            target1 = d // 2
            target2 = target1 + 1
            m1 = m2 = None
            current_sum = 0
            for val in range(MAX_EXPENDITURE):
                current_sum += count[val]
                if m1 is None and current_sum >= target1:
                    m1 = val
                if current_sum >= target2:
                    m2 = val
                    return m1 + m2
                    
    # Slide the window across the remaining elements
    for i in range(d, len(expenditure)):
        current_val = expenditure[i]
        
        # Check for notification condition
        if current_val >= get_double_median(count, d):
            notifications += 1
            
        # Update sliding window: add trailing element, remove leading element
        count[current_val] += 1
        count[expenditure[i - d]] -= 1
        
    return notifications

    
if __name__ == '__main__':
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    start_time = time.perf_counter()
    result = activityNotifications(expenditure, d)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function executed in {execution_time:.6f} seconds")
    print(result)

