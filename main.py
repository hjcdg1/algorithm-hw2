from hw2 import *
import random

def make_out_seq(opt_seq, val_seq) :
    out_seq = []
    for opt, val in zip(opt_seq, val_seq):
        if opt == 0:
            out_seq.append(os_insert(val))
        elif opt == 1:
            out_seq.append(os_delete(val))
        elif opt == 2:
            out_seq.append(os_select(val))
        elif opt == 3:
            out_seq.append(os_rank(val))
    return out_seq

if __name__=="__main__":
    for k in range(0, 10) :
        init()
        opt_seq = []
        val_seq = []
        for i in range(0, 10) :
            opt_seq.append(random.randint(0, 3))
            val_seq.append(random.randint(1, 4))
        print("<"+str(k)+"th", "Random Test Case"+">")
        print("opt_seq :", opt_seq)
        print("val_seq :", val_seq)
        out_seq = make_out_seq(opt_seq, val_seq)
        print("out_seq :", out_seq)
        print("Check Result :", check(opt_seq, val_seq, out_seq))
        print()

    # 삽입 2, 삽입 5, 삽입 4, 삽입 3, 삭제 5, 삭제 2
    init()
    print("<Test Case 1 : Insert 2, Insert 5, Insert 4, Insert 3, Delete 5, Delete 2>")
    test1_opt_seq = [0, 0, 0, 0, 1, 1]
    test1_val_seq = [2, 5, 4, 3, 5, 2]
    print("opt_seq :", test1_opt_seq)
    print("val_seq :", test1_val_seq)
    test1_out_seq = make_out_seq(test1_opt_seq, test1_val_seq)
    print("out_seq :", test1_out_seq)
    print("Check Result :", check(test1_opt_seq, test1_val_seq, test1_out_seq))
    print()

    # 삽입 1, 삽입 2, 삽입 3, 삭제 1, 삽입 4
    init()
    print("<Test Case 2 : Insert 1, Insert 2, Insert 3, Delete 1, Insert 4>")
    test2_opt_seq = [0, 0, 0, 1, 0]
    test2_val_seq = [1, 2, 3, 1, 4]
    print("opt_seq :", test2_opt_seq)
    print("val_seq :", test2_val_seq)
    test2_out_seq = make_out_seq(test2_opt_seq, test2_val_seq)
    print("out_seq :", test2_out_seq)
    print("Check Result :", check(test2_opt_seq, test2_val_seq, test2_out_seq))
