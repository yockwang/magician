from magician.repository.playerclass import Player_repository
from magician.service.stone_number_check import stone_number_check

def test_spell_fail():
    except_input_hold_stone = ["magic1", "magic2", "magic3", "magic4", "magic5"]
    player_seat = (0)
    
    Player_repository.update_player_hold_stone(except_input_hold_stone,player_seat)

    player_spell_number = ["magic7"]
    #stone_number_check(player_spell_number,player_seat)

    assert "spell fail minus 1 HP" == stone_number_check(player_spell_number,player_seat)