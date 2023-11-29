from magician.repository.player_class import Player_repository
from magician.repository.gameboard_class import gameboard_repository

def test_stone_storge_ladder():
    except_group_name = ["A", "B", "C", "D", "E"]
    except_input_hand_stone = [
        [3, 3, 5, 7, 8],
        [5, 5, 7, 8, 8],
        [4, 5, 5, 6, 8],
        [4, 6, 6, 7, 8],
        [2, 6, 7, 7, 8],
    ]
    except_ladder = []
    player_spell_magic = 5

    for player_name in except_group_name:
        player = Player_repository(player_name = player_name)
        player.player_name = player_name
        player.group_names = except_group_name
        assert player.player_name == player_name
        assert player.group_names == except_group_name

    for player_name, hand_stone in zip(except_group_name, except_input_hand_stone):
        player = Player_repository(player_name)
        player.player_hand_stone = hand_stone
        assert player.player_hand_stone == hand_stone

    game = gameboard_repository()
    game.group_names = except_group_name
    assert game.group_names == except_group_name
    game.ladder = except_ladder
    assert game.ladder == except_ladder