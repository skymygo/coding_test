class MovingTotal:

    def __init__(self):
        self.array = list()
        self.sum = dict()
        self.len = 0

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        # self.array.extend(numbers)
        # self.sum = [sum(self.array[num:num + 3]) for num in range(len(self.array) - 2)]
        self.array.extend(numbers)
        new_dict = {sum(self.array[num:num+3]):0 for num in range(self.len, len(self.array)-2)}
        self.sum.update(new_dict)
        self.len = len(self.array)-2

        pass

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return total in self.sum


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))

    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))