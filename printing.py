import reports


def printing_answers(file_name):
    print (reports.count_games(file_name))
    print (reports.decide(file_name, 2009))
    print (reports.get_latest(file_name))
    print (reports.count_by_genre(file_name, "RPG"))
    print (reports.get_line_number_by_title(file_name, "Half-Life"))

printing_answers("game_stat.txt")
