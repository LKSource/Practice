import practices

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #myPython1.print_mypython1("Namashivaya Narayana Swami Narayan ")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Namashivaya Narayana Swami Narayan ')
    print(practices.fibonacci(10))
    print(practices.is_palindrome("malayalam"))
    ls = ["aabccddd","aaabccddd","aaabccddd","baab","aa","ab","aabbccddeeff","abcdeffedcba","aaabccba"]
    #print(set(s))
    for s in ls:
        result = practices.superReducedString(s)
        print(result)    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/