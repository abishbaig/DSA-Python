import array as arr

# T.C = O(n) - S.C = O(1)
def linearSearch(arr: arr.array, key: int) -> int:
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    else:
        return -1


def main():
    arr1 : arr.array = arr.array("i",[1,2,3,4,5])
    print(linearSearch(arr1,9)) 

if __name__=="__main__":
    main()