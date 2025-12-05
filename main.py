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
    i = i + 1
    table.add_row(str(i), "pangrams", "We promptly judged antique ivory buckles for the next prize", str(practices.pangrams("We promptly judged antique ivory buckles for the next prize")))    
    i = i + 1
    table.add_row(str(i), "weightedUniformStrings", "abbcccddddab [1, 7, 5, 4, 15, 4, 15,1]", str(practices.weightedUniformStrings('abbcccddddab', [1, 7, 5, 4, 15, 4, 15,1])))    
    i = i + 1
    table.add_row(str(i), "separateNumbers", "['99910001001','7891011','9899100','999100010001']", str(practices.separateNumbers('99910001001')))    
    i = i + 1
    table.add_row(str(i), "funnyString", "['acxz','bcxz']", str(practices.funnyString('acxz')))    
    i = i + 1
    table.add_row(str(i), "countingSort", "[1,1,3,2,1]", str(practices.countingSort([1,1,3,2,1])))
    i = i + 1
    table.add_row(str(i), "gemstones", "['abcdde', 'baccd', 'eeabgc']", str(practices.gemstones(['abcdde', 'baccd', 'eeabgc'])))
    i = i + 1
    table.add_row(str(i), "alternatingCharacters", "['AAAA',,'AABBAABB','ABABABAA','ABBABBAA']", str(practices.alternatingCharacters('ABABABAA')))
    i = i + 1
    table.add_row(str(i), "beautifulBinaryString", "0100101010", str(practices.beautifulBinaryString('0100101010')))
    i = i + 1
    table.add_row(str(i), "closestNumbers", "[5,4,3,2]", str(practices.closestNumbers([5,4,3,2])))
    i = i + 1
    table.add_row(str(i), "findMedian", "[0,1,2,4,6,5,3]", str(practices.findMedian([0,1,2,4,6,5,3])))
    i = i + 1
    table.add_row(str(i), "theLoveLetterMystery", "abcd", str(practices.theLoveLetterMystery("abcd")))
    i = i + 1
    table.add_row(str(i), "palindromeIndex", "aaab", str(practices.palindromeIndex("aaab")))
    i = i + 1
    table.add_row(str(i), "anagram", "aaabbb", str(practices.anagram("aaabbb")))
    i = i + 1
    table.add_row(str(i), "makingAnagrams", "'abc','amnop'", str(practices.makingAnagrams('abc','amnop')))
    i = i + 1
    table.add_row(str(i), "gameOfThrones", "cdcdcdcdeeeef", str(practices.gameOfThrones('cdcdcdcdeeeef')))

    console.print(table)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/