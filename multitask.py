import time
import threading

def brushteeth():
    for i in range(10):
        print('กำลังแปรงฟันอยู่...')
        time.sleep(0.5)

def shower():
    for i in range(10):
        print('กำลังอาบน้ำ')
        time.sleep(1)

# เด็กชายดำ ใช้เวลา 15 วินาทีในการเตรียมตัว
print('-----------ดช.ดำ------------')
t1 = time.time()
brushteeth()
shower()
t2 = time.time()
print(t2-t1)
print('-----------ดช.แดง------------')

t1 = time.time()
task1 = threading.Thread(target=brushteeth)
task2 = threading.Thread(target=shower)


task1.start()
task2.start()
task1.join()
task2.join()
print('---เวลาทั้งหมด---')
t2 = time.time()
print(t2-t1)