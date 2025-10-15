import requests

def fetch_constitution_lines(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.text.splitlines()

def search_and_print(lines, term):
    term_l = term.lower()
    i = 0
    printed = set()
    N = len(lines)
    while i < N:
        if term_l in lines[i].lower():
            # find start
            start = i
            while start > 0 and lines[start].strip() != "":
                start -= 1
            if lines[start].strip() == "":
                start += 1
            # find end
            end = i
            while end < N and lines[end].strip() != "":
                end += 1
            key = (start, end)
            if key not in printed:
                printed.add(key)
                print()
                for j in range(start, end):
                    print(f"Line {j+1}: {lines[j]}")
                print()
            i = end
        else:
            i += 1

def main():
    url = "https://brucebauer.info/constitution.txt"
    try:
        lines = fetch_constitution_lines(url)
    except Exception as e:
        print("Error downloading constitution:", e)
        return

    while True:
        term = input("Enter search term: ").strip()
        if term == "":
            print("Exiting.")
            break
        search_and_print(lines, term)

if __name__ == "__main__":
    main()
