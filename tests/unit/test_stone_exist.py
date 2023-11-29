from magician.service.magic_and_spelling_class import magic_and_spelling
from magician.repository.player_class import Player_repository

def test_stone_exist():

    spell_stone = 5

    assert magic_and_spelling.check_magic_exist(spell_stone) == "magic exist"

def test_hand_stone_exist():
    except_player_name = "A"
    except_hand_stone = 5
    except_group_name = ["A", "B", "C", "D", "E"]
    except_input_hand_stone = [
        [3, 3, 5, 7, 8],
        [5, 5, 7, 8, 8],
        [4, 5, 5, 6, 8],
        [4, 6, 6, 7, 8],
        [2, 6, 7, 7, 8],
    ]
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

        assert magic_and_spelling.check_hand_stone_exist(except_player_name,except_hand_stone,except_group_name) == "hand_stone_exist"
        

