# =========================================================
# Project : Functional Treat
# Topic   : Data Analyzer and Transformer
# =========================================================

# ==================== Global Variables ====================

dataset = []
records = []
report_dataset = {}
summary_dataset = {}


# ==================== Helper Function ====================

def get_flat_dataset_datasetset():
    """Return the datasetset as a 1D list."""
    if not dataset:
        return []

    if isinstance(dataset[0], list):
        flat_dataset = []
        for row in dataset:
            flat_dataset.extend(row)
        return flat_dataset

    return dataset


# ==================== Input 1D Data ====================

def input_1d():
    """Input dataset in 1D list."""
    global dataset

    dataset = list(map(int, input(
        "Enter numbers separated by space: "
    ).split()))

    print("\n1D Data stored successfully!")


# ==================== Input 2D Data ====================

def input_2d():
    """Input dataset in 2D list."""
    global dataset

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    dataset = []

    print("\nEnter the elements:")

    for i in range(rows):
        while True:
            row_values = list(map(int, input(
                f"Row {i + 1}: "
            ).split()))

            if len(row_values) == columns:
                break

            print(
                f"Please enter exactly "
                f"{columns} values."
            )

        dataset.append(row_values)

    print("\n2D Data stored successfully!")


# ==================== Display Data ====================

def display_dataset():
    """Display the stored datasetset."""

    if not dataset:
        print("\nNo dataset available.")
        return

    print("\n========== STORED DATA ==========")

    if isinstance(dataset[0], list):
        print("==============================")

        for row in dataset:
            for value in row:
                print(f"{value:5}", end="")
            print()

        print("==============================")
    else:
        print(dataset)


# ==================== Built-in Functions ====================

def display_summary():
    """Display summary using built-in functions."""
    global summary_dataset

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()

    total_sum_elements = len(flat_dataset)
    total_sum_sum = sum(flat_dataset)
    lowest = min(flat_dataset)
    highest = max(flat_dataset)
    average = total_sum_sum / total_sum_elements

    summary_dataset = {
        "Total Elements": total_sum_elements,
        "Minimum": lowest,
        "Maximum": highest,
        "Sum": total_sum_sum,
        "Average": round(average, 2)
    }

    print("\n========== DATA SUMMARY ==========")
    print("Total Elements :", total_sum_elements)
    print("Minimum Value  :", lowest)
    print("Maximum Value  :", highest)
    print("Sum            :", total_sum_sum)
    print("Average        :", round(average, 2))


# ==================== Average ====================

def calculate_average():
    """Calculate average of the datasetset."""

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()
    average = sum(flat_dataset) / len(flat_dataset)

    print("\nAverage =", round(average, 2))


# ==================== Duplicate Values ====================

def find_duplicates():
    """Find duplicate values."""

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()
    duplicates = []

    for value in flat_dataset:
        if flat_dataset.count(value) > 1 and value not in duplicates:
            duplicates.append(value)

    if duplicates:
        print("\nDuplicate Values :", duplicates)
    else:
        print("\nNo duplicate values found.")


# ==================== Unique Values ====================

def unique_values():
    """Display unique values."""

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()
    unique = []

    for value in flat_dataset:
        if value not in unique:
            unique.append(value)

    print("\nUnique Values :", unique)


# ==================== *args ====================

def display_values(*args):
    """Display multiple values using *args."""

    print("\nValues received using *args:")

    for value in args:
        print(value, end=" ")

    print()


# ==================== **kwargs ====================

def display_datasetset_info(**kwargs):
    """Display datasetset information using **kwargs."""

    print("\n========== DATASET INFORMATION ==========")

    for key, value in kwargs.items():
        print(f"{key} : {value}")


# ==================== Recursion ====================

def factorial(num):
    """Calculate factorial using recursion."""

    if num < 0:
        return None

    if num == 0 or num == 1:
        return 1

    return num * factorial(num - 1)


# ==================== Lambda + Filter ====================

def filter_dataset():
    """Filter values greater than or equal to a limit_value."""

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()

    limit_value = int(input(
        "Enter limit_value value: "
    ))

    filtered_data = list(
        filter(lambda x: x >= limit_value, flat_dataset)
    )

    print("\nFiltered Data :", filtered_data)


# ==================== Lambda + Map ====================

def square_dataset():
    """Square all values using lambda and map."""

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()

    squared_data = list(
        map(lambda x: x * x, flat_dataset)
    )

    print("\nSquared Values :", squared_data)


# ==================== Global Summary ====================

def update_global_summary():
    """Update datasetset summary using global keyword."""
    global summary_dataset

    if not dataset:
        print("\nNo dataset available.")
        return

    flat_dataset = get_flat_dataset_datasetset()

    summary_dataset = {
        "Total Elements": len(flat_dataset),
        "Minimum": min(flat_dataset),
        "Maximum": max(flat_dataset),
        "Sum": sum(flat_dataset),
        "Average": round(sum(flat_dataset) / len(flat_dataset), 2)
    }

    print(
        "\nGlobal datasetset summary "
        "updated successfully."
    )


# ==================== Return Multiple Values ====================

def datasetset_statistics():
    """Return multiple statistics of the datasetset."""

    if not dataset:
        return None

    flat_dataset = get_flat_dataset_datasetset()

    min_value = min(flat_dataset)
    max_value = max(flat_dataset)
    total_sum = sum(flat_dataset)
    average = round(total_sum / len(flat_dataset), 2)

    return min_value, max_value, total_sum, average


