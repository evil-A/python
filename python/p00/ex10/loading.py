import time

def ft_progress(n):
    for number in n:
        if (number == 0):
            st = time.time()
        pt = time.time() - st
        anum = number + 1
        per = anum * 100 / (len(n))
        bar_size = int(anum * 20 / (len(n)))
        un_bar = 20 - bar_size
        num = str(anum)
        eta = (pt / anum) * len(n) 
        print("\rETA: {:.2f}s [".format(eta) + " {:.2f}%][".format(per) + ('=' * bar_size) + ">" + (' ' * un_bar) + "]",
                num + "/" + str(len(n)), "| elapsed time {:.2f} s".format(pt), end='\0')
        yield number
'''
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
'''

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
