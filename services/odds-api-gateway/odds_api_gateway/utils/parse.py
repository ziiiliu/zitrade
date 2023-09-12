
def parse_all_sports():
    pass

arr = [1,2,3,4]

def all_sub(arr):
    def rec(arr, ans):
        print(arr, ans)
        # cur_results = []
        if len(arr) == 1:
            ans = [arr] + ans
            print(ans)
            return [arr]
        prev_results = rec(arr[1:], ans)
        ans.append([arr[0]])
        print(ans)
        for prev in prev_results:
            ans.append([arr[0]] + prev)
        return ans
    return rec(arr, [])

print(all_sub(arr))