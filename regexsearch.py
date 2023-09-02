import re

def regex_search(data, pattern):
    matches = re.findall(pattern, data)
    return matches

def main():
    data = "some text with sensitive information 2023-08-01"
    pattern = r"\b\d{4}-\d{2}-\d{2}\b(.*?)\b" # Example regex pattern for date format
    matches = regex_search(data, pattern)
    print("Matched patterns:", matches)

if __name__ == '__main__':
    main()
