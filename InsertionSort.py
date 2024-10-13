import matplotlib.pyplot as plt

def visualize_sorting(number_list,compare_indices=None, color='skyblue', min_index=None,comaparing=False):
    plt.clf()
    if compare_indices:
        colors = []
        for i in range(len(number_list)):
            if comaparing:
                if i in compare_indices:
                    colors.append('green')
                else:
                    colors.append(color)
            else:
                if i in compare_indices:
                    colors.append('magenta')
                else:
                    colors.append(color)
    else:
        colors=color
    plt.bar(range(len(number_list)), number_list, color=colors)
    for i in range(len(number_list)):
        plt.text(i, number_list[i], str(number_list[i]), ha='center', va='bottom')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorting Visualization')
    plt.pause(2)

def initialize_visualization():
    number_list = eval(input("Enter numbers to sort: "))
    for i in range(1, len(number_list)):
        x = number_list[i]
        j = i - 1
        while (j >= 0 and x < number_list[j]):
            number_list[j + 1] = number_list[j]
            visualize_sorting(number_list, compare_indices=[j, j + 1], comaparing=True)
            j = j - 1
        number_list[j + 1] = x
        visualize_sorting(number_list, compare_indices=[j + 1])
    visualize_sorting(number_list, color='orange')
    print("The sorted numbers are: ",number_list)