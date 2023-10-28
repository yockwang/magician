import random
from magician.repository.playerclass import Player_repository

def round_start():
    # Given 目前有5位玩家A、B、C、D、E
    # When 系統確認玩家為A、B、C、D 、E 5名玩家魔法石都有5顆
    # Then 系統回合開始

    # 局初始設置：
    # 1.已洗好魔法石
    # 2.每位玩家已拿5顆魔法石
    # 3.已設定玩家血量
    # 4.已決定第一位玩家
    # 5.從剩餘魔法石取出4顆魔法石作為秘密魔法石
    all_stone = []
    assigned_stones = []

    for i in range(1,9):
        stone = [i] * i
        all_stone = all_stone + stone
    random.shuffle(all_stone)
    except_input_name = ["Teds", "Tux", "Yock", "Momo", "Leave3310"]

    for player,hand_stone in zip(except_input_name,all_stone):
        hand_stone = all_stone[:5]
        all_stone = all_stone[5:]
        assigned_stones.append(hand_stone)
        player_hand_stone = Player_repository(player)
        player_hand_stone.set_player_hand_stone(hand_stone)

    assert player_hand_stone.get_hand_stone(except_input_name) == assigned_stones
