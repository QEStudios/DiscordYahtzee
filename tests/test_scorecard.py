import yahtzee


def test_scorecard_creation():
    scorecard = yahtzee.Scorecard(player_num=1, player_name="alice")

    assert isinstance(scorecard, main.Scorecard)
