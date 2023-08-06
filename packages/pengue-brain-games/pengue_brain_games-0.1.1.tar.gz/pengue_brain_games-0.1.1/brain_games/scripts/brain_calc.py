#!/usr/bin/env python3
import brain_games.game_engine
from brain_games.games import brain_calc


def main():
    brain_games.game_engine.run_game(brain_calc)


if __name__ == '__main__':
    main()
