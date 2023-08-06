import random


def fiftyfifty(alst, calst, i):
    ranswr = calst[i]
    ranswr_idx = alst[i].index(ranswr)
    answr_choice_idx = random.randint(0, 3)
    if answr_choice_idx == ranswr_idx:
        return fiftyfifty(alst, calst, i)
    else:
        if answr_choice_idx < ranswr_idx:
            print(
                f"\nHere are the answers:\n\t{alst[i][answr_choice_idx]}\n\t{alst[i][ranswr_idx]}"
            )
            blst = [alst[i][ranswr_idx], alst[i][answr_choice_idx]]
            alst[i].clear()
            alst[i].append(blst[1])
            alst[i].append(blst[0])
        else:
            print(
                f"\nHere are the answers:\n\t{alst[i][ranswr_idx]}\n\t{alst[i][answr_choice_idx]}"
            )
            blst = [alst[i][ranswr_idx], alst[i][answr_choice_idx]]
            alst[i].clear()
            alst[i].append(blst[0])
            alst[i].append(blst[1])


def phone_a_friend(alst, calst, i, lvl):
    """The success rate of the friend's answer depends on difficulty level of the question"""
    frnd_answer = []
    ranswr = calst[i]
    ranswr_idx = alst[i].index(ranswr)
    if len(alst[i]) == 2:
        for _ in range(5 - lvl):
            frnd_answer.append(ranswr_idx)
        r_choice = random.randint(0, 1)
        frnd_answer.append(r_choice)
        frnd_choice = random.choice(frnd_answer)
        if frnd_choice == ranswr_idx:
            print(f"\nYour friend says it's: {alst[i][frnd_choice]}")
        else:
            print("\nYour friend says: I don't know")

    else:
        for _ in range(4 - lvl):
            frnd_answer.append(ranswr_idx)
        r_choice = random.randint(0, 3)
        frnd_answer.append(r_choice)
        frnd_choice = random.choice(frnd_answer)
        if frnd_choice == ranswr_idx:
            print(f"\nYour friend says it's: {alst[i][frnd_choice]}")
        else:
            print("\nYour friend says: I don't know")


def ask_audience(alst, calst, i, lvl):
    """The success rate of the audience poll  depends on difficulty level of the question"""
    ranswr = calst[i]  # B
    ranswr_idx = alst[i].index(ranswr)

    if len(alst[i]) == 4:
        if lvl == 1:
            ranswr_prcnt = round((random.uniform(0.45, 1)), 2)

        elif lvl == 2:
            ranswr_prcnt = round((random.uniform(0.4, 0.7)), 2)

        else:
            ranswr_prcnt = round((random.uniform(0.3, 0.6)), 2)

        wanswr1 = round(random.uniform(0, (1 - ranswr_prcnt)), 2)
        wanswr2 = round(random.uniform(0, (1 - ranswr_prcnt - wanswr1)), 2)
        if wanswr2 < 0:
            wanswr2 = 0
        wanswr3 = round((1 - ranswr_prcnt - wanswr1 - wanswr2), 2)
        if wanswr3 < 0:
            wanswr3 = 0

        wanswr_lst = [wanswr1, wanswr2, wanswr3]

        print("\nThe Audience poll results:")

        if ranswr_idx == 0:
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][2]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        elif ranswr_idx == 1:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][2]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        elif ranswr_idx == 2:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')
            print(f'\t{alst[i][3]} - {wanswr_lst[0]:.0%}')

        else:
            wachoice = random.randint(0, 2)
            print(f'\t{alst[i][0]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            wachoice = random.randint(0, 1)
            print(f'\t{alst[i][1]} - {wanswr_lst[wachoice]:.0%}')
            wanswr_lst.pop(wachoice)
            print(f'\t{alst[i][2]} - {wanswr_lst[0]:.0%}')
            print(f'\t{alst[i][ranswr_idx]} - {ranswr_prcnt:.0%}')

    else:
        if lvl == 1:
            ranswr_prcnt = round((random.uniform(0.45, 1)), 2)

        elif lvl == 2:
            ranswr_prcnt = round((random.uniform(0.4, 0.7)), 2)

        else:
            ranswr_prcnt = round((random.uniform(0.3, 0.6)), 2)

        wanswr = round(1 - ranswr_prcnt, 2)

        print("\nThe Audience poll results:")

        if ranswr_idx == 0:
            print(f'\t{alst[i][0]} - {ranswr_prcnt:.0%}')
            print(f'\t{alst[i][1]} - {wanswr:.0%}')

        elif ranswr_idx == 1:
            print(f'\t{alst[i][0]} - {wanswr:.0%}')
            print(f'\t{alst[i][1]} - {ranswr_prcnt:.0%}')


def lifeline_choice(lflst):
    decision = input("\nWould you like to use a Lifeline? (Y/N): ").upper().strip()
    if decision[0] == 'Y':
        print("\nYour available Lifelines:")
        for i in lflst:
            print(i, end=", ")
        lfchoice = input(f"\n\nWhich one do you choose? (Type: 55/pf/aa): ").upper().strip()
        if lfchoice[0] == '5':
            print(f'Your choice is: "50:50"')
            return '50:50'
        elif lfchoice[0] == 'P':
            print(f'Your choice is: "Phone a friend"')
            return 'Phone a friend'
        elif lfchoice[0] == 'A':
            print(f'Your choice is: "Ask Audience:')
            return 'Ask Audience'

    else:
        return False
