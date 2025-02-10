def sort_sum(s):
    numbers = sorted(map(int, s.split('+')))
    return '+'.join(map(str, numbers))

# Leitura de entrada
s = input().strip()

# Processamento e saída
print(sort_sum(s))
