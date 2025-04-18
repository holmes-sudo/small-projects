import random

score = {'tie': 0, 'win': 0, 'lose': 0}
valid_options = {'r':'rock','p':'paper','s':'scissors'}

def generate_computers_move():
    # making computers move.
    MOVES = ['rock', 'paper', 'scissors']
    random_number = random.randint(0,2)

    return MOVES[random_number]

def evaluate_winner(users_move, computers_move):
    print(f'inside evaluate_winner, inputs: user-{users_move}  computer-{computers_move}')
    if users_move == computers_move:
        score["tie"] =  score["tie"] + 1
        print(f"Its a tie!!! \nYour move: {users_move} \nComputers move: {computers_move}")
        #user will wins if.
    elif users_move =='rock' and computers_move=='scissors':
        score["win"] = score["win"] + 1
        print(f"You win!!! \nYour move: {users_move} \nComputers move: {computers_move}")
    elif users_move == 'paper' and computers_move=='rock':
        score["win"] = score["win"] + 1
        print(f"You win!!! \nYour move: {users_move} \nComputers move: {computers_move}")
    elif users_move == 'scissors' and computers_move=='paper':
        score["win"] = score["win"] + 1
        print(f"You win!!! \nYour move: {users_move} \nComputers move: {computers_move}")
        #user loose if
    elif users_move =='rock' and computers_move=='paper':
        score["lose"] = score["lose"] + 1
        print(f"You lost!!! \nYour move: {users_move} \nComputers move: {computers_move}")
    elif users_move =='paper' and computers_move=='scissors':
        score["lose"] = score["lose"] + 1
        print(f"You lost!!! \nYour move: {users_move} \nComputers move: {computers_move}")
    elif users_move == 'scissors' and computers_move=='rock':
        score["lose"] = score["lose"] + 1
        print(f"You lost!!! \nYour move: {users_move} \nComputers move: {computers_move}")


def main():
    while True:
        print('welcome to the game of rock,paper,scissors type')
        print(" 'R' => Rock \n 'P' => Paper \n 'S' => Sciccors \n 'Q' => Quit")

        users_move = input().lower()

        if users_move.isalpha():
        
            if users_move=='q':
                print('''============================\n============================\n============================''')
                print(f'you have ({score["win"]} wins) ({score["lose"]} loose) and ({score["tie"]} ties) ')
                break

            if users_move in valid_options:
                users_move = valid_options[users_move]
                print(f'You played {users_move}')

                computers_move = generate_computers_move()

                evaluate_winner(users_move, computers_move)
            else:
                print("Please type: \n 'R' => Rock \n 'P' => Paper \n 'S' => Sciccors 'Q' => Quit")
                continue
        else:
            print("Please type: \n 'R' => Rock \n 'P' => Paper \n 'S' => Sciccors 'Q' => Quit")
            continue


if __name__ == "__main__":                
    main()