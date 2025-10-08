def ParseDegreeString(ddmmss):
    deg_symbol = chr(176)
    min_symbol = "'"
    sec_symbol = '"'

    deg_index = ddmmss.index(deg_symbol)
    min_index = ddmmss.index(min_symbol)
    sec_index = ddmmss.index(sec_symbol)

    degrees = float(ddmmss[:deg_index])
    minutes = float(ddmmss[deg_index + 1:min_index])
    seconds = float(ddmmss[min_index + 1:sec_index])

    return degrees, minutes, seconds

def DDMMSStoDecimal(deg, min, sec):
    return deg + min / 60 + sec / 3600

def main():
    input_file = "07.Project Angles Input.txt"
    output_file = "07.Project Angles Output.txt"
    results = []

    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                try:
                    d, m, s = ParseDegreeString(line)
                    decimal = DDMMSStoDecimal(d, m, s)
                    results.append(decimal)
                except Exception as e:
                    print(f"Skipping line '{line}': {e}")

        with open(output_file, "w", encoding="utf-8") as outfile:
            for val in results:
                outfile.write(f"{val}\n")

        print(f"{len(results)} records processed")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")

if __name__ == "__main__":
    main()
