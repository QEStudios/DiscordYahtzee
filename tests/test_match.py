from uuid import UUID
import yahtzee


def test_match_creation():
    players = [
        yahtzee.Player(name, i) for i, name in enumerate(["alice", "bob", "charlie"])
    ]
    match = yahtzee.Match(players, 0)

    assert match.players == players
    assert isinstance(match.uuid, UUID)
