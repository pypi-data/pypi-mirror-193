import sys
from datetime import datetime

import numpy as np


def say_hello_with_message(msg: str) -> str:
    """Awesome function to say hello with message.

    Args:
        msg (str): The message of your dreams.

    Returns:
        str: The standard sentence with your message.
    """
    current_time = datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S") + "-UTC"
    return f"Hello, the message is: {msg}. The current time is: {current_time}."


def wow(quantity: float) -> str:
    """Diplays a Numpy array with one element."""
    return f"Numpy result: {np.array([quantity])}"


def run() -> None:
    # Read arguments:
    input_msg = sys.argv[1]

    # Execute function:
    print(say_hello_with_message(input_msg))


if __name__ == "__main__":  # pragma: no cover
    run()
