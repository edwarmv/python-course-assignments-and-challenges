import csv
import io

data = io.open("example.csv", encoding="utf-8")

csv_data = csv.reader(data)

data_lines = list(csv_data)


def get_fullnames():
    for data_line in data_lines[1:10]:
        yield f"{data_line[1]} {data_line[2]}"


print("Fullname")
print(list(get_fullnames()))

# new file
file_to_output = io.open("to_save_file.csv", "w", newline="")
csv_writer = csv.writer(file_to_output, delimiter=",")
csv_writer.writerow(["a", "b", "c"])
csv_writer.writerows([["1", "2", "3"], ["4", "5", "6"]])
file_to_output.close()

# existing file
f = io.open("to_save_file.csv", "a", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["new", "new", "new"])
f.close()
