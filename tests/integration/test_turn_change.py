from magician.service.turn_change import round_change
from magician.repository.player_class import Player_repository

def test_turn_change():
    except_group_name = ["A", "B", "C", "D", "E"]
    except_initial_player = "A"

    for player_name in except_group_name:
        player = Player_repository(player_name = player_name)
        player.player_name = player_name
        player.group_names = except_group_name
        assert player.player_name == player_name
        assert player.group_names == except_group_name

    # player_seat = Player_repository(except_initial_player)
    # assert player_seat.set_turn_change() == 1

    # round_change(except_initial_player)
