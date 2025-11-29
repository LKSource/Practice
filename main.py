import practices
from rich import print
from rich.console import Console
from rich.table import Table
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #myPython1.print_mypython1("Namashivaya Narayana Swami Narayan ")
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    console = Console()
    table = Table(title="Results Table")
    table.add_column("Sl. no.", justify="center", style="cyan")
    table.add_column("Function", justify="left", style="magenta")
    table.add_column("Result", style="green")    
    print_hi('Namashivaya Narayana Swami Narayan ')
    table.add_row("1", "fibonacci", str(practices.fibonacci(10)))
    table.add_row("2", "is_palindrome", str(practices.is_palindrome("malayalam")))
    ls = ["aabccddd","aaabccddd","aaabccddd","baab","aa","ab","aabbccddeeff","abcdeffedcba","aaabccba"]
    #print(set(s))
    for index, s in enumerate(ls, start=3):
        result = practices.superReducedString(s)
        table.add_row(str(index), "superReducedString", str(result))
    i = index + 1
    table.add_row(str(i), "camelcase", str(practices.camelcase('saveChangesInTheEditor')))
    i = i + 1
    table.add_row(str(i), "minimumNumber", str(practices.minimumNumber(5,'2bbbb')))
    i = i + 1
    table.add_row(str(i), "isGreekAlphabet", str(practices.isGreekAlphabet('ALPHA')))
    i = i + 1
    table.add_row(str(i), "alternate", str(practices.alternate('asdcbsdcagfsdbgdfanfghbsfdab')))
    i = i + 1
    table.add_row(str(i), "hackerrankInString", str(practices.hackerrankInString('hacakaeararanaka')), str(practices.hackerrankInString('hhhackkerbanker')))
    i = i + 1
    table.add_row(str(i), "caesarCipher", "middle-Outz", str(practices.caesarCipher("middle-Outz", 2)))
    i = i + 1
    table.add_row(str(i), "marsExploration", "SOSSPSSQSSOR", str(practices.marsExploration("SOSSPSSQSSOR")))
    i = i + 1
    table.add_row(str(i), "quickSort", "[4, 5, 3, 7, 2]", str(practices.quickSort([4, 5, 3, 7, 2])))    
    console.print(table)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/