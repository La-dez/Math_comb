import numpy as np
from math import comb, factorial

# # Сколько бросков кубика дадут 6?
# samples = np.random.randint(1, 7, 100000)
# print(np.mean(samples == 6))  # вероятность выпадения 6

#симуляция по выпадению 4 и более успехов в 10 испытаниях с вероятностью успеха 0.3
result_simulation = np.mean(np.random.binomial(10, 0.3, 100000) >= 4) # вызов распределения уже даёт массив
result_truth = 1 - sum((comb(10, k) * (0.3 ** k) * (0.7 ** (10 - k))) for k in range(4))
print(f"{result_simulation=} and {result_truth=}: difference={100*(result_truth-result_simulation)/result_truth}%")  
# вероятность выпадения 4 и более успехов в 10 испытаниях с вероятностью успеха 0.3


#Смоделировать 100 000 экспериментов:
#в каждом бросаем 5 кубиков и считаем, в каком проценте случаев выпало ровно три шестёрки.

trials_count = 1_000_000
# 1. Генерируем броски: 100000 строк по 5 кубиков
throws = np.random.randint(1, 7, size=(trials_count, 5))
# 2. Подсчёт количества шестёрок в каждой строке
sixes_per_trial = np.sum(throws == 6, axis=1)
print(sixes_per_trial)
# 3. Сколько экспериментов дали ровно 3 шестёрки
count = np.sum(sixes_per_trial == 3)
# 4. Вывод процента
percent = count / trials_count * 100
print(f"Ровно три шестёрки: {count} случаев ({percent:.2f}%)")

trials = np.random.binomial(n=5, p=1/6, size=trials_count)
percent = np.mean(trials == 3) * 100
print(f"Ровно три шестёрки: {percent:.2f}%")

#задача про сарай и 6 видов животных
trials_count = 10_000_000
days = 6
#основная генерация
throws = np.random.randint(1, 7, size=(trials_count, days))
throws = np.sort(throws, axis=1)
#подсчёт количества видов уникальных животных в каждом эксперименте
animals_per_trial = (throws[:,1:] != throws[:,:-1]).sum(axis=1)+1
counter = lambda x: np.sum(animals_per_trial == x+1)
counts = [counter(i) for i in range(6)]
probs = [count / trials_count for count in counts]
[print(f"Ровно {i+1} вида(-ов): {counts[i]} случаев ({probs[i]:.2%})") for i in range(6)]
print(f"Сумма вероятностей: {sum(probs):.2%}")
print(f"Мат. ожидание: {sum([(i+1)*probs[i] for i in range(6)])}")

