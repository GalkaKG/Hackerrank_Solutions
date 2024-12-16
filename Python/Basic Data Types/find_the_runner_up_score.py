if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    arr = list(map(int, input().split()))  # Convert the input to a list of integers

    # Find the best runner (maximum value)
    best_runner_res = max(arr)
    
    # Initialize the runner-up as 0 (this will change if necessary)
    runner_up = 0
    
    # Iterate through the list to find the runner-up
    for el in arr:
        if el != best_runner_res:
            runner_up = max(runner_up, el)  # Keep the maximum of the remaining elements
    
    print(runner_up)
