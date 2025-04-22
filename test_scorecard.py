import main


def test_game_scorecard_creation():
    game_scorecard = main.GameScorecard(game_num=0, player_num=0, player_name="alice")

    assert isinstance(game_scorecard, main.GameScorecard)


def test_game_scorecard_score_setting():
    game_scorecard = main.GameScorecard(game_num=0, player_num=0, player_name="bob")

    game_scorecard.ones = 1
    game_scorecard.twos = 2
    game_scorecard.threes = 3
    game_scorecard.fours = 4
    game_scorecard.fives = 5
    game_scorecard.sixes = 6

    game_scorecard.three_of_a_kind = 7
    game_scorecard.four_of_a_kind = 8
    game_scorecard.full_house = 9
    game_scorecard.small_straight = 10
    game_scorecard.large_straight = 11
    game_scorecard.yahtzee = 100
    game_scorecard.chance = 12
    game_scorecard.mark_yahtzee_bonus()
    game_scorecard.mark_yahtzee_bonus()
    game_scorecard.mark_yahtzee_bonus()


def test_game_scorecard_printing():
    game_scorecard = main.GameScorecard(game_num=0, player_num=0, player_name="charlie")

    game_scorecard.ones = 3
    game_scorecard.yahtzee = 100
    game_scorecard.mark_yahtzee_bonus()

    print(game_scorecard)
