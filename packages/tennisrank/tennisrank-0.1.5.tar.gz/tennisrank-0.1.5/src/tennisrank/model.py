from dataclasses import dataclass


@dataclass(frozen=True)
class Player:
    id: int = 0
    name: str = ''


@dataclass(frozen=True)
class Match:
    winner: Player = None
    loser: Player = None
    point_diff: int = None
    surface: str = None


@dataclass(frozen=True)
class PlayerRank:
    player: Player = None
    rank: float = None
    surface: str = None
