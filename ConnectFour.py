from argparse import ArgumentParser, ArgumentTypeError
from ConnectFourState import ConnectFour
from Agents import MinimaxAgent, AlphaBetaAgent
from Functions import DefaultEval
import re

def str_to_board(string):
    match = re.compile(r'((?:\.|r|y){7},?){6}').match(string)
    if not match or match.group() != string:
        raise ArgumentTypeError(f'Invalid board: {string}')
    return string

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('state', help='Current board state', type=str_to_board)
    parser.add_argument('player', help='Current player', choices=['red', 'yellow'])
    agent_args = parser.add_argument_group('Agent options')
    agent_args.add_argument('agent', help='Agent to use', choices=['A', 'M'], nargs='?')
    agent_args.add_argument('depth', help='Agent search depth', type=int, nargs='?')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    state = ConnectFour.from_string(args.player, args.state)
    eval_fn = DefaultEval(args.player)
    if args.agent == 'A':
        agent = AlphaBetaAgent(eval_fn, args.depth)
    elif args.agent == 'M':
        agent = MinimaxAgent(eval_fn, args.depth)
    else:
        raise NotImplemented
    print(agent.compute_action(state))
    print(agent.expanded)
