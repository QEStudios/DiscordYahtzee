class Scorecard:
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

    def __init__(self, player_num: int, player_name: str):
        self.scores: dict[str, int | None] = {
            category: None for category in self.ALL_CATEGORIES
        }  # None means the category hasn't been scored yet
        self.revision = 0

        self.player_num = player_num
        self.player_name = player_name

    def set_score(self, category: str, score: int):
        """Set score for a category. Raises error if already filled or invalid category."""
        if category not in self.ALL_CATEGORIES:
            raise ValueError(f"Invalid category: {category}")
        if self.scores[category] is not None:
            raise ValueError(f"Category '{category}' already scored.")
        self.scores[category] = score
        self.revision += 1

    @property
    def upper_total(self):
        return sum(
            score
            for cat, score in self.scores.items()
            if cat in self.UPPER_SECTION and score is not None
        )

    @property
    def upper_bonus(self):
        return 35 if self.upper_total >= 63 else 0

    @property
    def lower_total(self):
        return sum(
            score
            for cat, score in self.scores.items()
            if cat in self.LOWER_SECTION and score is not None
        )

    @property
    def total_score(self):
        return self.upper_total + self.upper_bonus + self.lower_total

    @property
    def is_complete(self):
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
        lines.append(f"{'Total Score':<15}: {self.total_score}")
        return "\n".join(lines)

    def __getattr__(self, name):
        if name in self.ALL_CATEGORIES:
            return self.scores[name]
        super().__getattr__(name)

    def __setattr__(self, name, value):
        if name in self.ALL_CATEGORIES:
            self.set_score(self, name, value)
        super().__setattr__(name, value)
