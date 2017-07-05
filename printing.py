import reports


def count_games_print(file_name):
    print (reports.count_games(file_name))


def decide_print(file_name, year):
    print (reports.decide(file_name, year))


def get_latest_print(file_name):
    print (reports.get_latest(file_name))


def count_by_genre_print(file_name, genre):
    print (reports.count_by_genre(file_name, genre))


def get_line_number_by_title(file_name, title):
    print (reports.get_line_number_by_title(file_name, title))


def print_all_the_answers(file_name):
    count_games_print(file_name)
    decide_print(file_name, 2004)
    get_latest_print(file_name)
    count_by_genre_print(file_name, "First-person shooter")
    get_line_number_by_title(file_name, "Half-Life")


print_all_the_answers("game_stat.txt")
