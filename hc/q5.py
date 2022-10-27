class Coin:
    """Do not fix this function"""
    def toss():
        import random
        return random.randint(0, 1)


class Dice:
    @staticmethod
    def toss():
        # Don't use python random library,
        res =0
        if Coin.toss():
            res +=3
        dice_list = [1 for i in range(3)]
        before_list = dice_list.copy()
        while sum(dice_list) != 1:
            for i in range(3):
                if dice_list[i] == 1: dice_list[i] = Coin.toss()
            if sum(dice_list) == 0:
                dice_list = before_list.copy()
            else:
                before_list = dice_list.copy()

        # Only use Coin.toss()
        return dice_list.index(1) + 1 + res

Dice.toss()

print(Dice.toss())
