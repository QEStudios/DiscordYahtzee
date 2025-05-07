import pytest
import yahtzee


def test_session_creation():
    session = yahtzee.Session()

    assert isinstance(session, yahtzee.Session)


def test_session_creation_with_existing_matches():
    players = [
        yahtzee.Player("alice", 0),
        yahtzee.Player("bob", 1),
        yahtzee.Player("charlie", 2),
    ]

    matches = [
        yahtzee.Match(players=players, game_num=0),
        yahtzee.Match(players=players, game_num=1),
        yahtzee.Match(players=players, game_num=2),
    ]

    session = yahtzee.Session(matches=matches)

    assert session.matches == matches


def test_session_start_match():
    session = yahtzee.Session()

    alice = yahtzee.Player("alice", 0)
    bob = yahtzee.Player("bob", 1)
    charlie = yahtzee.Player("charlie", 2)

    match = session.start_match(players=[alice, bob, charlie])

    assert isinstance(match, yahtzee.Match)


def test_session_match_count_exceed_max():
    session = yahtzee.Session()

    alice = yahtzee.Player("alice", 0)
    bob = yahtzee.Player("bob", 1)
    charlie = yahtzee.Player("charlie", 2)

    matches = []

    # start max number of matches
    for i in range(session.MAX_MATCHES):
        print(f"Match count: {i}")
        matches.append(session.start_match(players=[alice, bob, charlie]))

    print(len(matches))

    # ensure no more matches can be made
    with pytest.raises(RuntimeError):
        matches.append(session.start_match(players=[alice, bob, charlie]))