# ==================== Display Statistics ====================

def show_statistics():
    """Display statistics returned from datasetset_statistics()."""

    result = datasetset_statistics()

    if result is None:
        print("\nNo dataset available.")
        return

    min_value, max_value, total_sum, average = result

    print("\n========== DATASET STATISTICS ==========")
    print("Minimum :", min_value)
    print("Maximum :", max_value)
    print("Sum     :", total_sum)
    print("Average :", average)


# ==================== Sort 1D List ====================

def sort_1d():
    """Sort a 1D list using sort()."""

    if not dataset:
        print("\nNo dataset available.")
        return

    if isinstance(dataset[0], list):
        print(
            "\nSorting using sort() "
            "is only for 1D list."
        )
        return

    print("\n1. Ascending")
    print("2. Descending")

    choice = int(input(
        "Enter your choice: "
    ))

    if choice == 1:
        dataset.sort()
        print("\nSorted Data :", dataset)

    elif choice == 2:
        dataset.sort(reverse=True)
        print("\nSorted Data :", dataset)

    else:
        print("\nInvalid Choice.")


# ==================== Sort 2D List ====================

def sort_2d():
    """Sort rows of a 2D list using sorted()."""

    if not dataset:
        print("\nNo dataset available.")
        return

    if not isinstance(dataset[0], list):
        print(
            "\nCurrent datasetset is "
            "not a 2D list."
        )
        return

    ordered_dataset = sorted(dataset)

    print("\n========== SORTED 2D LIST ==========")

    for row in ordered_dataset:
        print(row)


# ==================== Function Documentation ====================

def show_documentation():
    """Display documentation of all functions."""

    print("\n========== FUNCTION DOCUMENTATION ==========")

    print("\ninput_1d:")
    print(input_1d.__doc__)

    print("\ninput_2d:")
    print(input_2d.__doc__)

    print("\ndisplay_dataset:")
    print(display_dataset.__doc__)

    print("\ndisplay_summary:")
    print(display_summary.__doc__)

    print("\ncalculate_average:")
    print(calculate_average.__doc__)

    print("\nfind_duplicates:")
    print(find_duplicates.__doc__)

    print("\nunique_values:")
    print(unique_values.__doc__)

    print("\ndisplay_values:")
    print(display_values.__doc__)

    print("\ndisplay_datasetset_info:")
    print(display_datasetset_info.__doc__)

    print("\nfactorial:")
    print(factorial.__doc__)

    print("\nfilter_dataset:")
    print(filter_dataset.__doc__)

    print("\nsquare_dataset:")
    print(square_dataset.__doc__)

    print("\nupdate_global_summary:")
    print(update_global_summary.__doc__)

    print("\ndatasetset_statistics:")
    print(datasetset_statistics.__doc__)

    print("\nshow_statistics:")
    print(show_statistics.__doc__)

    print("\nsort_1d:")
    print(sort_1d.__doc__)

    print("\nsort_2d:")
    print(sort_2d.__doc__)


# ==================== MAIN MENU ====================

while True:
    print("\n")
    print("=" * 50)
    print("              FUNCTIONAL TREAT")
    print("       DATA ANALYZER AND TRANSFORMER")
    print("=" * 50)

    print("1.  Input 1D Data")
    print("2.  Input 2D Data")
    print("3.  Display Data")
    print("4.  Built-in Function Summary")
    print("5.  Calculate Average")
    print("6.  Find Duplicate Values")
    print("7.  Display Unique Values")
    print("8.  Demonstrate *args")
    print("9.  Demonstrate **kwargs")
    print("10. Factorial (Recursion)")
    print("11. Filter Data (Lambda + Filter)")
    print("12. Square Data (Lambda + Map)")
    print("13. Sort 1D List")
    print("14. Sort 2D List")
    print("15. Dataset Statistics")
    print("16. Exit")

    try:
        choice = int(input("\nEnter your choice : "))

    except ValueError:
        print("\nPlease enter a valid number.")
        continue

    if choice == 1:
        input_1d()

    elif choice == 2:
        input_2d()

    elif choice == 3:
        display_dataset()

    elif choice == 4:
        display_summary()

    elif choice == 5:
        calculate_average()

    elif choice == 6:
        find_duplicates()

    elif choice == 7:
        unique_values()

    elif choice == 8:
        display_values(10, 20, 30, 40, 50)

    elif choice == 9:
        if dataset:
            update_global_summary()

            if summary_dataset:
                display_datasetset_info(**summary_dataset)
        else:
            print("\nNo dataset available.")

    elif choice == 10:
        try:
            number = int(input("Enter a number : "))

            if number < 0:
                print(
                    "\nFactorial is not "
                    "defined for negative numbers."
                )
            else:
                print("Factorial =", factorial(number))

        except ValueError:
            print("\nPlease enter a valid integer.")

    elif choice == 11:
        filter_dataset()

    elif choice == 12:
        square_dataset()

    elif choice == 13:
        sort_1d()

    elif choice == 14:
        sort_2d()

    elif choice == 15:
        show_statistics()

    elif choice == 16:
        print(
            "\nThank You for using "
            "Functional Treat!"
        )
        break

    else:
        print(
            "\nInvalid Choice! "
            "Please Try Again."
        )
