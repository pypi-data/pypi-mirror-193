import socketio
from abc import ABC, abstractmethod
import random
import requests
import webbrowser
from urllib.parse import urljoin


# TODO: Handle retrying and what happens if we never receive a message back ()
# TODO: Turn print statements into logging statements
# TODO: Turn Dict messages into classes
# TODO: Kill the client better, sometimes it hangs
# TODO: Create enums for game_types (MODEL_ONLY=1, OPEN_POOL=2)
class PlaygroundClient(ABC):
    def __init__(
        self,
        game,
        model_name,
        auth,
        game_type=1,  # must be 1 or 2
        endpoint="https://cdn.playgroundrl.com:8083",
        max_exchange=20,
        num_games=1,
        render_gameplay=False
    ):
        """
        An API to handle one game.
        """

        assert(game_type in [1, 2])
        assert(num_games >= 1)

        # Retrieve user id
        # urljoin has weird behavior when it's not terminated right
        if not endpoint.endswith('/'):
            endpoint += '/'
        url = urljoin(endpoint, 'email_to_uid')
        response = requests.get(url, params={"email": auth["email"]})
        assert(response.text != "email not found")
        assert(response.status_code == 200)
        self.user_id = response.text

        print("Connecting....")
        self.sio = socketio.Client()
        socket_auth = {"user_id": self.user_id, "api_key": auth["api_key"], "is_human": False}

        self.sio.connect(endpoint, auth=socket_auth, namespaces=["/"])
        self.register_handlers()
        print("Connected!")

        self.server_side_sid = None
        if render_gameplay:
            self.sio.emit("request_server_side_sid", {})

        self.game = game
        self.model_name = model_name
        self.game_type = game_type
        self.num_games = num_games
        self.render_gameplay = render_gameplay
        self.game_id = None
        self.endpoint = endpoint

        # Temporary variable to limit number of messages received
        # Todo: Find a more elegant solution to prevent infinite loops
        self.max_exchange = max_exchange
        self.exchanged = 0

    def is_current_user_move(self, state):
        _user = state["player_moving"]
        _model_name = state["model_name"]
        return self.user_id == _user and self.model_name == _model_name


    def register_handlers(self):
        self.sio.on("return_server_side_sid", lambda msg: self._on_get_server_side_sid(msg))
        self.sio.on("state_msg", lambda msg: self._on_state_msg(msg))
        # this now happens by default, when the state updated correctly
        self.sio.on("ack", lambda msg: self._on_action_ack_msg(msg))
        self.sio.on("game_over", lambda msg: self._on_game_over_msg(msg))
        self.sio.on("send_game_id", lambda msg: self._on_send_game_id_msg(msg))
        self.sio.on("exception", lambda msg: self._on_error_msg(msg))
        self.sio.on("*", lambda type, msg: self._default_callback(self, type, msg))

    @abstractmethod
    def callback(self, state: str, reward: str) -> str:
        """
        Instances implement this with their RL strategies.
        Returns the action for the client to take,
        or none for no action.
        """
        # TODO: Make self, state, and reward proper objects
        pass

    @abstractmethod
    def gameover_callback(self):
        """Run some action when the game ends"""
        pass

    def _on_get_server_side_sid(self, msg):
        self.server_side_sid = msg["server_side_sid"]

    def _on_state_msg(self, msg):
        print(" --state_msg received: ", msg)
        state = msg["state"]
        reward = msg["reward"]
        is_game_over = msg["is_game_over"]
        if is_game_over or self.exchanged > self.max_exchange:
            print(
                "Game is over or max number of messages has been reached..."
            )
            self.gameover_callback()
            # self.sio.disconnect()
            return

        # Use user defined function to determine callback
        action = self.callback(state, reward)
        if action is not None:
            payload = {"action": action, "game_id": self.game_id}
            print(" -- sending action: ", action)
            self.sio.emit("submit_agent_action", payload)

        self.exchanged += 1

    def _on_action_ack_msg(self, msg):
        print(" --ack message received", msg)
        # self.sio.emit('get_state', {'game_id': self.game_id})

    # TODO: handle this gracefully
    def _on_game_over_msg(self, msg):
        print("  --Game ended. Outcome:", msg["outcome"])
        if self.num_games <= 0:
            self.sio.disconnect()
            exit()
        self.run()

    def _on_send_game_id_msg(self, msg):
        print("  --send_game_id message received", msg)
        if self.render_gameplay and self.game_id is None and self.server_side_sid is not None:
            # TODO: figure out a cleaner way to do this
            url = self.endpoint.replace(":8083/", "/").replace("stagingcdn", "dev").replace("cdn.", "")
            if ".com" not in url:
                url = url[:-1]
                url += ":3000/"
            webbrowser.open(url
                            + self.game.replace("_", "")
                            + "/?listen_to_sid="
                            + self.server_side_sid)

        self.game_id = msg["game_id"]
        assert self.game_id is not None
        self.sio.emit("get_state", {"game_id": self.game_id})


    def _default_callback(self, msg_type, msg):
        raise Exception("Received unexpected data from server: " + msg_type + msg)

    def _on_error_msg(self, msg):
        raise Exception(msg)

    def run(self):
        """
        Server and client will repeatedly
        """
        print("  --running")
        self.num_games -= 1
        self.sio.emit(
            "start_game",
            {
                "game": self.game,
                "game_type": self.game_type,
                "model_name": self.model_name,
            },
        )
        self.sio.wait()
