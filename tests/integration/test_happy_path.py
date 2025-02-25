from magician.repository.player_class import Player_repository
from magician.repository.gameboard_class import gameboard_repository
from magician.service.initial_player import initial_player
from magician.service.magic_and_spelling_class import magic_and_spelling


def test_happy_path():
    except_group_name = ["A", "B", "C", "D", "E"]
    except_input_seat = [0, 1, 2, 3, 4]
    except_input_HP = [6] * 5
    except_input_score = [0] * 5
    except_input_hand_stone = [
        [3, 3, 5, 7, 8],
        [5, 5, 7, 8, 8],
        [4, 5, 5, 6, 8],
        [4, 6, 6, 7, 8],
        [2, 6, 7, 7, 8],
    ]
    except_secret_stone = [2, 3, 7, 8]
    except_unknown_stone = [4, 8, 6, 1, 6, 7, 4]
    except_ladder = []
    except_round = 1
    except_turn = 1

    for player_name in except_group_name:
        player = Player_repository(player_name = player_name)
        player.player_name = player_name
        player.group_names = except_group_name
        assert player.player_name == player_name
        assert player.group_names == except_group_name

    for player_name, seat in zip(except_group_name, except_input_seat):
        player = Player_repository(player_name)
        player.player_seat = seat
        assert player.player_seat == seat

    for player_name, hp in zip(except_group_name, except_input_HP):
        player = Player_repository(player_name)
        player.player_hp = hp
        assert player.player_hp == hp

    for player_name, score in zip(except_group_name, except_input_score):
        player = Player_repository(player_name)
        player.player_score = score
        assert player.player_score == score

    for player_name, hand_stone in zip(except_group_name, except_input_hand_stone):
        player = Player_repository(player_name)
        player.player_hand_stone = hand_stone
        assert player.player_hand_stone == hand_stone

    player = Player_repository(player,except_group_name)
    assert player.get_all_players_seat == except_input_seat
    assert player.get_all_players_hp == except_input_HP
    assert player.get_all_players_score == except_input_score
    assert (
        player.get_all_players_hand_stone == except_input_hand_stone
    )

    game = gameboard_repository()
    game.group_names = except_group_name
    assert game.group_names == except_group_name

    game.secret_stone = except_secret_stone
    assert game.secret_stone == except_secret_stone

    game.unknown_stone = except_unknown_stone
    assert game.unknown_stone == except_unknown_stone

    game.ladder = except_ladder
    assert game.ladder == except_ladder

    game.round = except_round
    assert game.round == except_round

    game.turn = except_turn
    assert game.turn == except_turn

    #玩家A施放5號魔法石並成功,玩家A左右兩邊玩家：B、E各扣1HP
    player = initial_player(except_group_name)
    assert player == "A"

    player_spell_magic = 5

    assert magic_and_spelling.check_magic_exist(player_spell_magic) == "magic exist"
    assert magic_and_spelling.check_hand_stone_exist(except_player_name=player,except_hand_stone=player_spell_magic,except_group_name=except_group_name)

    magic_and_spelling.magic_5_effect(player=player,group_name=except_group_name,seat=except_input_seat)
    check_all_player_hp = Player_repository(except_group_name=except_group_name)
    assert check_all_player_hp.get_all_players_hp == [6,5,6,6,5]