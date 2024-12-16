if __name__ == '__main__':
    matrix, sorted_matrix = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        matrix.append([name, score])
        sorted_matrix = sorted(matrix, key=lambda x: (x[1], x[0]))
        
unique_scores = sorted(set([row[1] for row in matrix]))

sec_score = unique_scores[1]

[print(row[0]) for row in sorted_matrix if row[1] == sec_score]   
