def read_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def is_integer_within_range(string):
    try:
        num = int(string)
        return -1023 <= num <= 1023
    except ValueError:
        return False

def filter_integers(data):
    integers = set()
    for item in data:
        if is_integer_within_range(item):
            integers.add(int(item))
    return list(integers)

def Sort_Unique(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Sort_Unique(left) + middle + Sort_Unique(right)

def main(file_name):
    data = read_file(file_name)
    integers = filter_integers(data)
    sorted_unique_integers = Sort_Unique(integers)
    print("Unique Integer:", sorted_unique_integers)
    print("Total Unique Integer:", len(sorted_unique_integers))

if __name__ == "__main__":
    file_name = "sample_input_for_students/sample_01.txt"  # Change this to your file name or pass as an argument
    main(file_name)