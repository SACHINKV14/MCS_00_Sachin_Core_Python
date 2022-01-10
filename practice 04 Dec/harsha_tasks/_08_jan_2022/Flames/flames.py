class Flames:
    def find_flames(self,name1,name2):
        n1=name1
        n2=name2
        n3=(n1.replace(" ","")+n2.replace(" ","")).lower()
        for i1 in n3:
            # print(i1)
            if (i1 in n1) and (i1 in n2):
                n1=n1.replace(i1,"",1)
                n2=n2.replace(i1,"",1)
        print("---------------------------")
        count=len(n1+n2)
        # flames=[1,2,3,4,5,6]
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        # keep looping until only one item
        # is not remaining in the result list
        while len(result) > 1:
            # store that index value from
            # where we have to perform slicing.
            split_index = (count % len(result) - 1)
            # this steps is done for performing
            # anticlock-wise circular fashion counting.
            if split_index >= 0:

                # list slicing
                right = result[split_index + 1:]
                left = result[: split_index]
                print(right,'\t',left)
                # list concatenation
                result = right + left

            else:
                result = result[: len(result) - 1]
        # print final result
        return result[0]

