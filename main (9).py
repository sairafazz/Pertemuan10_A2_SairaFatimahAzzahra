def cetak_matriks(matriks):
    for row in matriks:
        print(row)

def pjg_matriks(matriks):
    return len(matriks[0])

def lbr_matriks(matriks):
    return len(matriks)

def transpose_matriks(matriks_a):
    temp_mat = []

    for i in range(0, pjg_matriks(matriks_a)):
        temp_row = []
        for j in range(0, lbr_matriks(matriks_a)):
            temp_row.append(matriks_a[j][i])
        temp_mat.append(temp_row)

    return temp_mat

matriks_a = [[1, 2, 3, 5], [3, 4, 5, 6], [5, 6, 7, 8]]
matriks_b = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

print("matriks_a : ")
cetak_matriks(matriks_a)
print("transpose matriks_a : ")
trp_mat_a = transpose_matriks(matriks_a)
cetak_matriks(trp_mat_a)

print("\nmatriks_b : ")
cetak_matriks(matriks_b)
print("transpose matriks_b : ")
trp_mat_b = transpose_matriks(matriks_b)
cetak_matriks(trp_mat_b)


