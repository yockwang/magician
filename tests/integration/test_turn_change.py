from magician.service.turn_change import round_change
from magician.repository.playerclass import Player_repository


def test_turn_change():
    except_team_player = ["A", "B", "C", "D", "E"]
    except_initial_player = "A"

    for player in except_team_player:
        player_name = Player_repository(player, except_team_player)
        player_name.set_player_name()

    assert player_name.get_group_names() == except_team_player

    # player_seat = Player_repository(except_initial_player)
    # assert player_seat.set_turn_change() == 1

    # round_change(except_initial_player)
