from typing import Any
import pandas as pd
import numpy as np

ipkBurukmin = 0
ipkBurukmax = 2.75

ipkCukupmin = 2
ipkCukupmax = 3.25

ipkBagusmin = 2.75
ipkBagusmax = 4.00

gajiKecilmin = 0
gajiKecilmax = 3

gajiSedangmin = 1
gajiSedangmax = 6

gajiBesarmin = 4
gajiBesarmax = 12

gajiSangatBesarmin = 7
gajiSangatBesarmax = 1001

df = pd.read_excel('masukan.xlsx')


def inRange(minimal, maximal, input):
    minimal = min(minimal, maximal)
    maximal = max(minimal, maximal)

    # print minimal
    # print maximal

    if((input > minimal) and (input < maximal)):
        return 1
    else:
        return 0


def fuzzyRules(ipk, gaji):
    global nilaikelulusanrendah
    global nilaikelulusantinggi

    nilaikelulusanrendah = 0
    nilaikelulusantinggi = 0

    ipkBuruk = inRange(ipkBurukmin, ipkBurukmax, ipk)
    ipkCukup = inRange(ipkCukupmin, ipkCukupmax, ipk)
    ipkBagus = inRange(ipkBagusmin, ipkBagusmax, ipk)

    gajiKecil = inRange(gajiKecilmin, gajiKecilmax, gaji)
    gajiSedang = inRange(gajiSedangmin, gajiSedangmax, gaji)
    gajiBesar = inRange(gajiBesarmin, gajiBesarmax, gaji)
    gajiSangatBesar = inRange(gajiSangatBesarmin, gajiSangatBesarmax, gaji)

    nkrendah_array = []
    nktinggi_array = []

    if ipkBuruk == 1 and gajiKecil == 1:
        print("Rule 1 : IPK Buruk dan Gaji Kecil")
        derajatkelulusanrendah = min(derajatipkburuk, derajatgajikecil)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkBuruk == 1 and gajiSedang == 1:
        print("Rule 2 : IPK Buruk dan Gaji Sedang")
        derajatkelulusanrendah = min(derajatipkburuk, derajatgajisedang)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = min(derajatipkburuk, derajatgajisedang)
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkBuruk == 1 and gajiBesar == 1:
        print("Rule 3 : IPK Buruk dan Gaji besar")
        derajatkelulusanrendah = min(derajatipkburuk, derajatgajibesar)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkBuruk == 1 and gajiSangatBesar == 1:
        print("Rule 4 : IPK Buruk dan Gaji sangatbesar")
        derajatkelulusanrendah = min(derajatipkburuk, derajatgajisangatbesar)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkCukup == 1 and gajiKecil == 1:
        print("Rule 5 : IPK Cukup dan Gaji Kecil")
        derajatkelulusantinggi = min(derajatipkcukup, derajatgajikecil)
        print("Derajat Kelulusan Tinggi ", derajatkelulusantinggi)
        nilaikelulusantinggi = derajatkelulusantinggi
        nktinggi = nktinggi_array.append(nilaikelulusantinggi)

    if ipkCukup == 1 and gajiSedang == 1:
        print("Rule 6 : IPK Cukup dan Gaji Sedang")
        derajatkelulusanrendah = min(derajatipkcukup, derajatgajisedang)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkCukup == 1 and gajiBesar == 1:
        print("Rule 7 : IPK Cukup dan Gaji Besar")
        derajatkelulusanrendah = min(derajatipkcukup, derajatgajibesar)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkCukup == 1 and gajiSangatBesar == 1:
        print("Rule 8 : IPK Cukup dan Gaji Sangat Besar")
        derajatkelulusanrendah = min(derajatipkcukup, derajatgajisangatbesar)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = derajatkelulusanrendah
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if ipkBagus == 1 and gajiKecil == 1:
        print("Rule 9 : IPK Bagus dan Gaji Kecil")
        derajatkelulusantinggi = min(derajatipkbagus, derajatgajikecil)
        print("Derajat Kelulusan Tinggi ", derajatkelulusantinggi)
        nilaikelulusantinggi = derajatkelulusantinggi
        nktinggi = nktinggi_array.append(nilaikelulusantinggi)

    if ipkBagus == 1 and gajiSedang == 1:
        print("Rule 10 : IPK Bagus dan Gaji Sedang")
        derajatkelulusantinggi = min(derajatipkbagus, derajatgajisedang)
        print("Derajat Kelulusan Tinggi ", derajatkelulusantinggi)
        nilaikelulusantinggi = derajatkelulusantinggi
        nktinggi = nktinggi_array.append(nilaikelulusantinggi)

    if ipkBagus == 1 and gajiBesar == 1:
        print("Rule 11 : IPK Bagus dan Gaji Besar")
        derajatkelulusantinggi = min(derajatipkbagus, derajatgajibesar)
        print("Derajat Kelulusan Tinggi ", derajatkelulusantinggi)
        nilaikelulusantinggi = derajatkelulusantinggi
        nktinggi = nktinggi_array.append(nilaikelulusantinggi)

    if ipkBagus == 1 and gajiSangatBesar == 1:
        print("Rule 12 : IPK Bagus dan Gaji Sangat Besar")
        derajatkelulusanrendah = min(derajatipkbagus, derajatgajisangatbesar)
        print("Derajat Kelulusan Rendah ", derajatkelulusanrendah)
        nilaikelulusanrendah = min(derajatipkbagus, derajatgajisangatbesar)
        nkrendah = nkrendah_array.append(nilaikelulusanrendah)

    if nilaikelulusantinggi == 0:
        nilaikelulusantinggi = 0
    else:
        nilaikelulusantinggi = max(nktinggi_array)

    if nilaikelulusanrendah == 0:
        nilaikelulusanrendah = 0
    else:
        nilaikelulusanrendah = max(nkrendah_array)

    print
    print("Nilai Kelulusan Rendah : ", nilaikelulusanrendah)
    print("Nilai Kelulusan Tinggi : ", nilaikelulusantinggi)


