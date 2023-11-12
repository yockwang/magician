from magician.repository.player_class import Player_repository


class magic_and_spelling:
    def check_magic_exist(stoneID):
        magic_stones = {
            0: True,
            1: True,
            2: True,
            3: True,
            4: True,
            5: True,
            6: True,
            7: True,
            8: True,
        }

        if stoneID in magic_stones:
            return "magic exist"
        else:
            return "magic doesn't exist"

    def magic_5_effect(player):
        player_seat = Player_repository()
        # assert player_seat.
