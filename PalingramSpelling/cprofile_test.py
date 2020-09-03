import cProfile
import palingrams
cProfile.run('palingrams.find_palingrams()')

'''
Profiling with time:
-----------------
Another way to time the program is to use time.time(), which returns an epoch timestamp- the number of seconds since 12AM on Jan 1, 1970
UTC ( the Unic epoch). 
'''