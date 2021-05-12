from random import choices, randint, uniform
from typing import List
import numpy as np
import pandas as pd
from math import sqrt

Nilai_saham = List[int]
Kromosom = List[int]
Populasi = List[Kromosom]
max_pop = 100  # DAPAT DIRUBAH SESUAI DENGAN MAX POPULASI YANG DIINGINKAN
max_generation = 1000


def generate_kromosom() -> Kromosom:
    # melakukan generate nilai dari a1 sampai a10
    return [uniform(-1, 1) for i in range(11)]


def harga_saham(konstanta: Kromosom, nilai: Nilai_saham):
    # dari soal f(x) = a0 + a1.y1 + a2.y2 + a3.y3 + .... + a10.y10
    # a = konstanta, y = nilai
    nilai = np.insert(nilai, 0, 1)
    return sum(np.multiply(konstanta, nilai))


def hitung_fitness(kromosom: Kromosom, saham: Nilai_saham) -> float:
    # rumus untuk nilai error (Mean Squared Error)
    squared_error = 0
    for i in range(10):
        y = harga_saham(kromosom, saham[i+1:i+11])
        error = saham[i] - y
        squared_error += error ** 2
    mse = sqrt(squared_error/10)
    return 1/(0.00000000000000000000000000000000000000000001+mse)


def populasi_awal() -> Populasi:
    # untuk melakukan generate populasi awal dengan range hingga makpop (sesuai yang diinginkan)
    return [generate_kromosom() for i in range(max_pop)]


def regen_pop(populasi: Populasi, parent: Populasi, pc: int) -> Populasi:
    # menampilkan regenerate populasi berdasarkan mutasi yang dilakukan
    populasi = populasi[:len(populasi)-pc]
    populasi += crossover(parent[0], parent[1], pc)
    return [mutasi(kromosom) for kromosom in populasi]


def parent_selection(populasi: Populasi, saham: Nilai_saham, fit: Populasi) -> Populasi:
    # memilih parent berdasarkan populasi
    return choices(
        populasi,
        weights=fit,
        k=2
    )


def crossover(parentA: Kromosom, parentB: Kromosom, pc: int) -> Populasi:
    # mengawinkan parent
    offspring = []
    for x in range(0, pc-1, 2):
        i = randint(1, 10)
        offspring += [parentA[0:i] + parentB[i:], parentB[0:i] + parentA[i:]]
    if pc % 2:
        i = randint(1, 10)
        offspring += choices([parentA[0:i] + parentB[i:],
                             parentB[0:i] + parentA[i:]], k=1)
    return offspring


def mutasi(kromosom: Kromosom) -> Kromosom:
    for i in range(0, len(kromosom)):
        if np.random.random_sample() < pm:
            kromosom[i] = uniform(-1, 1)
    return kromosom


# fungsi main
# Probabilitas operasi genetik (Pc dan Pm)
pm = 1/(max_pop*11)  # probabilitas mutasi = 1 / banyak gen
pc = round(0.4 * max_pop)

gen = 0
# membaca datasets yang ada pada excel
jumlah_hari = 50
dataset = pd.read_excel('datasets.xlsx', usecols='B')
awal = 60
saham = dataset.values[awal:awal+21]
harga = saham[0]
nilai = saham[1:11]
error = 0.1
forecast = []
for i in range(1, jumlah_hari+1):
    pop = populasi_awal()
    while gen < max_generation:
        gen += 1
        fit = [hitung_fitness(kromosom, saham) for kromosom in pop]
        pop = [x for _, x in sorted(zip(fit, pop), reverse=True)]
        fit = sorted(fit, reverse=True)

        if (fit[0] > error):
            break
        parent = parent_selection(pop, saham, fit)
        pop = regen_pop(pop, parent, pc)
    fit = [hitung_fitness(kromosom, saham) for kromosom in pop]
    pop = [x for _, x in sorted(zip(fit, pop), reverse=True)]
    best = pop[0]
    print('best kromosom hari ke-', i, ': ', best)
    harga_prediksi = round(harga_saham(best, saham[:10]))
    forecast += [[i, harga_prediksi,
                  int(saham[0]), int(abs(saham[0] - harga_prediksi))]]
    saham = dataset.values[awal-i:awal+21-i]
print('forecast harga saham: ', forecast)

# sebelum revisi
# pop = populasi_awal()
# print('Populasi Awal: ', pop)

# # Probabilitas operasi genetik (Pc dan Pm)
# pm = 1/(len(pop)*len(pop[0]))  # probabilitas mutasi = 1 / banyak gen
# pc = round(0.4 * max_pop)

# gen = 0
# # membaca datasets yang ada pada excel
# dataset = pd.read_excel('datasets.xlsx', usecols='B')
# awal = 20
# saham = dataset.values[awal:awal+21]
# harga = saham[0]
# nilai = saham[1:11]
# error = 1
# while gen < max_generation:
#     gen += 1
#     fit = [hitung_fitness(kromosom, saham) for kromosom in pop]
#     pop = [x for _, x in sorted(zip(fit, pop), reverse=True)]
#     fit = sorted(fit, reverse=True)
#     print(fit[0])
#     if (fit[0] > error):
#         break

#     parent = parent_selection(pop, saham, fit)

#     pop = regen_pop(pop, parent, pc)

# fit = [hitung_fitness(kromosom, saham) for kromosom in pop]
# pop = [x for _, x in sorted(zip(fit, pop), reverse=True)]

# print('Generasi: ', gen)
# print('Pilihan Kromosom Terbaik: ', pop[0])
# print('Prediksi Harga Saham: ', round(harga_saham(pop[0], saham[:10])))
