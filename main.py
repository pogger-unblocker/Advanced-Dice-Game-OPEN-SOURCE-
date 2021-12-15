#Made by Daniel D., I commented cuz I was bored in class.


import random
import os     #imports the essentials
import time
global win, lose, ties, streak, streakL #assigns the variables with the global attribute

win = 0    
lose = 0  # this area resets the variables on start
ties = 0
streak = 0
streakL = 0
idk = 'Made'
idk1 = 'By'
gamerun = 'PoggerUnblocker'
def clear():  #this defines the clear command
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)
def system():      #this defines the main frame
  global win, Ppoint, Aip, lose, ties, streak, streakL #this checks if the variables are global
  posNum = [1, 2, 3, 4, 5, 6] #this sets up the ai and player systems
  def addai(a, b, c):         
    return (a + b + c)
  def addP(x, y, z):
    return (x + y + z)
  global a, b, c
  a = random.choice(posNum)
  b = random.choice(posNum)  #this makes the ai points random
  c = random.choice(posNum)
  Aip = (addai(a, b, c))
  print(f'{idk} {idk1} {gamerun}')
  print(' ')
  print(' ')
  print(f'Your win streak is {streak}') #all the prints below are the text for menu
  print(f'Your loss streak is {streakL}')
  print(f'You have {win} wins this session')
  print(f'You have {lose} losses this session')
  print(f'You have {ties} ties this session')
  print('____________________________')
  print(' ')
  print('You are in a building, and the only way to leave is to get 10 wins')
  print(' ')
  start = str(input(f'Say (e) to roll, or say (f) if you have 10 wins ')) #creates the roll start
  if start == 'e':
    global chal
    clear()
    names = ['Daniel', 'Noah', 'Logan', 'Isaiah', 'Kirby', 'GitHub', 'UrMom', 'Ivan', 'Luke', 'Jacob', 'Brian', 'Tracy', 'Austin', 'Camille', 'Jose', 'Nikacado Avocado', 'Tryhard']  #In here are the enemy names
    chal = random.choice(names)
    print(f'You Challenge {chal}!')
    global x, y, z
    print('__________________________')
    x = random.choice(posNum)
    y = random.choice(posNum)   #this makes the player dice random
    z = random.choice(posNum)
    Ppoint = (addP(x, y, z))
  elif start == 'f' and win >= 1:
    clear()
    print('The guards are scared of your luck, so they let you go.') #win text
    time.sleep(2.5)
    clear()
    print('Thanks for playing.')
    time.sleep(0.1)
    print(' ')
    print(' ')
    print('Game made with 132 lines of code only.')
    time.sleep(99999)
  elif start == 'f' and win <= 10:
    clear()
    print('The guards knock you out...') #lose text
    time.sleep(9999999)
  else:
    print('error')
    time.sleep()
  if Ppoint > Aip:         #checks if you won         #below this is all the text for the dice part of game
    print(f'You rolled {x}, and {y}, and {z}')
    time.sleep(1)
    print(f'In total you got {Ppoint} points')
    time.sleep(1)
    print('__________________________')
    print(' ')
    print('_____________________________')
    print(f'{chal} rolled {a}, and {b}, and {c}')
    time.sleep(1)
    print(f'In total {chal} got {Aip} points')
    print('____________________________')
    time.sleep(1)
    print(' ')
    win = win + 1 
    streakL = 0  #changes wins, streak, etc variables
    streak = streak + 1
    print('You win!')
  elif Aip > Ppoint: #checks if you lost
    print(f'You rolled {x}, and {y}, and {z}')
    time.sleep(1)
    print(f'In total you got {Ppoint} points')
    time.sleep(1)
    print('__________________________')
    print(' ')
    print('_____________________________')
    print(f'{chal} rolled {a}, and {b}, and {c}')
    time.sleep(1)
    print(f'In total {chal} got {Aip} points')
    print('____________________________')
    time.sleep(1)
    print(' ')
    lose = lose + 1
    streakL = streakL + 1
    streak = 0
    print('You Lost!')
  elif Aip == Ppoint:
    print(f'You rolled {x}, and {y}, and {z}')
    time.sleep(1)
    print(f'In total you got {Ppoint} points')
    time.sleep(1)
    print('__________________________')
    print(' ')
    print('_____________________________')
    print(f'{chal} rolled {a}, and {b}, and {c}')
    time.sleep(1)
    print(f'In total {chal} got {Aip} points')
    print('____________________________')
    time.sleep(1)
    print(' ')
    ties = ties + 1
    print('Tie!')
  else:
    print('error')
  print(' ')
  print(' ')
  startOver = str(input('Say (e) for menu; Say (f) to give up '))  #e for menu text is here
  if startOver == 'e':
    clear()
    system()
  elif startOver == 'f':
    clear()
    time.sleep(0.25)
    print('The guards knock you out, once and for all...') #This is the text that shows when you press f
    time.sleep(999999)
  else:
    clear()  #once again, all these "clear" functions, clear the console.
    time.sleep(0.2)
    print('The guards make fun of you for making a typo as they beat you up lol')  #if you misspell LOL
    time.sleep(999999)
system()

