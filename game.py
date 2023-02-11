import random
print('RULES : ')
print('1. Enter A Random Number Between 1 and 5.')
print('2. The Computer Will Return A Random Number In Return')
print('3. If The Number Picked By You And The Computer Are Equal, The Game Ends . Otherwise The Number Picked By You Is Added To The Score \n')
score=0
while 1 :
    i=int( input() )
    print('\n')
    rand=int( random.random()*5+1 )
    if 0<i<6 :
        print(str(rand) + '\n')
        if i==rand:
            print('->GAME OVER \n SCORE : '+ str(score) + "\n")
            break
        else :
            score+=i
            print('SCORE : '+ str(score) +"\n")
    else:
        print('Invalid Number. Number must be an integer between 1 and 5 \n')  
