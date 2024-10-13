import matplotlib.pyplot as plt

def visualize_sorting(number_list, compare_indices=None, color='skyblue'):
    plt.clf()
    if compare_indices:
        colors = []
        for i in range(len(number_list)):
            if i in compare_indices:
                colors.append('green')
            else:
                colors.append(color)
    else:
        colors = color
    plt.bar(range(len(number_list)), number_list, color=colors)
    for i in range(len(number_list)):
        plt.text(i,number_list[i], str(number_list[i]), ha='center', va='bottom')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorting Visualization')
    plt.pause(0.31)

def initialize_visualization():
    number_list = eval(input("Enter numbers to sort:"))

    length = len(number_list)

    for i in range(length - 1):
        for j in range(length - 1 - i):
            if number_list[j] > number_list[j + 1]:
                visualize_sorting(number_list, compare_indices=[j, j + 1])  # Pass indices being compared
                number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]

    # Final visualization after sorting is complete, with all bars colored orange
    visualize_sorting(number_list, color='orange')
    plt.show()
    print(f"The sorted numbers are: {number_list}")
