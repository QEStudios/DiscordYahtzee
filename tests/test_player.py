from uuid import UUID
import yahtzee


def test_player_creation():
    alice = yahtzee.Player("alice", 0)
    bob = yahtzee.Player("bob", 1)

    assert alice.name == "alice"
    assert alice.player_num == 0
    assert isinstance(alice.uuid, UUID)

    assert bob.name == "bob"
    assert bob.player_num == 1
    assert isinstance(bob.uuid, UUID)
