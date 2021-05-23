from random import randrange

def init():
    '''
    初始化门和门后的物品
    '''
    result = {i:'goat' for i in range(3)}
    r = randrange(3)
    result[r] = 'car'
    return result

def GAME():
    doors = init()
    while True:
        try:
            firstDoor = int(input('Choose a door to open:'))
            assert 0<=firstDoor<=2
            break
        except:
            print('Choose a door between {} and {}'.format('0','2'))
        
    for door in doors.keys()-{firstDoor}:
        if doors[door] == 'goat':
            print('goat behind the door',door)

            thirdDoor = (doors.keys()-{door,firstDoor}).pop()
            change = input('Switch to {}?(y/n)'.format(thirdDoor))
            finalDoor = thirdDoor if change == 'y' else firstDoor
            if doors[finalDoor] == 'goat':
                return 'You Lose!'
            else:
                return 'You Win!'

def start():
    while True:
        print('='*35)
        print(GAME())
        again = input('Do you want to try once more?(y/n)')
        if again == 'n':
            break
if __name__ == "__main__":
    start()
