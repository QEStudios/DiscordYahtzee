import main


def test_scorecard_creation():
    scorecard = main.Scorecard(1, "test")

    assert isinstance(scorecard, main.Scorecard)


def test_scorecard_score_setting():
    scorecard = main.Scorecard(1, "test")

    scorecard.ones = 1
    scorecard.twos = 2
    scorecard.threes = 3
    scorecard.fours = 4
    scorecard.fives = 5
    scorecard.sixes = 6

    scorecard.three_of_a_kind = 7
    scorecard.four_of_a_kind = 8
    scorecard.full_house = 9
    scorecard.small_straight = 10
    scorecard.large_straight = 11
    scorecard.yahtzee = 100
    scorecard.chance = 12
    scorecard.mark_yahtzee_bonus()
    scorecard.mark_yahtzee_bonus()
    scorecard.mark_yahtzee_bonus()


def test_scorecard_printing():
    scorecard = main.Scorecard(1, "test")

    scorecard.ones = 3
    scorecard.yahtzee = 100
    scorecard.mark_yahtzee_bonus()

    print(scorecard)
