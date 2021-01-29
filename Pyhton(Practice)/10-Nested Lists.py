if __name__ == '__main__':
    dictr = {}
    s= list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dictr:
            dictr[score].append(name)
        else:
            dictr[score] = [name]   
        if score not in s:
            s.append(score)
    m = min(s)
    s.remove(m) 
    m1= min(s) 
    dictr[m1].sort()
    for i in dictr[m1]:
        print(i)
                
                 