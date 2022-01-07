class Phone:
    def __init__(self,screen,camera,androidversion):
        self.screen=screen
        self.camera=camera
        self.androidversion=androidversion

    def display(self):
        print(f'mobile screen is:{self.screen}'
              f'mobile camera is :{self.camera}'
              f'mobile androidversion:{self.androidversion}')


scr=input("enter mobile screen type:")
cam=int(input("enter input in camera in mp:"))
and_ver=int(input("android version of your phone:"))

mobile_phone=Phone(scr,cam,and_ver)
mobile_phone.display()

