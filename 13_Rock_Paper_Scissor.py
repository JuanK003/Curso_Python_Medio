import random

def choose_options():
    
    options = ('Rock', 'Paper', 'Scissor')
    user_option = input('\nChoose => Rock, Paper or Scissor => ').capitalize()
    
    if not user_option in options:
        print('You chose wrong, try again')
        #continue
        return None, None
    
    machine = random.choice(options)

    print('User option =>', user_option)
    print('\nComputer option =>', machine)
    return user_option, machine

def check_rules(user_option, machine, user_wins, machine_wins):
    
    if user_option == machine:
        print('\nYou Tied!')
            
    elif user_option == 'Rock':
        if machine == 'Scissor':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
                
    elif user_option == 'Paper':
        if machine == 'Rock':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
                
    elif user_option == 'Scissor':
        if machine == 'Paper':
            print('\nYou Win!')
            user_wins += 1
        else:
            print('\nYou Lost!')
            machine_wins += 1
    
    return user_wins, machine_wins

def check_winner(user_wins, machine_wins):
    if machine_wins == 2:
        print('\n\t\t\tThe winner is => MACHINE!')  
        print('Machine wins =>', machine_wins)
        print('User wins =>', user_wins)
        exit()
            
    if user_wins == 2:
        print('\n\t\t\tThe winner is => YOU!')
        print('Machine wins =>', machine_wins)
        print('User wins =>', user_wins)  
        exit()

def run_game():
    
    machine_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('=' * 65)
        print('\t\t\tROUND # ', rounds )
        print('=' * 65)
        
        print('\nMachine wins =>', machine_wins)
        print('\nUser wins =>', user_wins)
        
        rounds += 1
        
        user_option, machine = choose_options()
        
        user_wins, machine_wins = check_rules(user_option, machine, user_wins, machine_wins)
        
        check_winner(user_wins, machine_wins)
    
run_game()