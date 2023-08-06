from ..client import PlaygroundClient
import random, math
import json
from stockfish import Stockfish
import attrs


# The following line are an example of how to use the API
class TestStockfishChess(PlaygroundClient):
    def __init__(self, stockfish_path, auth, endpoint="http://44.205.255.44:8083"):
        super().__init__(
            "chess",
            model_name="chessrobot" + str(random.randrange(100, 1000)),
            endpoint=endpoint,
            auth = auth,
            max_exchange=5000,
            game_type=2,
        )
        self.stockfish = Stockfish(stockfish_path)

    def callback(self, state, reward):
        state = json.loads(state)

        # TODO: Abstract serialization and deserialization
        if not self.is_current_user_move(state):
            return None

        fen = state['fen']
        self.stockfish.set_fen_position(fen)
        move = self.stockfish.get_best_move()
        print("MOVE", move)
        action = {
            'uci': move
        }
        return json.dumps(action)

    def gameover_callback(self):
        pass

# REPLACE ME WHEN YOU RUN IT 
path = 'C:\\Users\\langs\\Downloads\\stockfish_15.1_win_x64_avx2\\stockfish_15.1_win_x64_avx2\\stockfish-windows-2022-x86-64-avx2.exe'
endpoint = "http://127.0.0.1:8083"
auth = {"email": "jane@stanford.edu", "api_key": "pDJSu9ZiSGQ8DdttMvC3gx44HvyeALhqWARL9CeUH4g"}

t = TestStockfishChess(path, auth,  endpoint=endpoint)
t.run()
