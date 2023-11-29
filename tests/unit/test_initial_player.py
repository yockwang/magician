from magician.service.initial_player import initial_player
from magician.repository.player_class import Player_repository

def test_initial_player():
    except_group_name = ["A", "B", "C", "D", "E"]
    except_input_seat = [0,1,2,3,4]
    
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


    assert initial_player(except_group_name) == "A"