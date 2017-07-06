import reports
import csv

answer = [
    reports.count_games("game_stat.txt"),
    reports.decide("game_stat.txt", 2009),
    reports.get_latest("game_stat.txt"),
    reports.count_by_genre("game_stat.txt", "First-person shooter"),
    reports.get_line_number_by_title("game_stat.txt", "The Sims"),
    ]


def export_file(file_name):
    csvfile = input("Name a file where to export: ")
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(answer)


export_file("game_stat.txt")
