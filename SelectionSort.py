import matplotlib.pyplot as plt

def visualize_sorting(number_list, compare_indices=None, color='skyblue', min_index=None,comaparing=False):
    plt.clf()
    if compare_indices:
        colors = []
        for i in range(len(number_list)):
            if comaparing:
                if i in compare_indices:
                    colors.append('magenta')  # Highlight current minimum value being compared
                else:
                    colors.append(color)
            else:
                if i in compare_indices:
                    colors.append('green')
                else:
                    colors.append(color)
    else:
        colors = color
    plt.bar(range(len(number_list)), number_list, color=colors)
    for i in range(len(number_list)):
        plt.text(i, number_list[i], str(number_list[i]), ha='center', va='bottom')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorting Visualization')
    plt.pause(1)

def initialize_visualization():
    number_list = eval(input("Enter numbers to sort: "))
    length = len(number_list)

    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if number_list[j] < number_list[min_index]:
                visualize_sorting(number_list, compare_indices=[i, j], min_index=min_index,
                                  comaparing=True)  # Visualize comparison
                min_index = j

        if min_index != i:
            number_list[i], number_list[min_index] = number_list[min_index], number_list[i]
            visualize_sorting(number_list, compare_indices=[i, j], min_index=min_index)  # Visualize comparison
        visualize_sorting(number_list)  # Visualize current state of the list

    # Final visualization after sorting is complete, with all bars colored orange
    visualize_sorting(number_list, color='orange')
    plt.show()
    print("The sorted numbers are: ", number_list)
