class Lists:
    def change_pos(self,my_list):
        print(f'original list:{my_list}')
        for i in range(0, len(my_list), 2):
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

        print(f'list after swapping:{my_list}')


my_list = [0, 1, 2, 3, 4, 5]
l1=Lists()
l1.change_pos(my_list)