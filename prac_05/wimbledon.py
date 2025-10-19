"""
wimbledon.py
CP1404/CP5632 Practical

Program to read Wimbledon champions data, count wins, and list winning countries.

Time Estimate: 30 minutes
Actual Time: 25 minutes
"""

import csv

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Reads champion data from a file and prints win counts and countries."""
    data = load_data(FILENAME)
    champion_to_count, winning_countries = process_data(data)
    display_results(champion_to_count, winning_countries)


def load_data(filename):
    """
    Loads data from the CSV file, skipping the header.
    Handles the UTF-8 BOM encoding.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for row in reader:
            data.append(row)
    return data


def process_data(data):
    """
    Processes the list of lists data to extract win counts and countries.

    Returns:
        tuple: (champion_to_count, winning_countries)
    """
    champion_to_count = {}
    winning_countries = set()
    for row in data:
        country = row[COUNTRY_INDEX]
        champion = row[CHAMPION_INDEX]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
        winning_countries.add(country)

    return champion_to_count, winning_countries


def display_results(champion_to_count, winning_countries):
    """Displays the champion win counts and the sorted list of countries."""
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    print()
    sorted_countries = sorted(list(winning_countries))
    countries_string = ", ".join(sorted_countries)
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(countries_string)


main()