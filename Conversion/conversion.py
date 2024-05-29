from html.parser import HTMLParser
from opencc import OpenCC
import re
from bs4 import BeautifulSoup, NavigableString

parser = HTMLParser()
converter = OpenCC('s2tw')

class Chineseconversion(object):
    
    def check_symmetrical(self, html_content):

        tags = re.findall(r'<(/?[\w]+)[^>]*>', html_content)

        stack = []

        for tag in tags:
            if tag in ['br', 'img', 'hr', 'input', 'meta', 'link']:
                continue

            if not tag.startswith('/'):
                stack.append(tag)
            else:
                if not stack:
                    return False
                start_tag = stack.pop()

                if start_tag != tag[1:]:
                    return False

        return len(stack) == 0
    
    def translate(self, text): 
        traditional_text = converter.convert(text)

        return traditional_text

    def prase(self, content):

        html_pattern = re.compile(r'<\s*(\w+)(\s+[^>]*)?>|<\/\s*(\w+)\s*>')
        is_html = bool(html_pattern.search(content))
        if is_html:
            if self.check_symmetrical(content):
                soup = BeautifulSoup(content, 'html.parser')

                text_nodes = []
                img_nodes = []
                for element in soup.descendants:
                    if isinstance(element, NavigableString) and element.strip():
                        text_nodes.append(element)
                    elif element.name == 'img' and 'alt' in element.attrs:
                        img_nodes.append(element)

                for node in text_nodes:
                    translated_text = self.translate(node)
                    node.replace_with(translated_text)


                for img in img_nodes:
                    alt_text = img['alt']
                    if alt_text:
                        translated_alt_text = self.translate(alt_text)
                        img['alt'] = translated_alt_text

                result_content = soup

            else:
                print ("標籤不對稱")

        else:
            print('請匯入HTML格式')
        result_content = self.translate(content)


        return result_content
