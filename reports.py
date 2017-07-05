def count_games(file_name):
    with open(file_name) as all_games:
        names_of_games = [sublist.split("\t")[0] for sublist in all_games]
        games = len(names_of_games)
        return games


def decide(file_name, year):
    with open(file_name) as all_games:
        for line in all_games:
            games_file = [sublist.split("\t") for sublist in all_games]
            for game in games_file:
                if int(game[2]) == year:
                    return True


def get_latest(file_name):
    with open(file_name) as all_games:
        latest_year = 0
        latest_title = str()
        for line in all_games:
            year = int(line.split("\t")[2])
            title = line.split("\t")[0]
            if year > latest_year:
                latest_year = year
                latest_title = title
        return (latest_title)


def count_by_genre(file_name, genre):
    game_genre = 0
    with open(file_name) as all_games:
            for line in all_games.readlines():
                if genre == line.split("\t")[3]:
                    game_genre += 1
    return game_genre


def get_line_number_by_title(file_name, title):
    with open(file_name) as all_games:
            for num, line in enumerate(all_games.readlines(), 1):
                if title == line.split("\t")[0]:
                    return num
            raise ValueError("There is no name like this in the game list")
