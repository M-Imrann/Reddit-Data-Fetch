import argparse


def parse_args():
    """
    parse_args() function parse the arguments
    """
    parser = argparse.ArgumentParser(
        description="Fetch and Process the Reddit Data"
        )

    parser.add_argument("--name",
                        type=str,
                        required=True,
                        help="Subreddit name")

    parser.add_argument("--limit",
                        type=int,
                        default=10,
                        help="Post Limit")

    parser.add_argument("--score",
                        type=float,
                        default=5.0,
                        help="Minimum Score"
                        )

    return parser.parse_args()
