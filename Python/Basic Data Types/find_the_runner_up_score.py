if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    arr = list(map(int, input().split()))  # Convert the input to a list of integers

    # Remove duplicates by converting to a set, then sort the unique scores in descending order
    unique_scores = sorted(set(arr), reverse=True)

    # The runner-up score is the second largest unique score
    print(unique_scores[1])
