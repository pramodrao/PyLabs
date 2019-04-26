class Sorter:

    @staticmethod
    def run_selection_sort(unsorted_list):
        list_len = len(unsorted_list)
        if list_len < 2:
            return
        for i in range(list_len):
            for j in range(i+1, list_len):
                if unsorted_list[i] > unsorted_list[j]:
                    unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]

    @staticmethod
    def run_merge_sort(unsorted_list):
        list_len = len(unsorted_list)
        if list_len < 2:
            return unsorted_list
        else:
            mid = list_len//2
            left_list = Sorter.run_merge_sort(unsorted_list[:mid])
            right_list = Sorter.run_merge_sort(unsorted_list[mid:])
            return Sorter.__merge_lists(left_list, right_list)

    @staticmethod
    def __merge_lists(left_list, right_list):
        left_len = len(left_list)
        right_len = len(right_list)
        left_index = 0
        right_index = 0
        merged_list = []
        while left_index < left_len and right_index < right_len:
            if left_list[left_index] < right_list[right_index]:
                merged_list.append(left_list[left_index])
                left_index += 1
            else:
                merged_list.append(right_list[right_index])
                right_index += 1

        while left_index < left_len:
            merged_list.append(left_list[left_index])
            left_index += 1

        while right_index < right_len:
            merged_list.append(right_list[right_index])
            right_index += 1

        return merged_list
