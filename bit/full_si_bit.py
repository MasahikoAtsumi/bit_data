import random
import numpy as np

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
                empty_data[id_ch][id_row][id_col] = random.randint(-32768, 32767)
    return empty_data


def create_data_m(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = random.randint(-32768, 0)
    return empty_data

def create_data_p(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = random.randint(0, 32767)
    return empty_data

def create_data_max(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = 32767
    return empty_data

def create_data_min(inchs, rows, cols):
    empty_data = np.zeros((inchs, rows, cols))
    for id_ch in range(0, inchs):
        for id_row in range(0, rows ):
            for id_col in range(0, cols ):
                empty_data[id_ch][id_row][id_col] = -32768
    return empty_data


def save_as_hex(in_data, upper_save_path, lower_save_path):
    u_f = open(upper_save_path, 'w')
    l_f = open(lower_save_path, 'w')
    for id_ch in range(0, len(in_data)):
        for id_row in range(0, len(in_data[id_ch])):
            for id_col in range(0, len(in_data[id_ch][id_row])):
                val = int(in_data[id_ch][id_row][id_col])
                if val < 0:
                    val = val & 0xffff
                hex = format(val, '04x')
                u_f.write('8\'h')
                u_f.write(hex[0:2])
                u_f.write(', ')
                l_f.write('8\'h')
                l_f.write(hex[2:4])
                l_f.write(', ')
            u_f.write('\n')
            l_f.write('\n')
    u_f.close()
    l_f.close()



s_path_d_up = '/d_upper.txt'
s_path_d_lw = '/d_lower.txt'
s_path_w0_up = '/w0_upper.txt'
s_path_w0_lw = '/w0_lower.txt'
s_path_ans = '/ans.txt'


# random
in_d_0 = create_data(8, 5, 5)
in_w_0 = create_data(8, 5, 5)
def_path = './ex1_random'
ans_0 = conv(in_d_0, in_w_0)
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()

# random > 0
in_d_0 = create_data_p(8, 5, 5)
in_w_0 = create_data_p(8, 5, 5)
def_path = './ex2_p'
ans_0 = conv(in_d_0, in_w_0)
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()



# random < 0
in_d_0 = create_data_m(8, 5, 5)
in_w_0 = create_data_p(8, 5, 5)
def_path = './ex3_m'
ans_0 = conv(in_d_0, in_w_0)
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()


# max
in_d_0 = create_data_max(8, 5, 5)
in_w_0 = create_data_max(8, 5, 5)
def_path = './ex4_max'
ans_0 = conv(in_d_0, in_w_0)
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()


# min
in_d_0 = create_data_max(8, 5, 5)
in_w_0 = create_data_min(8, 5, 5)
ans_0 = conv(in_d_0, in_w_0)
def_path = './ex5_min'
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()



# overflow
in_d_0 = create_data_min(8, 5, 5)
in_w_0 = create_data_min(8, 5, 5)
def_path = './ex6_overflow'
ans_0 = conv(in_d_0, in_w_0)
save_as_hex(in_d_0, def_path+s_path_d_up, def_path+s_path_d_lw)
save_as_hex(in_w_0, def_path+s_path_w0_up, def_path+s_path_w0_lw)
f = open(def_path+s_path_ans, 'w')
f.write("answer 0 : "+str(ans_0))
f.close()
