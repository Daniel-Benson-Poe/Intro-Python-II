import time
from player_input import InputParser

class GameLoop:
    def __init__(self, player):
        self.player = player
            
        self.player.current_room.print_room_details()
        time.sleep(1)

        if player.current_room.items:
            print()
            player.current_room.print_items_in_room()
            time.sleep(1)

        if player.current_room.enemy:
            player.current_room.enemy.print_description()

        input_parser = InputParser(self.player)
        input_parser.use_player_input()
            
