import random
from magician.repository.player_class import Player_repository
from magician.repository.gameboard_class import gameboard_repository

def test_hand_stone():
    hand_stone = [1, 2, 3, 4, 5]
    player = "Yock"
    player_hand_stone = Player_repository(player)
    player_hand_stone.player_hand_stone = hand_stone

    assert player_hand_stone.player_hand_stone == hand_stone
    

#def test_all_players_hand_stone():
#    all_stone = []
#    assigned_stones = []
#
#    for i in range(1,9):
#        stone = [i] * i
#        all_stone = all_stone + stone
#    random.shuffle(all_stone)
#    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]
#
#    for player,hand_stone in zip(except_input_name,all_stone):
#        hand_stone = all_stone[:5]
#        all_stone = all_stone[5:]
#        assigned_stones.append(hand_stone)
#        player_hand_stone = Player_repository(player)
#        player_hand_stone.player_hand_stone = hand_stone
#        assert player_hand_stone.player_hand_stone == hand_stone
#
#    assert player_hand_stone.get_all_players_hand_stone == assigned_stones
#
#    secret_stone = all_stone[:4]
#    last_stone = all_stone[4:]
#
#    
#    store_warehouse_secret_stone = gameboard_repository(except_input_name)
#    store_warehouse_secret_stone.set_warehouse_secret_stone(secret_stone)
#    assert store_warehouse_secret_stone.get_warehouse_secret_stone(except_input_name) == secret_stone
#
#    store_warehouse_stone = gameboard_repository(except_input_name)
#    store_warehouse_stone.set_warehouse_stone(last_stone)
#    assert store_warehouse_stone.get_warehouse_stone(except_input_name) == last_stone

    
