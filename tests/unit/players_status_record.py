from magician.repository.playerclass import Player_repository
from magician.repository.warehouse import warehouse_repository

def test_players_status_record():
    except_input = ["yock", "Teds", "Tux", "Leave3310", "Momo"]
    except_input_seat = ["A","B","C","D","E"]
    except_input_HP = ["6","6","6","6","6"]
    
    player_status = Player_repository(except_input, except_input_seat, except_input_HP)
    
    assert player_status.get_player_names() == except_input


def test_stone_storage_warehouse():
    Number_of_magic_stones = {
        "magic1":1,
        "magic2":2,
        "magic3":3,
        "magic4":4,
        "magic5":5,
        "magic6":6,
        "magic7":7,
        "magic8":8,
    }
    warehouse_repository(Number_of_magic_stones)