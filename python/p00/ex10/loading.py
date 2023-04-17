import time

def draw(st, i, end, count, n):
    pt = time.time() - st
#    i += 1
    per = i * 100 / count 
    bar_size = int((i * 20) / count)
    un_bar = 20 - bar_size
    if not i: eta = pt * count
    else: eta = (pt / i) * count
    print("\rETA: {:6.2f}s [".format(eta) + "{:6.2f}%][".format(per) + ('=' * bar_size) + ">" + (' ' * un_bar) + "]",
            str(i + n) + "/" + str(end), "| elapsed time {:6.2f}s".format(pt), end='\0')

def ft_progress(n):
    if not isinstance(n, range): raise TypeError("Must be a range")
    st = time.time()
    end = n[0] + len(n)
    count = len(n)
    step = n[1] - n[0]
    draw(st, n[0], end, count, n[0])
    for i, number in enumerate(n):
        yield number
        draw(st, number + step, end, count, n[0] )

#listy = range(100,0,-1)
#listy = range(100,0,-1)
listy = range(100,200)
#listy = range(3333)
#listy = range(1000) 
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
