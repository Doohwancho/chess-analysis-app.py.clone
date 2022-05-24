import chess
import chess.engine

# Change this if stockfish is somewhere else
engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")

# ...same as before
board = chess.Board("5Q2/5K1k/8/8/8/8/8/8 w - - 0 1")

# Get the 3 best moves
info = engine.analyse(board, chess.engine.Limit(depth=20), multipv=3)

# Info is now an array with at most 3 elements
# If there aren't 3 valid moves, the array would have less than 3 elements
print(info[0])
print(info[1])
print(info[2])

def analyze_position(fen, num_moves_to_return=1, depth_limit=None, time_limit=None):
    search_limit = chess.engine.Limit(depth=depth_limit, time=time_limit)
    board = chess.Board(fen)
    infos = engine.analyse(board, search_limit, multipv=num_moves_to_return)
    return [format_info(info) for info in infos]

def format_info(info):
    # Normalize by always looking from White's perspective
    score = info["score"].white()

    # Split up the score into a mate score and a centipawn score
    mate_score = score.mate()
    centipawn_score = score.score()
    return {
        "mate_score": mate_score,
        "centipawn_score": centipawn_score,
        "pv": format_moves(info["pv"]),
    }

# Convert the move class to a standard string 
def format_moves(pv):
    return [move.uci() for move in pv]

print(analyze_position("8/8/6P1/4R3/8/6k1/2r5/6K1 b - - 0 1", num_moves_to_return=3, depth_limit=20))
