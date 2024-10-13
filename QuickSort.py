import matplotlib.pyplot as plt

def visualize_sorting(number_list, compare_indices=None, color='skyblue', pivot_index=None):
    plt.clf()
    colors = [color] * len(number_list)
    if compare_indices:
        for i in compare_indices:
            colors[i] = 'magenta'
    if pivot_index is not None:
        colors[pivot_index] = 'green'
    plt.bar(range(len(number_list)), number_list, color=colors)
    for i in range(len(number_list)):
        plt.text(i, number_list[i], str(number_list[i]), ha='center', va='bottom')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorting Visualization')
    plt.pause(1)

def quick_sort(number_list, start, end):
    if start < end:
        pivot_index = partition(number_list, start, end)
        visualize_sorting(number_list, pivot_index=pivot_index)
        quick_sort(number_list, start, pivot_index - 1)
        quick_sort(number_list, pivot_index + 1, end)

def partition(number_list, start, end):
    pivot = number_list[end]
    i = start - 1
    for j in range(start, end):
        if number_list[j] < pivot:
            i += 1
            number_list[i], number_list[j] = number_list[j], number_list[i]
            visualize_sorting(number_list, compare_indices=[i, j])
    number_list[i + 1], number_list[end] = number_list[end], number_list[i + 1]
    visualize_sorting(number_list, compare_indices=[i + 1, end])
    return i + 1

def initialize_visualization():
    number_list = eval(input("Enter numbers to sort: "))
    quick_sort(number_list, 0, len(number_list) - 1)
    visualize_sorting(number_list, color='orange')
    print("The sorted numbers are: ",number_list)
