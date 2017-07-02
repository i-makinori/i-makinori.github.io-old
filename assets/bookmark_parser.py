from html.parser import HTMLParser
from functools import reduce

"""
twig :: [(twig | page)] , title
page :: (title, url)
"""

databse_file = "program_bookmarks.html"
output_file = "bookmarks.md"



def read_file (file_name):
    f = open(file_name)
    content = f.read()
    f.close()
    return content

def write_file(file_name, str):
    f = open(file_name, 'w')
    f.write(str)
    f.close()


    

class TreeToMarkdownParser(HTMLParser):


    def __init__(self):
        HTMLParser.__init__(self)

        self.pages_markdown_list = [""]

        self.tag = False
        self.twig_level =0
        self.attrs = []
    

    def handle_starttag(self, tag, attrs):
        self.attrs = dict(attrs)
        self.tag = tag

        if tag == "dl":
            self.twig_level += 1

    def handle_endtag(self, tag):
        if tag=="dl":
            self.twig_level -= 1
        self.tag = False

    def handle_data (self, data):

        if self.tag=="h3" :
            str = self.twig_markdown_text(self.twig_level, data, self.attrs)
            self.pages_markdown_list += [str]

        if self.tag=="a": 
            str = self.page_markdown_text(self.twig_level, data, self.attrs)
            self.pages_markdown_list += [str]

    def twig_markdown_text(self, twig_level, data, attrs):
        indents = "".join([' ' for i in range(2*twig_level)])
        str = "".join([indents, " - ", data, "  \n"])
        return str

    def page_markdown_text(self, twig_level, data, attrs):

        indents = "".join([' ' for i in range(2*twig_level)])

        url = ""
        if 'href' in attrs : 
            url = attrs['href']

        link_text = "[{data}]({url}) ".format(data=data, url=url)

        str = "".join([indents, " - ", link_text, "  \n"])
        return str

    def pages_markdown_list_to_text(self):        
        return  "".join(self.pages_markdown_list)
        


if __name__ == "__main__":

    text_content = read_file(databse_file)
    

    parser = TreeToMarkdownParser()
    parser.feed(text_content)

    output_str = reduce (lambda acc, item: acc+item, parser.pages_markdown_list, "")
    print(output_str)

    write_file(output_file, output_str)


