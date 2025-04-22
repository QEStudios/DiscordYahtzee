import yahtzee


def test_session_creation():
    session = yahtzee.Session()

    alice = yahtzee.Player("alice", 0)
    bob = yahtzee.Player("alice", 1)
    charlie = yahtzee.Player("alice", 2)

    match = session.start_match(players=[alice, bob, charlie])

    print(match)
