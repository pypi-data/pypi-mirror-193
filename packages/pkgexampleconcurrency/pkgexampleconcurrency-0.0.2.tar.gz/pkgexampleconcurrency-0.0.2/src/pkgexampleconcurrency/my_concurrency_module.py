import argparse


def my_threading():
    my_threading_parser = argparse.ArgumentParser(
        description="Run default threading example"
    )
    my_threading_parser.add_argument(
        "--run", action="store_true", help="Run default threading example"
    )
    my_args = my_threading_parser.parse_args()
    print(my_args.run)


def my_concurrentfutures():
    my_concurrentfutures_parser = argparse.ArgumentParser(
        description="Run default concurrent futures example"
    )
    my_concurrentfutures_parser.add_argument(
        "--run", action="store_true", help="Run default concurrent futures example"
    )
    my_args = my_concurrentfutures_parser.parse_args()
    print(my_args.run)


def my_multiprocessing():
    my_multiprocessing_parser = argparse.ArgumentParser(
        description="Run default multiprocessing example"
    )
    my_multiprocessing_parser.add_argument(
        "--run", action="store_true", help="Run default multiprocessing example"
    )
    my_args = my_multiprocessing_parser.parse_args()
    print(my_args.run)


def my_asyncio():
    my_asyncio_parser = argparse.ArgumentParser(
        description="Run default asyncio example"
    )
    my_asyncio_parser.add_argument(
        "--run", action="store_true", help="Run default asyncio example"
    )
    my_args = my_asyncio_parser.parse_args()
    print(my_args.run)
