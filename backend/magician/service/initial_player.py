from magician.repository.player_class import Player_repository

def initial_player(except_group_name):
    initial_seat = 0
    player = Player_repository(except_group_name=except_group_name,initial_seat=initial_seat)
    return player.initial_player
    