import time
from magician.service.round_start import round_start
from magician.repository.playerclass import Player_repository


def game_create(players):
    if len(players["playerIDs"]) <= 3:
        return "players is not enough"
    elif len(players["playerIDs"]) >= 6:
        return "players is over 5"
    else:
        except_input_seat = list(range(5))
        except_input_HP = [6]*5
        except_input_score = [0]*5
        Player_repository(
            players["playerIDs"],
            except_input_seat,
            except_input_HP,
            except_input_score
        )
        #create_room_id(players["playerIDs"][0])
        round_start()
        return "start game"


def create_room_id(first_player):
    game_room_id = first_player + str(time.time_ns())
    return game_room_id
