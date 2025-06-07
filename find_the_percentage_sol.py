if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
   
    query_scores = student_marks[query_name]
 
    total = sum(query_scores)
 
    number_of_scores = len(query_scores)

 
    avg_score = total / number_of_scores
 
    print(f"{avg_score:.2f}")