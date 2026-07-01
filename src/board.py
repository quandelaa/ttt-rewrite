class Board:
    def __init__(self) -> None:
        self.state = [["?", "?", "?"],
                      ["?", "?", "?"],
                      ["?", "?", "?"]]
    
    def update_state(self, new_state):
        self.state = new_state.copy()
