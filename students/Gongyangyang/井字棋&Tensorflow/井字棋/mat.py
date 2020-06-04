import numpy as np

def mat(a):
    a1 = a # 行

    a2 = a1.swapaxes(0,1) # 列

    a3 = np.array([[a1[i][i],a1[a1.shape[0]-1-i][i]] for i in range(a1.shape[0])]).swapaxes(0,1) # 斜

    b= a1.tolist() + a2.tolist() + a3.tolist()

    for x in b:
        if 0 not in x :
            s = 'win'
            break
        s = ''
    return s

if __name__ == "__main__":
    a = np.array([[1,1,1],
                [0,0,0],
                [0,1,1]])
    print(mat(a))