def centroidMethod(nilaikelulusanrendah, nilaikelulusantinggi):

    global hasil
    hasil = (((10+20+30+40+50+60)*nilaikelulusanrendah)+((70+80+90+100) *
             nilaikelulusantinggi))/((6*nilaikelulusanrendah)+(4*nilaikelulusantinggi))
    print("Nilai Kelulusan : ", hasil)
    return hasil


def fungsiKeanggotaanSegitiga(a, b, c, x):

    if ((x > a) and (x < b)):
        derajatKeanggotaan = (x-a)/(b-a)

    elif (x == b):
        derajatKeanggotaan = 1

    elif ((x > b) and (x < c)):

        derajatKeanggotaan = -((x-c)/(c-b))

    else:
        derajatKeanggotaan = 0

    return derajatKeanggotaan


def fungsiKeanggotaanTrapesium(a, b, c, d, x):

    if ((x > a) and (x < b)):
        derajatKeanggotaan = (x-a)/(b-a)

    elif ((x >= b) and (x <= c)):
        derajatKeanggotaan = 1

    elif ((x > c) and (x < d)):
        derajatKeanggotaan = -((x-d)/(d-c))

    else:
        derajatKeanggotaan = 0

    return derajatKeanggotaan


def derajatIpk(ipk):

    global derajatipkburuk
    global derajatipkcukup
    global derajatipkbagus

    derajatipkburuk = fungsiKeanggotaanTrapesium(
        ipkBurukmin, ipkBurukmin, 2, ipkBurukmax, ipk)
    derajatipkcukup = fungsiKeanggotaanSegitiga(
        ipkCukupmin, 2.75, ipkCukupmax, ipk)
    derajatipkbagus = fungsiKeanggotaanTrapesium(
        ipkBagusmin, 3.25, ipkBagusmax, ipkBagusmax, ipk)

    print("Derajat IPK Buruk : ", derajatipkburuk)
    print("Derajat IPK Cukup : ", derajatipkcukup)
    print("Derajat IPK Bagus : ", derajatipkbagus)


def derajatGaji(gaji):

    global derajatgajikecil
    global derajatgajisedang
    global derajatgajibesar
    global derajatgajisangatbesar
    global derajatgajibesar

    derajatgajikecil = fungsiKeanggotaanTrapesium(
        gajiKecilmin, gajiKecilmin, 1, gajiKecilmax, gaji)
    derajatgajisedang = fungsiKeanggotaanTrapesium(
        gajiSedangmin, 3, 4, gajiSedangmax, gaji)
    derajatgajibesar = fungsiKeanggotaanTrapesium(
        gajiBesarmin, 6, 7, gajiBesarmax, gaji)
    derajatgajisangatbesar = fungsiKeanggotaanTrapesium(
        gajiSangatBesarmin, 12, gajiSangatBesarmax, gajiSangatBesarmax, gaji)

    print("Derajat Gaji Kecil        : ", derajatgajikecil)
    print("Derajat Gaji Sedang       : ", derajatgajisedang)
    print("Derajat Gaji besar        : ", derajatgajibesar)
    print("Derajat Gaji Sangat Besar : ", derajatgajisangatbesar)


def main():

    from time import time

    data = []
    n = df.No.count()  # int(input("Masukkan jumlah data : "))

    for i in range(0, n):

        ipk = df.IPK[i]  # float(input("Masukkan IPK Anda : "))
        gaji = df.Gaji[i]  # float(input("Masukkan gaji anda : "))
        t0 = time()

        print("\n==========  PROSES FUZZYFICATION   ==========\n")
        print("\n========== Derajat Keanggotaan IPK ==========\n")
        dIpk = derajatIpk(ipk)

        print("\n========== Derajat Keanggotaan Gaji ==========\n")
        dGaji = derajatGaji(gaji)

        print("\n========== PROSES INTERFERENCES ==========\n")
        fuzzyRules(ipk, gaji)

        print("\n========== PROSES DEFUZZYFICATION ==========\n")

        DEFUZZYFICATION = centroidMethod(
            nilaikelulusanrendah, nilaikelulusantinggi)
        print(DEFUZZYFICATION)
        DEFUZZY = data.append(DEFUZZYFICATION)
        t1 = time() - t0
        print("Waktu Eksekusi Fuzzy = ", t1)

    row = 0
    column = 0
    c = sorted(data, reverse=True)
    print(c)
    print("data paling besar adalah : ", max(data))
    datfra = pd.DataFrame()
    datfra['Nilai Kelulusan'] = c[0:10]
    datfra.to_excel('luaran.xlsx', index=False)

    return 0


if __name__ == "__main__":
    main()
