import sys

n = int(sys.stdin.readline())
n_cpy = n
t_list = [] 
    
t = input()
t_split = t.split(' ')
for i in range(len(t_split)):
    t_list.append(int(t_split[i]))

tp = input()
tp_split = tp.split(' ')
mt = int(tp_split[0])
mp = int(tp_split[1])

t_cnt = 0

for i in t_list:
    if(i!=0):
        if(i%mt != 0):
            t_cnt = t_cnt + (i//mt)+1
        else:
            t_cnt = t_cnt + (i//mt)

p_quo = n_cpy // mp
p_mod = n_cpy % mp

print(t_cnt)
print(p_quo,p_mod)