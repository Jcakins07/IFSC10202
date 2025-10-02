# 06.Project.py

input_file = "06.Project Input File.txt"
merge_file = "06.Project Merge File.txt"
output_file = "06.Project Output File.text"

input_count = 0
merge_count = 0
output_count = 0

with open(output_file, 'w') as out:
    with open(input_file, 'r') as inp:
        for line in inp:
            if '**Insert Merge File Here**' in line:
                input_count += 1
                with open(merge_file, 'r') as merge:
                    for mline in merge:
                        out.write(mline)
                        merge_count += 1
                        output_count += 1
            else:
                out.write(line)
                input_count += 1
                output_count += 1

print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")
