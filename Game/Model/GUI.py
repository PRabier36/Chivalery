import time

from Game.Model.Fight import Fight
from Game.Model.Knight import Knight
from Game.Model.Map import Map
from Game.Model.enemy import Enemy
from Game.Model.Unit import Unit
from Game.Model.Player import Player
import os
import requests

api_url = "http://localhost:3001"


def start_game():
    os.system('cls')
    play = True
    while play:
        try:

            choice = int(input("1. New game\n"
                               "2. Continue\n"
                               "0. Quit\n"))
            if choice == 1:
                new_game()
            elif choice == 2:
                selectPlayer()
            elif choice == 0:
                print("Bye !")
                return
            else:
                print("Entry error !")
                input("Enter for continue...")
        except ValueError:
            print("Entry error !")
            input("Enter for continue...")
    return


def listPlayers():
    try:
        players = requests.request("GET", api_url+"/players/")
        playerList = []
        i = 1
        for player in players.json():
            p = Player(player["_id"], player["name"], player["rank"], player["level"], player["money"], player["xp"], player["teachingBonus"])

            p.add_from_list(player["Knight_list"])
            playerList.append(p)
            print(i)
            p.print()
            i += 1
        return playerList
    except ValueError:
        print(ValueError)


def selectPlayer():
    list = listPlayers()
    print("0. Return\n")
    play = True
    while play:
        try:
            choice = int(input("Select your save\n"))
            if choice == 0:
                return
            else:
                main_menu(list[(choice-1)])
                return
        except ValueError:
            print("Entry error !")
            input("Enter for continue...")


def new_game():
    # name = "King Arthur"
    name = input("Your name ?: ")

    p = Player(None, name)
    main_menu(p)


def main_menu(Player):
    play = True
    while play:
        os.system('cls')
        print("Main Menu\n")
        try:
            choice = int(input("What do you want to do?\n"
                               "1. Recruit Knight (-25 GP)\n"
                               "2. Player' info\n"
                               "3. Knight's List\n"
                               "4. Fight\n"
                               "5. Save\n"
                               # "5. School\n"
                               # "6. Shop\n"
                               "0. Save and back menu\n"))
            if choice == 1:
                if Player.get_money() > 25:
                    k = Player.create_new_knight()
                    print("Your new knight : \n")
                    k.print()
                    Player.add_money(-25)
                    input("Enter for continue...")
                else:
                    print("Need more gold\n"
                          "Your gold : " + str(Player.get_money()))
                    input("Enter for continue...")
            elif choice == 2:
                print("Profil:\n")
                Player.print()
                input("Enter for continue...")
            elif choice == 3:
                Player.print_knights()
                input("Enter for continue...")
            elif choice == 4:
                if len(Player.get_knightList()) >= 1:
                    list_fight(Player)
                    # input("Enter for continue...")
                else:
                    print("Need to recruit")
                    input("Enter for continue...")
            elif choice == 5:
                Player.save()
                input("Enter for continue...")
            elif choice == 0:
                Player.save()
                print("Save... !")
                input("Enter for continue...")
                return
            else:
                print("Entry error ! (127)")
                input("Enter for continue...")
        except ValueError:
            print("Entry error (except) !")
            input("Enter for continue...")


def list_fight(Player):
    fight_loop = True
    while fight_loop:
        os.system('cls')
        goblin_id = 123
        goblin_str = 7
        goblin_agi = 14
        goblin_const = 10
        goblin_mana = 8
        goblin_mastery = 7
        goblin_luck = 8
        goblin_xpDrop = 50
        goblin_goldDrop = 5
        goblin_pos = "front"
        g1 = Enemy(goblin_id, "Goblin", goblin_str, goblin_agi, goblin_const, goblin_mana,
                   goblin_mastery, goblin_luck, goblin_xpDrop, goblin_goldDrop, goblin_pos)
        f1_e = [g1]
        fight1 = Fight("First Fight", 10, 50, 15, f1_e, Player)
        fight_list = [fight1]
        i = 1
        for fight in fight_list:
            print(str(i) + ". " + fight.print())
            i += 1
        print("0. Return")
        try:
            choice = int(input("Choose your quest : "))
            if choice == 0:
                return
            elif choice <= len(fight_list):
                i = 0
                for fight in fight_list:
                    if choice == i + 1:
                        fight.Start()
                    i += 1
            else:
                print("Entry error !")
                input("Enter for continue...")
        except ValueError:
            print("Entry error !")
            input("Enter for continue...")

    return
