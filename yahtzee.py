from __future__ import annotations
import random
import string
from uuid import uuid4
from typing import cast


class Player:
    """A single player"""

    def __init__(self, name: str, player_num: int):
        self.name = name
        self.player_num = player_num
        self.uuid = uuid4()


class Game:
    """A single game for a single player"""

    UPPER_SECTION = ["ones", "twos", "threes", "fours", "fives", "sixes"]
    LOWER_SECTION = [
        "three_of_a_kind",
        "four_of_a_kind",
        "full_house",
        "small_straight",
        "large_straight",
        "yahtzee",
        "chance",
    ]
    ALL_CATEGORIES = UPPER_SECTION + LOWER_SECTION

    def __init__(self, game_num: int, player: Player):
        self.scores: dict[str, int | None] = {
            category: None for category in self.ALL_CATEGORIES
        }  # None means the category hasn't been scored yet
        self.yahtzee_bonus: tuple[bool, bool, bool] = (False, False, False)

        self.uuid = uuid4()
        self.revision = 0

        self.game_num = game_num
        self.player = player

        self.match: Match | None = None

    def assign_match(self, match: Match) -> None:
        """Assign a parent match to this game"""
        self.match = match

    def set_score(self, category: str, score: int) -> None:
        """Set score for a category. Raises error if already filled or invalid category."""
        if category not in self.ALL_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")
        if self.scores[category] is not None:
            raise ValueError(f"Category '{category}' already scored.")
        self.scores[category] = score
        self.revision += 1

    def mark_yahtzee_bonus(self) -> None:
        """Marks the next available Yahtzee bonus slot as used."""
        for i, marked in enumerate(self.yahtzee_bonus):
            if not marked:
                bonus_list = list(self.yahtzee_bonus)
                bonus_list[i] = True
                self.yahtzee_bonus = cast(tuple[bool, bool, bool], tuple(bonus_list))
                self.revision += 1
                return
        raise ValueError("All Yahtzee bonus slots are already used.")

    @property
    def yahtzee_bonus_total(self) -> int:
        """The calculated Yahtzee Bonus"""
        return sum(self.yahtzee_bonus) * 100

    @property
    def upper_total(self) -> int:
        """The calculated Total of Upper Section"""
        return sum(
            score
            for cat, score in self.scores.items()
            if cat in self.UPPER_SECTION and score is not None
        )

    @property
    def upper_bonus(self) -> int:
        """The calculated Upper Section Bonus"""
        return 35 if self.upper_total >= 63 else 0

    @property
    def lower_total(self) -> int:
        """The calculated Total of Lower Section"""
        return sum(
            score
            for cat, score in self.scores.items()
            if cat in self.LOWER_SECTION and score is not None
        )

    @property
    def total_score(self) -> int:
        """The calculated Grand Total score"""
        return (
            self.upper_total
            + self.upper_bonus
            + self.lower_total
            + self.yahtzee_bonus_total
        )

    @property
    def is_complete(self) -> bool:
        """Returns True if the player has filled in all 13 scoring categories"""
        return all(score is not None for score in self.scores.values())

    def __str__(self):
        lines = []
        for cat in self.UPPER_SECTION:
            lines.append(f"{cat.capitalize():<15}: {self.scores[cat]}")
        lines.append(f"{'Bonus':<15}: {self.upper_bonus}")
        for cat in self.LOWER_SECTION:
            lines.append(
                f"{cat.replace('_', ' ').capitalize():<15}: {self.scores[cat]}"
            )
        lines.append(
            f"{'Yahtzee Bonus':<15}: {self.yahtzee_bonus} (+{self.yahtzee_bonus_total})"
        )
        lines.append(f"{'Total Score':<15}: {self.total_score}")
        return "\n".join(lines)

    def __getattr__(self, name):
        if name in self.ALL_CATEGORIES:
            return self.scores[name]
        super().__getattr__(name)

    def __setattr__(self, name, value):
        if name in self.ALL_CATEGORIES:
            self.set_score(name, value)
        super().__setattr__(name, value)


class Scorecard:
    """A scorecard for 6 games, equivalent to a single score card sheet in Yahtzee"""

    def __init__(self, player: Player, games: list[Game] | None = None):
        self.player = player
        if games == None:
            self.games = [Game(game_num, player) for game_num in range(6)]
        else:
            self.games = games

        self.uuid = uuid4()
        self.id = self._generate_id()
        self.revision = 0

    @property
    def _id_exists(self) -> bool:
        return False  # TODO

    def _generate_id(self, length: int = 6) -> str:
        chars = string.ascii_lowercase + string.digits

        generated_id = "".join(random.choice(chars) for _ in range(length))

        return generated_id


class Match:
    """A single match between 2-10 players"""

    def __init__(
        self, players: list[Player], game_num: int, games: list[Game] | None = None
    ):
        self.players = players
        self.uuid = uuid4()

        if games == None:
            self.games = [Game(game_num, player) for player in players]
        else:
            allocatable_players = players.copy()
            for game in games:
                assert (
                    game.player in allocatable_players
                ), "Provided games don't have the same players as the match!"
                allocatable_players.remove(game.player)
                game.assign_match(self)
            assert (
                len(allocatable_players) == 0
            ), "Provided games don't have the same players as the match!"
            self.games = games


class Session:
    """A session of multiple matches"""

    def __init__(self, matches: list[Match] = []):
        self.matches = matches
        self.involved_players: list[Player] = []

        for match in matches:
            for player in match.players:
                if player not in self.involved_players:
                    self.involved_players.append(player)

        self.match_in_progress = False
        self.uuid = uuid4()

    @property
    def current_match_num(self) -> int:
        """Returns the current match number if a match is in progress"""
        if self.match_in_progress == False:
            raise RuntimeError("No active match")
        return max(0, len(self.matches) - 1)

    @property
    def current_match(self) -> Match:
        """Returns the current match if a match is in progress, else None"""
        if self.match_in_progress == False:
            raise RuntimeError("No active match")
        return self.matches[self.current_match_num]

    def start_match(self, players: list[Player]) -> Match:
        """Start a new match in this session"""

        if self.match_in_progress == True:
            raise RuntimeError(
                "Cannot start a new match until the current one is complete"
            )

        match = Match(players=players, game_num=len(self.matches))

        return match
