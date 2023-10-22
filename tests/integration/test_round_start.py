import random
from magician.repository.playerclass import Player_repository
def test_hand_stone():
    #stone = [
    #    "magic1",
    #    "magic2","magic2",
    #    "magic3","magic3","magic3",
    #    "magic4","magic4","magic4","magic4",
    #    "magic5","magic5","magic5","magic5","magic5",
    #    "magic6","magic6","magic6","magic6","magic6","magic6",
    #    "magic7","magic7","magic7","magic7","magic7","magic7","magic7",
    #    "magic8","magic8","magic8","magic8","magic8","magic8","magic8","magic8",
    #]

    #random.shuffle(stone)

    #players = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]
    #assigned_stone = {}
    #for player in players:
    #    assigned_stone[player] = stone[:5]
    #    stone = stone[5:]

#for i in range(1,9):
#    [i] * i

    hand_stone = [1,2,3,4,5]
    player ="Yock"
    player_hand_stone = Player_repository(player)
    player_hand_stone.except_input_HP = 5
    player_hand_stone.update_player_hand_stone(hand_stone) #set_hand_stone
    
    assert player_hand_stone.get_hand_stone() == hand_stone


