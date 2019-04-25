class BinarySearch:

    def __init__(self, lst):
        self.lst = lst

    def add_to_list(self, element):
        self.lst.append(element)

    def search_normal(self, element):
        lst_len = len(self.lst)
        if lst_len == 0:
            raise ValueError
        for i in range(lst_len):
            if self.lst[i] == element:
                print("Found in index", i)
                return True
        print("Element Not Found in list", element)
        return False

    def search_binary(self, element):

        def search_binary_helper(lst, e, top_index, bottom_index):

            print(str(top_index), '\t', str(bottom_index))
            if top_index == bottom_index:
                if lst[top_index] == e:
                    print("Found in index", top_index, '\t', str(lst[top_index]))
                    return True
                else:
                    return False

            mid_index = (top_index + bottom_index)//2
            print('Mid Index:', str(mid_index), '\t', str(lst[mid_index]))

            if lst[mid_index] == e:
                print("Found in index", mid_index)
                return True
            elif lst[mid_index] > e:
                if top_index >= mid_index:
                    return False
                else:
                    search_binary_helper(lst, e, top_index, mid_index)
            else:
                search_binary_helper(lst, e, mid_index + 1, bottom_index)

        self.lst.sort()
        print('Sorted List')
        for i in range(len(self.lst)):
            print(self.lst[i])
        return search_binary_helper(self.lst, element, 0, len(self.lst)-1)

