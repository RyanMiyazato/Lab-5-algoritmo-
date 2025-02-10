def sort_students(n, student_data):
    houses = {"Slytherin": [], "Hufflepuff": [], "Gryffindor": [], "Ravenclaw": []}

    for i in range(0, 2 * n, 2):
        name = student_data[i]
        house = student_data[i + 1]
        houses[house].append(name)

    order = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"]

    result = []
    for house in order:
        result.append(f"{house}:")
        result.extend(houses[house])
        result.append("")

    return "\n".join(result).strip()


# Leitura de entrada
n = int(input().strip())
student_data = [input().strip() for _ in range(2 * n)]

# Processamento e saída
print(sort_students(n, student_data))
