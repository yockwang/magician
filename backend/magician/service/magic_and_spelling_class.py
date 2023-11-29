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

    def check_hand_stone_exist(except_player_name,except_hand_stone,except_group_name):
        player = Player_repository(player_name=except_player_name,except_group_name=except_group_name)
        playerA_hand_stone = player.player_hand_stone
        #assert playerA_hand_stone == [3,3,5,7,8]

        if except_hand_stone in playerA_hand_stone:
            return "hand_stone_exist"
        

    def magic_5_effect(player,group_name,seat):
        spelling_player = Player_repository(player_name=player,except_group_name=group_name)
        #assert spelling_player.player_seat == 0

        affected_player = Player_repository(except_group_name=group_name)
        
        affected_seat_1 = spelling_player.player_seat + 1
        #assert affected_seat_1 == 1
        if affected_seat_1 ==5:
            affected_seat_1 = affected_seat_1-5

        affected_seat_2 = spelling_player.player_seat - 1
        #assert affected_seat_2 == -1
        if affected_seat_2 == -1:
            affected_seat_2 = affected_seat_2 + 5

        affected_player.player_minus_1HP = affected_seat_1        
        affected_player.player_minus_1HP = affected_seat_2




