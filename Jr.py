
with open('speed.txt', 'r') as file:
    speeds = [float(line.strip()) for line in file.readlines()]

t = 1/100
m = 82.0

Jr_list = []

for a in speeds:
    Jr = m * a * t
    Jr_list.append(Jr)


output_file_path = 'Jr.txt'
with open(output_file_path, 'w') as output_file:
    for result in Jr_list:
        output_file.write(f"{result:.2f}\n")

print(f"Results written to {output_file_path}")
