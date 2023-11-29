from magician.repository.player_class import Player_repository
from magician.service.initial_player import initial_player
from magician.service.magic_and_spelling_class import magic_and_spelling

def test_magic_5_effect():
    except_group_name = ["A", "B", "C", "D", "E"]
    except_input_HP = [6] * 5
    except_input_seat = [0,1,2,3,4]

    for player_name in except_group_name:
        player = Player_repository(player_name = player_name)
        player.player_name = player_name
        player.group_names = except_group_name
        assert player.player_name == player_name
        assert player.group_names == except_group_name

    for player_name, seat in zip(except_group_name, except_input_seat):
        player = Player_repository(player_name=player_name)
        player.player_seat = seat
        assert player.player_seat == seat

    for player_name, hp in zip(except_group_name, except_input_HP):
        player = Player_repository(player_name=player_name)
        player.player_hp = hp
        assert player.player_hp == hp

    spelling_player = initial_player(except_group_name)
    assert spelling_player == "A"
    
    magic_and_spelling.magic_5_effect(player=spelling_player,group_name=except_group_name,seat=except_input_seat)

    check_all_player_hp = Player_repository(except_group_name=except_group_name)
    assert check_all_player_hp.get_all_players_hp == [6,5,6,6,5]