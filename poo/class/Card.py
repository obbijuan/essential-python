from typing import Tuple
from enum import Enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


class Card:

    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def __str__(self):
        return str(self.__class__.__name__) + ": " + str(self.__dict__)
        # return f'{self.__class__.__name__} {repr(self._points())} '

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

class AceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 1, 11

class FaceCard(Card):

    def _points(self) -> Tuple[int, int]:
        return 10, 10


def card(rank: int, suit: Suit) -> Card:
    if rank == 1:
        return AceCard("A", suit)
    elif 2 <= rank < 11:
        return Card(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: "J", 12: "Q", 13: "K"}[rank]
        return FaceCard(name, suit)
    raise Exception("Design Failure")


cards = [AceCard('A', Suit.Spade), Card('2', Suit.Diamond), FaceCard('Q', Suit.Club),]
for x in cards:             
    print(x)

cards2 = [ card(rank, suit) for rank in range(1,14) for suit in Suit.Heart ]
for x in cards2:             
    print(x)

