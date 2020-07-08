import light_control
import lightstate_get
import threading

def light_control_job():
    while True:
        light_control.coordinate_detection()

def lightstate_get_job():
    while True:
        lightstate_get.get_light_state()

    
def main():
    third_thread=threading.Thread(target=light_control_job,name='T3')
    third_thread.start()
    forth_thread=threading.Thread(target=lightstate_get_job,name='T4')
    forth_thread.start()

if __name__=='__main__':
    main()
