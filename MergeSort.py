import matplotlib.pyplot as plt

def visualize_sorting(number_list, low=None, high=None, merged_indices=None, temp_indices=None,add_sorted_data=None):
    plt.clf()
    # Original list subplot
    plt.subplot(1, 2, 1)
    plt.bar(range(len(number_list)), number_list, color='skyblue')
    if low is not None and high is not None:
        plt.axvline(x=low - 0.5, color='r', linestyle='--', label='Low Index')
        plt.axvline(x=high + 0.5, color='g', linestyle='--', label='High Index')
    if merged_indices:
        plt.bar(merged_indices, [number_list[i] for i in merged_indices], color='orange', label='Merging process bar')
    for i in range(len(number_list)):
        plt.text(i, number_list[i], str(number_list[i]), ha='center', va='bottom')  # Display numbers on top of bars
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Original List')
    plt.legend()

    # Merging process subplot
    plt.subplot(1, 2, 2)
    if temp_indices:
        plt.bar(temp_indices, [add_sorted_data[i] for i in temp_indices], color='green')
        for i in temp_indices:
            plt.text(i, add_sorted_data[i] + 0.1, str(add_sorted_data[i]), ha='center', va='bottom')  # Display numbers slightly above the bars
    plt.xlabel('Index')
    plt.title('Sorted Data from Temp List')
    plt.suptitle('Merge Sort Visualization')
    plt.pause(2)


def merge(number_list, low, mid, high):
    count=0
    temp = []
    left = low
    right = mid + 1
    temp_indices = []  # Indices of elements being merged
    visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)
    while left <= mid and right <= high:
        if number_list[left] <= number_list[right]:
            temp.append(number_list[left])
            temp_indices.append(count)
            left += 1
            count+=1
            visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)
        else:
            temp.append(number_list[right])
            temp_indices.append(count)
            right += 1
            count+=1
            visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)
    while left <= mid:
        temp.append(number_list[left])
        temp_indices.append(count)
        left += 1
        count+=1
        visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)
        
    while right <= high:
        temp.append(number_list[right])
        temp_indices.append(count)
        right += 1
        count+=1
        visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)

    for i in range(low, high + 1):
        number_list[i] = temp[i - low]

    visualize_sorting(number_list, low, high, merged_indices=range(low, high + 1),temp_indices=temp_indices,add_sorted_data=temp)

def mergeSort(number_list, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(number_list, low, mid)
    mergeSort(number_list, mid + 1, high)
    merge(number_list, low, mid, high)

def initialize_visualization():
    number_list = eval(input("Enter numbers to sort: "))
    length = len(number_list)
    print("Before Sorting Array:")
    for i in range(length):
        print(number_list[i], end=" ")
    print("\n")
    plt.ion()
    mergeSort(number_list, 0, length - 1)
    plt.ioff()
    print("The sorted numbers are: ", number_list)
