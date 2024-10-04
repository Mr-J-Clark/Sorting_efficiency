def selection_sort(x):
    print("### Selection Sort ###")
    arr = x.copy()
    selection_sort_writes = 0
    selection_sort_loops = 0
    selection_sort_reads = 0

    # Traverse through all array elements
    for i in range(len(arr)):
        selection_sort_loops += 1
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                selection_sort_reads += 2  # Reading arr[j] and arr[min_index]
                min_index = j

        # Swap the found minimum element with the first element
        if min_index != i:
            arr[i]  = arr[min_index]   # Write operation
            arr[min_index] = arr[i] # Write operation
            selection_sort_writes += 2  # Writing to arr[i] and arr[min_index]
        print (arr)
    return selection_sort_reads, selection_sort_writes, selection_sort_loops


def bubble_sort(x):
    print("### Bubble Sort ###")
    arr = x.copy()
    bubble_sort_writes = 0
    bubble_sort_reads = 0
    bubble_sort_loops = 0

    for i in range(len(arr)):
        swapped = False
        bubble_sort_loops += 1
        for j in range(len(arr) - 1 - i):  # Compare adjacent elements
            bubble_sort_reads += 2  # Reading arr[j] and arr[j+1]
            if arr[j] > arr[j + 1]:
                bubble_sort_reads += 2  # Reading arr[j] and arr[j+1]
                arr[j]  = arr[j + 1]  # Write operation
                arr[j + 1] = arr[j]  # Write operation
                bubble_sort_writes += 2  # Writing to arr[j] and arr[j+1]
                swapped = True

        if not swapped:
            break
        print(arr)

    return bubble_sort_reads, bubble_sort_writes, bubble_sort_loops


# Test the sorting algorithms
selection_sort_reads, selection_sort_writes, selection_sort_loops = selection_sort([34, 43, 73, 88, 9, 91, 48, 10, 94, 3, 75, 87, 74, 63, 11, 36, 82, 100, 28, 68, 18, 60, 35, 81, 79, 23, 86, 41, 49, 2, 7, 83, 6, 58, 47, 39, 27, 54, 21, 12, 4, 5, 31, 46, 62, 55, 37, 57, 67, 93])
bubble_sort_reads, bubble_sort_writes, bubble_sort_loops = bubble_sort([34, 43, 73, 88, 9, 91, 48, 10, 94, 3, 75, 87, 74, 63, 11, 36, 82, 100, 28, 68, 18, 60, 35, 81, 79, 23, 86, 41, 49, 2, 7, 83, 6, 58, 47, 39, 27, 54, 21, 12, 4, 5, 31, 46, 62, 55, 37, 57, 67, 93])

# Comparison Printout numbers
print("\n### Comparison of Selection Sort and Bubble Sort with numbers ###")
print(f"Selection Sort - Reads: {selection_sort_reads}, Writes: {selection_sort_writes}, Loops: {selection_sort_loops}")
print(f"Bubble Sort    - Reads: {bubble_sort_reads}, Writes: {bubble_sort_writes}, Loops: {bubble_sort_loops}")

# Test the sorting algorithms names
selection_sort_reads, selection_sort_writes, selection_sort_loops = selection_sort(["Eustolia","Nathan","Milissa","Willie","Hoyt","Alexandria","Clelia","Alpha","Delbert","Boyd","Milton","Vivan","Constance","Hilma","Irving","Carie","Nicky","Adele","Carlene","Hermina","Ayana","Frederica","Arianna","Zandra","Vina","Lory","Mao","Alona","Lajuana","Coralie","Allyson","Corey","Geraldo","Sherryl","Monika","Charlesetta","Deon","Coletta","Jed","Carlee","Lise","Teresita","Odelia","Adeline","Olive","Elisha","Casey","Octavia","Alexandra","Franklyn"])
bubble_sort_reads, bubble_sort_writes, bubble_sort_loops = bubble_sort(["Eustolia","Nathan","Milissa","Willie","Hoyt","Alexandria","Clelia","Alpha","Delbert","Boyd","Milton","Vivan","Constance","Hilma","Irving","Carie","Nicky","Adele","Carlene","Hermina","Ayana","Frederica","Arianna","Zandra","Vina","Lory","Mao","Alona","Lajuana","Coralie","Allyson","Corey","Geraldo","Sherryl","Monika","Charlesetta","Deon","Coletta","Jed","Carlee","Lise","Teresita","Odelia","Adeline","Olive","Elisha","Casey","Octavia","Alexandra","Franklyn"
])

# Comparison Printout
print("\n### Comparison of Selection Sort and Bubble Sort  with names###")
print(f"Selection Sort - Reads: {selection_sort_reads}, Writes: {selection_sort_writes}, Loops: {selection_sort_loops}")
print(f"Bubble Sort    - Reads: {bubble_sort_reads}, Writes: {bubble_sort_writes}, Loops: {bubble_sort_loops}")



# Dates
# Convert dd/mm/yyyy to a tuple (yyyy, mm, dd) format for easy comparison
def convert_to_tuple(date_str):
    day, month, year = map(int, date_str.split('/'))
    return year, month, day  # Return a tuple in (yyyy, mm, dd) format


# Selection Sort for dates using manual comparison of the (yyyy, mm, dd) tuple
def selection_sort_dates(dates):
    print("### Selection Sort for Dates ###")

    for i in range(len(dates)):
        min_index = i
        for j in range(i + 1, len(dates)):
            if convert_to_tuple(dates[j]) < convert_to_tuple(dates[min_index]):
                min_index = j
        # Swap the found minimum date with the first date
        if min_index != i:
            dates[i], dates[min_index] = dates[min_index], dates[i]

    return dates


# Bubble Sort for dates using manual comparison of the (yyyy, mm, dd) tuple
def bubble_sort_dates(dates):
    print("### Bubble Sort for Dates ###")

    n = len(dates)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if convert_to_tuple(dates[j]) > convert_to_tuple(dates[j + 1]):
                dates[j], dates[j + 1] = dates[j + 1], dates[j]
                swapped = True
        if not swapped:
            break

    return dates


# Test dates
dates = [
    "29/06/2009", "06/06/1984", "16/06/1993", "23/11/1996", "23/09/1986", "07/07/2002",
    "29/01/1999", "13/06/1998", "14/02/2005", "29/08/2013", "24/12/2009", "04/09/2019",
    "02/02/2020", "22/10/2015", "08/11/1987", "23/10/2018", "14/10/2015", "19/02/2013",
    "05/06/1989", "21/08/1991", "06/06/2005", "03/02/1993", "01/12/1993", "01/09/1995",
    "24/01/2018"
]

# Sorting using Selection Sort
sorted_dates_selection = selection_sort_dates(dates.copy())
print("Dates sorted using Selection Sort:")
print(sorted_dates_selection)

# Sorting using Bubble Sort
sorted_dates_bubble = bubble_sort_dates(dates.copy())
print("Dates sorted using Bubble Sort:")
print(sorted_dates_bubble)