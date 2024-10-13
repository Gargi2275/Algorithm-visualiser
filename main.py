import InsertionSort, SelectionSort, QuickSort, MergeSort, BubbleSort
print('''
Welcome to Algorithm Visualizer!
Please choose an algorithm to visualize the sorting :
1. Insertion Sort
2. Selection Sort
3. Quick Sort
4. Merge Sort
5. Bubble Sort
6. Exit''')
user_input = int(input("Enter your choice: "))
if user_input == 1:
    InsertionSort.initialize_visualization()
elif user_input == 2:
    SelectionSort.initialize_visualization()
elif user_input == 3:
    QuickSort.initialize_visualization()
elif user_input == 4:
    MergeSort.initialize_visualization()
elif user_input == 5:
    BubbleSort.initialize_visualization()

