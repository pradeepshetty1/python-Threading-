##from threading import Thread
##import time
##
##def timer(name,delay,repeat):
##    print("Timer:" + name + "started")
##    while repeat >0:
##        time.sleep(delay)
##        print (name + ":" +str(time.ctime(time.time())))
##        repeat -=1
##    print "Timer:" +name+"completed"
##
##
##
##def Main():
##    t1 = Thread(target=timer,args=("Timer1",1,5))
##    t2 = Thread(target=timer,args=("Timer2",2,5))
##    t1.start()
##    t2.start()
##
##    print "Main completed"
##
##
##if __name__ == '__main__':
##    Main()


##
##from threading import Thread
##import time
##
##def data():
##    for info in range(15):
##        time.sleep(1)
##        print "This is data"
##
##def data1():
##    for info in range(15):
##        time.sleep(1)
##        print "This is data1"
##
##print "\n"
##print "data printed"
##
##t = time.time()
##
##t1 = Thread(target = data)
##t2 = Thread(target = data1)
##t1.start()
##t1.join()
##
##t2.start()
##t2.join()
##print time.time()-t


# import time
#
# def data3():
#     for info in range(15):
#         time.sleep(1)
#         print "This is data3"
#
#
# def data4():
#     for info in range(15):
#         time.sleep(1)
#         print "This is data4"
#
# t = time.time()
#
# data3()
#
# print "\n"
# data4()
#
# print time.time()-t
#


        




