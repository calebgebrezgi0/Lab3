"""
Word Count
Caleb Gebrezgi
Presents 4 files and allows a user to pick one to analyze.
10/01/2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self):
        try:
            if not self._filepath.exists():
                raise FileNotFoundError

            table = str.maketrans("", "", string.punctuation)
            with self._filepath.open(encoding="utf-8") as file:
                for line in file:
                    line = line.translate(table)
                    line = line.lower()
                    for word in line.split():
                        self._frequencies[word] = self._frequencies.get(word, 0) + 1
            return True
        except FileNotFoundError:
            print(f"Error: '{self._filepath}' was not found.")
            return False

    def print_report(self):
        for word in sorted(self._frequencies.keys()):
            print(f"{word:<10} :: {self._frequencies[word]}")


def main():
    files = {
        "1": Path("princess_mars.txt"),
        "2": Path("Tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt"),
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        for key, path in files.items():
            print(f"{key}. {path.stem}")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in files:
            analyzer = WordAnalyzer(files[choice])
            if analyzer.process_file():
                print(f"\nWord frequencies for {files[choice].stem}:\n")
                analyzer.print_report()
        else:
            print("Invalid choice. Please select from 1-5.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()