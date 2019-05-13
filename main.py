from hw2 import *
import random

if __name__=="__main__":
    for k in range(0, 10) :
        init()
        opt_seq = []
        val_seq = []
        out_seq = []
        for i in range(0, 50) :
            opt_seq.append(random.randint(0, 3))
            val_seq.append(random.randint(1, 9999))
        print(str(k)+"th", "Random Test Case")
        print(opt_seq)
        print(val_seq)

        for opt, val in zip(opt_seq, val_seq):
            if opt == 0:
                out_seq.append(os_insert(val))
            elif opt == 1:
                out_seq.append(os_delete(val))
            elif opt == 2:
                out_seq.append(os_select(val))
            elif opt == 3:
                out_seq.append(os_rank(val))

        if check(opt_seq, val_seq, out_seq) == False :
            print("Wrong Test Case Found! Fix this!")
            exit()
        print()
    print("No Wrong Test Cases! Good!")
