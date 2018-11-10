n = 6
def g_0(n):
    return ('?',) * n

def s_0(n):
    return ('T',) * n

def more_general(h1,h2):
    c_h1 = 0
    c_h2 = 0
    #most_general = g_0(n)
    c_h1 += h1.count('?')
    c_h2 += h2.count('?')

    if (c_h1>c_h2):
        return  True

    return False

def min_generalization(h,x):
    h_gen =()
    for i in range(0,n):
        if (h[i]!=x[i]):
            h_gen += ('?',)
        else:
            h_gen += (x[i],)
    return h_gen

def min_specializations(h, domains, x):
    res_list = []
    h_list = []
    changed = False
    for i in range(0,len(domains)):
        if (h[i] != x[i]):
            for j in range(0,len(domains[i])):
                if (domains[i][j] != x[i]):
                    h_res = h
                    h_res_list = list(h_res)
                    h_res_list[i] = domains[i][j]
                    h_res_final = tuple(h_res_list)
                    res_list.append(h_res_final)
        else :
            h_res = h
            h_res_list = list(h_res)
            h_res_list[i] = 'T'
            h_res_final = tuple(h_res_list)
            res_list.append(h_res_final)
    return res_list
'''
def candidate_elimination(examples):
    G = g_0(n)
    S = s_0(n)
    for 
    for i in range(0,n):
        if (concept[i] = True):
            for j in range(0,len(S)):
                if ()
'''
def main():

    h1 = g_0(n)
    h2 = s_0(n)
    h3 = s_0(n-3)+g_0(3)
    h4 = s_0(n-2)+g_0(2)
    print(min_generalization(h1,h3))

    h_ex = ('?','x')
    domains = [['a', 'b', 'c'],['x','y']]
    x = ('b','x')
    print(min_specializations(h_ex,domains,x))

if __name__ == "__main__":
    main()