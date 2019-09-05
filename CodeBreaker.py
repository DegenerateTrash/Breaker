def setcode():
    code = int(input("Code: "))
    return code

def main():
    import time
    import random
    code = setcode()
    start = time.time()
    for i in range(0,code+1,1):
        if code == i:
            print('It took {0:0.1f} seconds to crack the code {1} using for loop'.format(time.time() - start, code))
    start = time.time()
    attempt = 0
    while not code == attempt:
        attempt = random.randint(1000,9999)
    print('It took {0:0.1f} seconds to crack the code {1} using random'.format(time.time() - start, code))
    return
main()
