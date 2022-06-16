import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-a", "--as-number", help="AS number you want to target", type=str)
group.add_argument("-f", "--file", help="Enter a file containing AS numbers")
parser.add_argument("-o", "--output", help="Name of the output file")
ARGS = parser.parse_args()

BASE_URL = "https://ipinfo.io/AS"
USER_AGENT = {'User-agent': 'Mozilla/5.0'}
RESULTS = []


def process_input() -> list[str]:
    if ARGS.file:
        with open(ARGS.file, "r") as handle:
            urls = handle.readlines()
        urls = list(map(lambda u: u.strip(), urls))
    else:
        urls = [ARGS.as_number]
    return urls


def numbers_only_validator(numbers: list[str]) -> list[str]:
    result = []
    for number in numbers:
        if not str.isdecimal(number):
            print(f"{number} is invalid!")
            continue
        result.append(number)
    return result


def make_request_and_parse_response(as_number: str) -> None:
    bla = []
    res = requests.get(f"{BASE_URL}{as_number}", headers=USER_AGENT).content
    soup = BeautifulSoup(res, "html.parser")
    container = soup.find(id="ipv4-data")

    # Stops script from breaking in case there aren't any results
    if not container:
        return
    links = container.findAll('a')

    for idx, ip_range in enumerate(links):
        if "Show" not in ip_range.contents[0]:
            bla.append(f"{ip_range.contents[0]}")
    RESULTS.append(",".join(bla))


def main():
    numbers = process_input()
    validated_numbers = numbers_only_validator(numbers)
    print(f"Starting requests for {len(validated_numbers)} AS numbers...")

    for number in validated_numbers:
        make_request_and_parse_response(number)
    if not RESULTS:
        print("Sorry better luck next time!")
        exit()

    [print(x) for x in RESULTS]
    if ARGS.output:
        with open(ARGS.output, "w") as handle:
            [handle.write(x.replace(",", "\n")) for x in RESULTS]


if __name__ == '__main__':
    main()