import time
from magician.service.round_start import round_start
from magician.repository.player_class import Player_repository


def game_create(players):
    players_number = len(players["playerIDs"])
    if players_number <= 3:
        return "players is not enough"
    elif players_number >= 6:
        return "players is over 5"
    else:
        except_input_seat = list(range(players_number))
        except_input_HP = [6] * players_number
        except_input_score = [0] * players_number

        for player_name in players["playerIDs"]:
            player = Player_repository(player_name = player_name)
            player.player_name = player_name
            player.group_names = players["playerIDs"]
            assert player.player_name == player_name
            assert player.group_names == players["playerIDs"]

        for player_name, seat in zip(players["playerIDs"], except_input_seat):
            player = Player_repository(player_name)
            player.player_seat = seat
            assert player.player_seat == seat

        for player_name, hp in zip(players["playerIDs"], except_input_HP):
            player = Player_repository(player_name)
            player.player_hp = hp
            assert player.player_hp == hp

        for player_name, score in zip(players["playerIDs"], except_input_score):
            player = Player_repository(player_name)
            player.player_score = score
            assert player.player_score == score

        player = Player_repository(player,players["playerIDs"])
        assert player.get_all_players_seat == except_input_seat
        assert player.get_all_players_hp == except_input_HP
        assert player.get_all_players_score == except_input_score

        create_room_id(players["playerIDs"][0])
        # round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
