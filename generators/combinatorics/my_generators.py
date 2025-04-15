def generate_permutations(arr, path=[]): #перестановки
    if not arr:
        print(path)
        return
    for i in range(len(arr)):
        generate_permutations(arr[:i] + arr[i+1:], path + [arr[i]])

def generate_arrangements(arr, k, path=[]): #размещения, Идея: как в перестановках, но остановка на глубине k
    if len(path) == k:
        print(path)
        return
    for i in range(len(arr)):
        generate_arrangements(arr[:i] + arr[i+1:], k, path + [arr[i]])

def generate_combinations(arr, k, index=0, path=[]): #сочетания, Идея: выбираем элементы только из нетронутой части пути, т.е. всегда двигаемся вперёд + глубина
    if len(path) == k:
        print(path)
        return
    for i in range(index, len(arr)):
        generate_combinations(arr, k, i + 1, path + [arr[i]]) #во избежание повторений, комбинации не составляются с буквами, которые уже были в пути

def generate_product(arr, k, path=[]): #размещения с повторениями, Идея: как в перестановках, но остановка на глубине k
    if len(path) == k:
        print(path)
        return
    for i in range(len(arr)):
        generate_arrangements(arr, k, path + [arr[i]])

def generate_combinations_with_replacement(arr, k, index=0, path=[]): #сочетания, Идея: выбираем элементы только из нетронутой части пути, т.е. всегда двигаемся вперёд + глубина
    if len(path) == k:
        print(path)
        return
    for i in range(index, len(arr)):
        generate_combinations(arr, k, i, path + [arr[i]]) #во избежание повторений, комбинации не составляются с буквами, которые уже были в пути