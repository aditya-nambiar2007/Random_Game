import random
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