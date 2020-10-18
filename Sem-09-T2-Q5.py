def preencher_array(dim_0, dim_1, dim_2):
    dim_i = []
    for i in range(dim_0):
        dim_j = []
        for j in range(dim_1):
            dim_k = []
            for k in range(dim_2):
                dim_k.append(i+k+j)
            dim_j.append(dim_k)
        dim_i.append(dim_j)
    return dim_i

a = preencher_array(5, 7, 3)
for i in range(len(a)):
    print(a[i])
