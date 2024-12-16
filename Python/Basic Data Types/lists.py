if __name__ == '__main__':
    N = int(input())  # Read the number of operations
    arr = []  # Initialize the list
    
    # Define the methods in a way we can call them with arguments
    methods = {
        'insert': lambda i, e: arr.insert(int(i), int(e)),
        'print': lambda: print(arr),
        'remove': lambda e: arr.remove(int(e)),
        'append': lambda e: arr.append(int(e)),
        'sort': lambda: arr.sort(),
        'pop': lambda: arr.pop(),
        'reverse': lambda: arr.reverse()
    }
    
    # Process each operation
    for _ in range(N):
        line = input().split()  # Split the input into a list
        
        operation = line[0]  # The operation is always the first element
        args = line[1:]  # Remaining parts are the arguments
        
        # Call the method from methods dictionary with the provided arguments
        if args:
            methods[operation](*args)  # Call the method with unpacked arguments
        else:
            methods[operation]()  # Call the method if no arguments are needed

            
            
