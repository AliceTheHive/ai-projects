"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
from random import randint

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass

#these are just used to pass the tests
def custom_score(game, player):
    return float(1)
def custom_score_2(game, player):
    return float(1)
def custom_score_3(game, player):
    return float(1)


def defensive(game, player):
    """
    My moves minus my opponents moves (Neutral)

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    score = float(2*own_moves - opp_moves)

    return score

def aggressive(game, player):
    """
    My moves minus my opponents moves (Aggressive)
    """
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    score = float(own_moves - 2*opp_moves)

    return score

def distance_from_center(game, current_position):
    """
    Calculated score based on distance of current position from the center of the board
    """
    x, y = current_position
    center_x, center_y = game.width / 2, game.height / 2
    return (game.width - center_x) ** 2 + (game.height - center_y) ** 2 - (x - center_x) ** 2 - (y - center_y) ** 2

def cutoff_heuristics(game, player):
    """Changes the coefficients applied to player and its opponent based
    on where we are in the game.
    At the beginning of the game (blanks > 35), be more aggressive:
    own_moves - 3 * opp_moves
    At the end of the game, be more defensive:
    3 * own_moves - opp_moves
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).
    player : hashable
        One of the objects registered by the game object as a valid player.
        (i.e., `player` should be either game.__player_1__ or
        game.__player_2__).
    Returns
    ----------
    float
        The heuristic value of the current game state
    """

    blanks = len(game.get_blank_spaces())

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    if blanks > 35:
        return float(own_moves - 3 * opp_moves)
    else:
        return float(3 * own_moves - opp_moves)

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=defensive, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def active_player(self, game):
        return game.active_player == self

    def minimax_execute(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        #stop searching if you have reached the threshold
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        #once you have reached the leaves of the tree, 
        #then evaluate the position using the heuristic
        if depth == 0:
            return self.score(game, self), game.get_player_location(self)

        #if you are the active player, then baseline score is -inf
        if game.active_player == self:
            best_score = float('-inf')
        #if opponent is the active player, then baseline score is +inf
        else:
            best_score = float('inf')

        #default best move
        best_move = (-1, -1)
        possible_moves = game.get_legal_moves()

        if len(possible_moves) == 0:
            return self.score(game, self), (-1, -1)

        for move in possible_moves: #iterate over all possible moves
            next_position = game.forecast_move(move)
            score, _move = self.minimax_execute(next_position, depth - 1)

            if game.active_player == self:
                if score >= best_score:
                    best_score = score
                    best_move  = move
            else:
                if score <= best_score:
                    best_score = score
                    best_move  = move

        return best_score, best_move


    def minimax(self, game, depth):
        optimal_move = self.minimax_execute(game, depth)
        return optimal_move[1]


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """
    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        #implementation of iterative deepening
        try:
            #iterate through all possible depths in the game until time runs out
            for depth in range(1, game.width * game.height):
                best_move = self.alphabeta(game, depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.

        --alpha is the lowest score you are willing to accept (maximum lower bound)
        --beta is the highest score your opponent is willing to accept (minimum upper bound)
        
        alpha beta pruning is essentially the same as minimax except you stop evaluating 
        possible moves once you hit alpha and beta thresholds
        """


        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        possible_moves = game.get_legal_moves() 

        if not possible_moves:
            return (-1, -1)

        best_move = (-1, -1)
        score = float("-inf")

        for move in possible_moves:
            next_position = game.forecast_move(move)
            v = self.min_value(next_position, depth - 1, alpha, beta)
            alpha = max([v, alpha])
            if score < v:
                score = v
                best_move = move
        return best_move

    def max_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0 or len(game.get_legal_moves()) == 0:
            return self.score(game, self)

        v = float("-inf")
        legal_moves = game.get_legal_moves()

        for move in legal_moves:
            next_position = game.forecast_move(move)
            v = max(v, self.min_value(next_position, depth - 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max([v, alpha])
        return v

    def min_value(self, game, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0 or len(game.get_legal_moves()) == 0:
            return self.score(game, self)

        v = float("inf")
        legal_moves = game.get_legal_moves()

        for move in legal_moves:
            next_position = game.forecast_move(move)
            v = min(v, self.max_value(next_position, depth - 1, alpha, beta))
            if v <= alpha:
                return v
            beta = min([v, beta])
        return v