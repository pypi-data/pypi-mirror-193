from client import PlaygroundClient
import random, math
import json
import sys


# The following line are an example of how to use the API
class TestTicTacToe(PlaygroundClient):
    def __init__(self, auth, endpoint="https://stagingcdn.playgroundrl.com:8083"):
        super().__init__(
            "tic_tac_toe",
            model_name="tic_tac_toe_robot" + str(random.randrange(100, 1000)),
            auth=auth,
            endpoint=endpoint,
            max_exchange=5000,
            game_type=2,
            render_gameplay=True
        )

    def callback(self, state, reward):
        # Todo: After talking with Rayan
        # move this to JSON and user to checking to super class
        state = json.loads(state)
        board = state["board"]

        if not self.is_current_user_move(state):
            return None

        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == 0:
                    # Choose first open state
                    return str(i * 3 + j)

    def gameover_callback(self):
        pass


"""
run this in two windows to test:
    python -m test.tic_tac_toe.py 0
    python -m test.tic_tac_toe.py 1
"""
email_options = ["test@gmail.com", "test2@gmail.com"]
if len(sys.argv) > 1:
    email = email_options[int(sys.argv[-1])]
else:
    email = email_options[0]

endpoint = "http://localhost:8083/"
#auth = {"email": email, "api_key": "400"}
auth = {"email": "leland@stanford.edu", "api_key": "a4ik5VlWDQ2GNP8GATCHJ5z8TGsMy_ODkTEPCPCtVus"}
#endpoint = "https://stagingcdn.playgroundrl.com:8083/"
t = TestTicTacToe(auth=auth, endpoint=endpoint)
t.run()
