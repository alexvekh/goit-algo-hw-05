"""
Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа 
на основі двох текстових файлів (стаття 1, стаття 2). 
Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: 
одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.
"""

import timeit

from file1 import file1
from file2 import file2
from KMP_search_algorithm import kmp_search
from Boyer_Moore_search_algorithm import boyer_moore_search
from Rabin_Karp_search_algorithm import rabin_karp_search

exist_pattern = "Алгоритмы"
exist_pattern2 = "Берновски"
fantasy_pattern = "aaaaaaaaa"
file = file1 + file2


#print(f"  unsorted:".ljust(20), numbers_copy)
#print(f"  sorted by insertion:".ljust(20), insertion_sort(numbers_copy))

print("Text1 ==============================")
print("   ---  exist pattern  ---")
def search_by_kpm():
    kmp_search(file1, exist_pattern)
time_taken = timeit.timeit(search_by_kpm, number=100) / 100
print(kmp_search(file1, exist_pattern))
print(f"Average kmp search time: {time_taken:.6f} seconds")

def search_by_boyer_moore():
    boyer_moore_search(file1, exist_pattern)
time_taken = timeit.timeit(search_by_boyer_moore, number=100) / 100
print(boyer_moore_search(file1, exist_pattern))
print(f"Average Boyer Moore search time: {time_taken:.6f} seconds")

def search_by_rabin_karp():
    rabin_karp_search(file1, exist_pattern)
time_taken = timeit.timeit(search_by_rabin_karp, number=100) / 100
print(rabin_karp_search(file1, exist_pattern))
print(f"Average Rabin Karp search time: {time_taken:.6f} seconds")

print("   ---  fantasy pattern  ---")

def search_by_kpm():
    kmp_search(file1, fantasy_pattern)
time_taken = timeit.timeit(search_by_kpm, number=100) / 100
print(kmp_search(file1, fantasy_pattern))
print(f"Average kmp search time: {time_taken:.6f} seconds")

def search_by_boyer_moore():
    boyer_moore_search(file1, fantasy_pattern)
time_taken = timeit.timeit(search_by_boyer_moore, number=100) / 100
print(boyer_moore_search(file1, fantasy_pattern))
print(f"Average Boyer Moore search time: {time_taken:.6f} seconds")

def search_by_rabin_karp():
    rabin_karp_search(file1, fantasy_pattern)
time_taken = timeit.timeit(search_by_rabin_karp, number=100) / 100
print(rabin_karp_search(file1, fantasy_pattern))
print(f"Average Rabin Karp search time: {time_taken:.6f} seconds")

print("Text2 ==============================")
print("   ---  exist pattern  ---")
def search_by_kpm():
    kmp_search(file2, exist_pattern2)
time_taken = timeit.timeit(search_by_kpm, number=100) / 100
print(kmp_search(file2, exist_pattern2))
print(f"Average kmp search time: {time_taken:.6f} seconds")

def search_by_boyer_moore():
    boyer_moore_search(file2, exist_pattern2)
time_taken = timeit.timeit(search_by_boyer_moore, number=100) / 100
print(boyer_moore_search(file2, exist_pattern2))
print(f"Average Boyer Moore search time: {time_taken:.6f} seconds")

def search_by_rabin_karp():
    rabin_karp_search(file2, exist_pattern2)
time_taken = timeit.timeit(search_by_rabin_karp, number=100) / 100
print(rabin_karp_search(file2, exist_pattern2))
print(f"Average Rabin Karp search time: {time_taken:.6f} seconds")

print("   ---  fantasy pattern  ---")

def search_by_kpm():
    kmp_search(file2, fantasy_pattern)
time_taken = timeit.timeit(search_by_kpm, number=100) / 100
print(kmp_search(file2, fantasy_pattern))
print(f"Average kmp search time: {time_taken:.6f} seconds")

def search_by_boyer_moore():
    boyer_moore_search(file2, fantasy_pattern)
time_taken = timeit.timeit(search_by_boyer_moore, number=100) / 100
print(boyer_moore_search(file2, fantasy_pattern))
print(f"Average Boyer Moore search time: {time_taken:.6f} seconds")

def search_by_rabin_karp():
    rabin_karp_search(file2, fantasy_pattern)
time_taken = timeit.timeit(search_by_rabin_karp, number=100) / 100
print(rabin_karp_search(file2, fantasy_pattern))
print(f"Average Rabin Karp search time: {time_taken:.6f} seconds")