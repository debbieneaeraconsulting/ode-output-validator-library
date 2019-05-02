import json
import queue
from argparse import ArgumentParser
from odevalidator import TestCase

if __name__ == '__main__':
    """
    Provided for convenience. Allows users to perform validation using only the library.
    Arguments:
      --data-file (string): Newline-separated file containing records in json format.

    Output:
      Prints results in json.dumps format.
    """
    parser = ArgumentParser()
    parser.add_argument("--data-file", dest="data_file_path", help="Path to log data file that will be sent to the ODE for validation.", metavar="DATAFILEPATH", required=True)
    args = parser.parse_args()

    msg_list = []
    with open(args.data_file_path, 'r') as f:
        msg_list = f.read().splitlines()

    msg_queue = queue.Queue()
    for msg in msg_list:
        msg_queue.put(msg)

    results = TestCase().validate_queue(msg_queue)
    print(json.dumps(results))