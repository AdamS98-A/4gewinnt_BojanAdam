class Player:
    def __init__(self, name: str, current_turn: int, winner: bool):
        self.name = name
        self.current_turn = current_turn
        self.winner = winner

    def __repr__(self):
        return f'{self.name} {self.current_turn} {self.winner}'
    
    def increase_Turn_Counter(self):
        self.current_turn += 1


if __name__ == '__main__':
    s = Player("Rudi", 0, True)
    s.increase_Turn_Counter()
    print(s)
