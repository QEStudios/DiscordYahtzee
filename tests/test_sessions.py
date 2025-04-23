import yahtzee


def test_session_creation():
    session = yahtzee.Session()

    alice = yahtzee.Player("alice", 0)
    bob = yahtzee.Player("bob", 1)
    charlie = yahtzee.Player("charlie", 2)

    match = session.start_match(players=[alice, bob, charlie])

    print(match)
