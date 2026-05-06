"""third assidnment"""

def solve_median_maintenance(filename):
    """implemented median algorithm aimed at calculating 10000 medians"""
    sorted_list = []
    total_median_sum = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            val = line.strip()
            if not val:
                continue
            new_num = int(val)

            inserted = False
            for i in range(len(sorted_list)):
                if new_num < sorted_list[i]:
                    sorted_list.insert(i, new_num)
                    inserted = True
                    break

            if not inserted:
                sorted_list.append(new_num)

            k = len(sorted_list)
            if k % 2 == 1:
                median_index = (k + 1) // 2 - 1
            else:
                median_index = (k // 2) - 1

            total_median_sum += sorted_list[median_index]

        return total_median_sum % 10000


print(solve_median_maintenance("median.txt"))
