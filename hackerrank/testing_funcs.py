# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/leaderboard

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

### split func creates the iterable. int is a function.
### map only creates an object. use list to create list


    







