import random

options=['rock','paper','scissors']

exit=False
comp_score,user_score=0,0
while exit==False:
    user_input=input('enter rock, paper, paper,scissors or exit ').lower()
    comp=random.choice(options)

    if user_input=='exit':
        if comp_score and user_score!=0:
            print(f'Your score is {user_score} and computer score is {comp_score}')
        print("Bye...")
        exit=True


    elif comp=='rock':
        if user_input=='paper':
            print('Computer input is ',comp)
            print('You win!')
            user_score+=1

        elif user_input=='rock':
            print('Computer input is ',comp)
            print('It is a tie')

        elif user_input=='scissors':
            print('Computer input is ',comp)
            print('Computer wins')
            comp_score+=1

    elif comp=='paper':
        if user_input=='paper':
            print('Computer input is ',comp)
            print('It is a tie')

        elif user_input=='scissors':
            print('Computer input is ',comp)
            print('You win')
            user_score+=1

        elif user_input=='rock':
            print('Computer input is ',comp)
            print('Computer wins')
            comp_score+=1

    elif comp=='scissors':
        if user_input=='paper':
            print('Computer input is ',comp)
            print('Computer wins')
            comp_score+=1

        elif user_input=='rock':
            print('Computer input is ',comp)
            print('You win')
            user_score+=1

        elif user_input=='scissors':
            print('Computer input is ',comp)
            print('It is a tie')

    else:
        print('Invalid Input')










