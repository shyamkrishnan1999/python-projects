
import textwrap
#program to wrap a given string into paragraph of fixed word length

#c/c++ style
def wrap(string, max_width):
    print("This is output using c/c++ style of programming")
    count=0
    for ch in string:
        print(ch,end="")
        count+=1
        if count==4:
            print("")
            count=0


#pythonic style
def wrap2(string, max_width):
    print("This is the output using python style of programming")
    wrapper = textwrap.TextWrapper(max_width)
    text = wrapper.fill(string)
    return text


if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)
    print("")
    result=wrap2(string,max_width)
    print(result)