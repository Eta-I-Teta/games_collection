from engine.classes.GUI import *

class Player():
    def __init__(self, moving: bool):
        self.moving = moving

class Cell():
    def __init__(self, status: str = "nothing"):
        self.status = status

class Level():
    def __init__(self, inner: list, cell_size: int):
        self.inner = inner
        self.cell_size = cell_size
    def draw(self, surface: pygame.surface):
        x = (CONFIG_SCREEN["path_finder"]["width"] - self.cell_size * len(self.inner[0])) / 2
        y = (CONFIG_SCREEN["path_finder"]["height"] - self.cell_size * len(self.inner)) / 2

        for row in range(len(self.inner)):
            for column in range(len(self.inner[row])):
                if type(self.inner[row][column]) is Player:
                    cell_color = COLOR["orange"]
                elif (type(self.inner[row][column]) is Cell) and (self.inner[row][column].status == "nothing"):
                    cell_color = COLOR["gray"]
                elif (type(self.inner[row][column]) is Cell) and (self.inner[row][column].status == "traversed"):
                    cell_color = COLOR["yellow"]
                elif (type(self.inner[row][column]) is Cell) and (self.inner[row][column].status == "finish"):
                    cell_color = COLOR["white"]
                else: continue
                pygame.draw.rect(
                        surface,
                        cell_color,
                        [
                            x + column * self.cell_size,
                            y + row * self.cell_size,
                            self.cell_size,
                            self.cell_size
                        ]
                    )
    def get_player_pos(self) -> tuple[int, int]:
        for y in range(len(self.inner)):
            for x in range(len(self.inner[y])):
                if type(self.inner[y][x]) is Player:
                    return [x, y]
    
    def get_player(self) -> Player:
        return self.inner[self.get_player_pos()[1]][self.get_player_pos()[0]]
    
    def get_directions(self) -> list:
        crossroad = []
        player = self.get_player()
        [x, y] = self.get_player_pos()
        if not(x == len(self.inner[y]) - 1) and (type(self.inner[y][x + 1]) is Cell) and (self.inner[y][x + 1].status != "traversed"):
            crossroad.append([1, 0])
        if not(x == 0) and (type(self.inner[y][x - 1]) is Cell) and (self.inner[y][x - 1].status != "traversed"):
            crossroad.append([-1, 0])
        if not(y == len(self.inner) - 1) and (type(self.inner[y + 1][x]) is Cell) and (self.inner[y + 1][x].status != "traversed"):
            crossroad.append([0, 1])
        if not(y == 0) and (type(self.inner[y - 1][x]) is Cell) and (self.inner[y - 1][x].status != "traversed"):
            crossroad.append([0, -1])

        return crossroad
    
    def move(self, dash = None):
        [old_x, old_y] = self.get_player_pos()
        old_player = self.get_player()

        if dash == None:
            directions = self.get_directions()
        else:
            directions = [dash]
            old_player.moving = True
        if (len(directions) == 1) and (old_player.moving):
            self.inner[old_y + directions[0][1]][old_x + directions[0][0]] = Player(True)
            self.inner[old_y][old_x] = Cell(status = "traversed")
        else:
            old_player.moving = False