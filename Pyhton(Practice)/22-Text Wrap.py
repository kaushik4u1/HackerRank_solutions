#To use these modules, we need to import the textwrap module in our code.
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width)) #textwrap module is used to format and wrap plain texts. There are some options to format the texts by adjusting the line breaks in the input paragraph.




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
