import reports
import csv


functions = [
    reports.get_most_played("game_stat.txt"),
    ("\n"),
    reports.sum_sold("game_stat.txt"),
    ("\n"),
    reports.get_selling_avg("game_stat.txt"),
    ("\n"),
    reports.count_longest_title("game_stat.txt"),
    ("\n"),
    reports.get_date_avg("game_stat.txt"),
    ("\n"),
    reports.get_game("game_stat.txt", "Minecraft"),
    ]


def export_file(file_name):
    csvfile = input("Give a name for a file to export: ")
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(functions)


export_file("game_stat.txt")
