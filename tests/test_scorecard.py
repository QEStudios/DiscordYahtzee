import yahtzee


def test_scorecard_creation():
    player = yahtzee.Player("alice", 0)
    scorecard = yahtzee.Scorecard(player=player)

    assert isinstance(scorecard, yahtzee.Scorecard)
