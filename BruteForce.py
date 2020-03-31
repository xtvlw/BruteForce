#_[N_F]_
import time
password = int(input('password to test : '))
pos = 0
st = time.time()
while password != pos:
    pos += 1
fi = time.time()
di = fi - st
print('\nyour password is {}\nwas need {:.4f}S'.format(password, password))
