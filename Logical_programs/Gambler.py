import random

def gambler(stake, goal):
    """
    function for gambler problem
    :param stake: the amount that user have
    :param goal: the goal amount
    :return: number of wins and result
    """
    win_count = 0
    loss_count = 0
    trails = 0
    if stake <= 0:
        print("player didn't have any money ")
    else:
        while 0 < stake < goal:
            play = random.randint(0, 1)
            if play == 0:
                stake += 1
                win_count += 1
                trails += 1
            else:
                stake -= 1
                loss_count +=1
                trails += 1
        if stake <= 0:
            print("player goes broke and loss percentage is", loss_count/trails * 100)
        else:
            print("player reach goal")
        return win_count/trails * 100


if __name__ == "__main__":
    stake_input = int(input("Please enter stake amount"))
    goal_input = int(input("Please enter goal amount"))
    result = gambler(stake_input, goal_input)
    print("Player wins and win percentage is:", result)

