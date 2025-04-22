import yahtzee


def test_game_creation():
    player = yahtzee.Player("alice", 0)
    game = yahtzee.Game(game_num=0, player=player)

    assert isinstance(game, yahtzee.Game)


def test_game_score_setting():
    player = yahtzee.Player("bob", 1)
    game = yahtzee.Game(game_num=0, player=player)

    game.ones = 1
    game.twos = 2
    game.threes = 3
    game.fours = 4
    game.fives = 5
    game.sixes = 6

    game.three_of_a_kind = 7
    game.four_of_a_kind = 8
    game.full_house = 9
    game.small_straight = 10
    game.large_straight = 11
    game.yahtzee = 100
    game.chance = 12
    game.mark_yahtzee_bonus()
    game.mark_yahtzee_bonus()
    game.mark_yahtzee_bonus()


def test_game_printing():
    player = yahtzee.Player("charlie", 2)
    game = yahtzee.Game(game_num=0, player=player)

    game.ones = 3
    game.yahtzee = 100
    game.mark_yahtzee_bonus()

    print(game)
