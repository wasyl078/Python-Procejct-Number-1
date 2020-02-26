# imports
from blocks.abstract_block import AbtractBlock, abstractmethod
from general.consts_values import Blocks, Color
from blocks.player_block import Player
from typing import List
from graphs.graph import MyOwnGraph


# enemy block / object is always looking for player by using a* pathfinding algorithm
class Enemy(AbtractBlock):

    # constructor - setting enemy object; receives graph
    def __init__(self, pos_x: int, pos_y: int, graph: MyOwnGraph) -> None:
        super().__init__(pos_x, pos_y, Color.RED, Blocks.ENEMY)
        self.graph = graph
        self.player: Player = None
        self.timer = 60

    # updates position - it depends on player's position
    @abstractmethod
    def update(self, matrix, moveable_objects: List[AbtractBlock]):
        for objectt in moveable_objects:
            if objectt.block_type == Blocks.PLAYER:
                self.player = objectt
                break

        if self.timer < 0:
            T = self.graph.find_a_star_path(self.pos_x, self.pos_y, self.player.pos_x, self.player.pos_y)
            if self.check_place(T[-1].x, T[-1].y, matrix, moveable_objects):
                self.pos_x = T[-1].x
                self.pos_y = T[-1].y

            self.timer = 10
        else:
            self.timer -= 1

    # cannot move into enemy:
    def __bool__(self):
        return False