import numpy as np
import random
np.set_printoptions(formatter={'int':hex})

def conv(in_data, weight):
    ans = 0
    tmp = 0
    for id_ch in range(0, len(in_data)):
        for id_row in range(0, len(in_data[id_ch])):
            for id_col in range(0, len(in_data[id_ch][id_row])):
                tmp = in_data[id_ch][id_row][id_col]*weight[id_ch][id_row][id_col]
                ans += tmp
    return ans

def create_data(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = random.randint(0, 255)
    return empty_data

def create_data_max(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = 255
    return empty_data

def create_data_min(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = 0
    return empty_data


def save_as_hex(in_data, save_path):

    f = open(save_path, 'w')

    for id_ch in range(0, len(in_data)):
        for id_row in range(0, len(in_data[id_ch])):
            for id_col in range(0, len(in_data[id_ch][id_row])):
                val = int(in_data[id_ch][id_row][id_col])
                f.write('8\'h')
                f.write(format(val, '02x'))
                f.write(', ')
            f.write('\n')
    f.close()

s_path_d0 = './d0.txt'
s_path_d1 = './d1.txt'
s_path_w0 = './w0.txt'
s_path_w1 = './w1.txt'
s_path_w2 = './w2.txt'
s_path_w3 = './w3.txt'

s_path_ans = './ans.txt'


# random
in_d_0 = create_data(8, 5, 5)
in_d_1 = create_data(8, 5, 5)
in_w_0 = create_data(8, 5, 5)
in_w_1 = create_data(8, 5, 5)
in_w_2 = create_data(8, 5, 5)
in_w_3 = create_data(8, 5, 5)


"""
# max
in_d_0 = create_data_max(8, 5, 5)
in_d_1 = create_data_max(8, 5, 5)
in_w_0 = create_data_max(8, 5, 5)
in_w_1 = create_data_max(8, 5, 5)
in_w_2 = create_data_max(8, 5, 5)
in_w_3 = create_data_max(8, 5, 5)
"""

"""
# min
in_d_0 = create_data_min(8, 5, 5)
in_d_1 = create_data_min(8, 5, 5)
in_w_0 = create_data_min(8, 5, 5)
in_w_1 = create_data_min(8, 5, 5)
in_w_2 = create_data_min(8, 5, 5)
in_w_3 = create_data_min(8, 5, 5)
"""

ans_0 = conv(in_d_0, in_w_0)
ans_1 = conv(in_d_1, in_w_1)
ans_2 = conv(in_d_0, in_w_2)
ans_3 = conv(in_d_1, in_w_3)

save_as_hex(in_d_0, s_path_d0)
save_as_hex(in_d_1, s_path_d1)
save_as_hex(in_w_0, s_path_w0)
save_as_hex(in_w_1, s_path_w1)
save_as_hex(in_w_2, s_path_w2)
save_as_hex(in_w_3, s_path_w3)

ans_0_1 = int(ans_0 + ans_1)
ans_2_3 = int(ans_2 + ans_3)
f = open(s_path_ans, 'w')
f.write("answer 0 + 1: "+str(ans_0_1))
f.write('\n')
f.write("answer 2 + 3: "+str(ans_2_3))
f.close()
