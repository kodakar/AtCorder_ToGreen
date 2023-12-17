N, A, B = map(int, input().split())
print(A*(N//(A+B)) + ((N%(A+B)) if (N%(A+B)) < A else A))