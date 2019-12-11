"""
ChemMath HW3-1
"""
import numpy as np
import decimal


def P_H_C_D_P(_g, P, a):
    H = H0 + _g * P
    w, v = np.linalg.eigh(H)
    C_occ = v[:, 0:3]  # 第1, 2, 3個 eigenvector。請記得 Python 從 0 開始數。
    D = C_occ@(C_occ.T.conjugate())
    P_new = np.diag(D.diagonal())
    P_new = a * P_new + (1 - a) * P

    return P_new


def scf(_method, _a, _g):
    max_iter = 10000  # 設定一個很大的圈數
    P_old = np.zeros([6, 6])  # 開一個空的矩陣當作 Initial Guess

    # For original case
    if _method == 'Non-damping Method':
        for i in range(max_iter):  # i會記錄迴圈跑幾圈
            P_new = P_H_C_D_P(_g, P_old, 1)  # 代入舊的 P_old，得到新的 P_new
            dP = (P_new - P_old)  # 計算兩個 P 矩陣的差異
            err = np.max(np.abs(dP))  # 計算這些 diagonal element 的最大差距
            if err < 1e-10:  # 如果跟上一圈的差距足夠小了，就當作收斂了
                print("SCF Converged.")
                break
            else:
                P_old = P_new  # 把 P_old 直接用 P_new 覆蓋，準備進入下一圈
        return i, err  # 把 圈數 和 err 丟出來

    # For damping method
    elif _method == 'Damping Method':
        for i in range(max_iter):  # i會記錄迴圈跑幾圈
            P_new = P_H_C_D_P(_g, P_old, _a)  # 代入舊的 P_old，得到新的 P_new
            dP = (P_new - P_old)  # 計算兩個 P 矩陣的差異
            err = np.max(np.abs(dP))  # 計算這些 diagonal element 的最大差距
            if err < 1e-10:  # 如果跟上一圈的差距足夠小了，就當作收斂了
                # print("SCF Converged.")
                break
            else:
                P_old = P_new  # 把 P_old 直接用 P_new 覆蓋，準備進入下一圈
        return i, err  # 把 圈數 和 err 丟出來


# Initial parameter
H0 = np.diag(-np.ones(5), k=-1) + np.diag(-np.ones(5), k=1)
H0[0, 0] = -1
H0[5, 0] = -1
H0[0, 5] = -1
gamma = [3, 10, 100]

# Main part
'''
i, err = scf('Non-damping Method', 1)
# 不管有沒有收斂，離開迴圈後用 print 顯示結果
print('Non-damping Method:')
print(i, err)
'''

# For different alpha
print('Damping Method')
for g in gamma:
    print('gamma:\t%d' % g)
    print('Alpha\tIterations\tConvergence')
    alpha = np.linspace(0, 1, 50)
    for a in alpha:
        iteration, err = scf('Damping Method', a, g)
        print('%.2f\t%d\t\t\t%.2E' % (a, iteration, decimal.Decimal(err)))

print('Work Done!! Go buy some drink and enjoy the New years eve!!')
