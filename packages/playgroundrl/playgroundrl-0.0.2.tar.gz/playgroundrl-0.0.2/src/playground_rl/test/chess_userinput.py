from ..client import PlaygroundClient
import random, math
import json
from stockfish import Stockfish
import attrs


# The following line are an example of how to use the API
class TestChess(PlaygroundClient):
    def __init__(self, auth, endpoint="http://44.205.255.44:8083"):
        super().__init__(
            "chess",
            model_name="chessrobot" + str(random.randrange(100, 1000)),
            auth = auth,
            endpoint=endpoint,
            max_exchange=5000,
            game_type=2,
        )

    def callback(self, state, reward):
        state = json.loads(state)

        # TODO: Abstract serialization and deserialization
        if not self.is_current_user_move(state):
            return None

        print("FEN: ", state['fen'])
        print("Input Move (UCI format, e.g. a2a3): ")
        move_str = input()
        action = {
            'uci': move_str
        }
        return json.dumps(action)

    def gameover_callback(self):
        pass


endpoint = "http://127.0.0.1:8083"
auth = {"email": "jane@stanford.edu", "api_key": "pDJSu9ZiSGQ8DdttMvC3gx44HvyeALhqWARL9CeUH4g"}

t = TestChess(auth = auth, endpoint=endpoint)
t.run()
