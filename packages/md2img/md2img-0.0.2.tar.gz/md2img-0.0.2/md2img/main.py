import re
from PIL import Image, ImageFont, ImageDraw

fontA = r"fonts/sarasa-mono-sc-regular.ttf"     # 普通字体
fontB = r"fonts/sarasa-mono-sc-bold.ttf"        # 加粗字体
fontC = r"fonts/sarasa-mono-sc-italic.ttf"      # 普通斜体
fontD = r"fonts/sarasa-mono-sc-bolditalic.ttf"  # 加粗斜体

# 每一行文本作为一个对象
class Text:
    def __init__(self, text, size, space, width, \
                 height, bg, fg):
        self.text = text.strip()
        self.font = fontA                   # 默认普通字体
        self.size = size                    # 字体尺寸
        self.height = size                  # 本行行高
        self.bg = bg                        # 背景颜色
        self.fg = fg                        # 字体颜色
        self.space = space                  # 与下一行的行间距
        self.width = width                  # 背景宽度
        self.height = height                # 背景高度
        self.length = 0                     # 一行种的字符个数
        self.multi = None                   # 一行中是否存在多个对象

    def parser(self):
        # 判断文本是否为标题
        title = re.match(r"(#+) ", self.text)
        if title:
            level = len(title.group(1))
            self.font = fontB               # 使用加粗字体
            self.size *= (4 - level)        # 根据标题级别调整字体尺寸
            self.text = self.text[level:].strip()

        # 判断是否为无序列表
        ul = re.match(r"[*+-] ", self.text)
        if ul:
            self.text = "• " + self.text[1:].strip()
            self.length -= 1

        # 判断是否粗斜体
        italic = re.search(r"\*\*\*(.+)\*\*\*", self.text)
        if italic:
            pos = italic.span()
            self.multi = []
            # 如果不是整行斜体，就需要存放为多个对象
            if pos[0] != 0 or pos[1] != len(self.text):
                t1 = Text(self.text[:pos[0]], self.size, self.space, self.width, \
                     self.height, self.bg, self.fg)
                t1.font = fontA
                self.multi.append(t1)
                t2 = Text(self.text[pos[0]+3:pos[1]-3], self.size, self.space, \
                          self.width, self.height, self.bg, self.fg)
                t2.font = fontD
                self.multi.append(t2)
                t3 = Text(self.text[pos[1]:], self.size, self.space, self.width, \
                          self.height, self.bg, self.fg)
                t3.font = fontA
                self.multi.append(t3)
                self.length -= 6
            else:
                self.font = fontD
                self.text = self.text[:pos[0]] + self.text[pos[0]+3:pos[1]-3] + \
                            self.text[pos[1]:]
        else:
            # 判断是否粗体
            bold = re.search(r"\*\*(.+)\*\*", self.text)
            if bold:
                pos = bold.span()
                self.multi = []
                # 如果不是整行加粗，就需要存放为多个对象
                if pos[0] != 0 or pos[1] != len(self.text):
                    t1 = Text(self.text[:pos[0]], self.size, self.space, self.width, \
                         self.height, self.bg, self.fg)
                    t1.font = fontA
                    self.multi.append(t1)
                    t2 = Text(self.text[pos[0]+2:pos[1]-2], self.size, self.space, \
                              self.width, self.height, self.bg, self.fg)
                    t2.font = fontB
                    self.multi.append(t2)
                    t3 = Text(self.text[pos[1]:], self.size, self.space, self.width, \
                              self.height, self.bg, self.fg)
                    t3.font = fontA
                    self.multi.append(t3)
                    self.length -= 4
                else:
                    self.font = fontB
                    self.text = self.text[:pos[0]] + self.text[pos[0]+2:pos[1]-2] + \
                                self.text[pos[1]:]
            else:
                # 判断是否斜体
                italic = re.search(r"\*(.+)\*", self.text)
                if italic:
                    pos = italic.span()
                    self.multi = []
                    # 如果不是整行斜体，就需要存放为多个对象
                    if pos[0] != 0 or pos[1] != len(self.text):
                        t1 = Text(self.text[:pos[0]], self.size, self.space, self.width, \
                             self.height, self.bg, self.fg)
                        t1.font = fontA
                        self.multi.append(t1)
                        t2 = Text(self.text[pos[0]+1:pos[1]-1], self.size, self.space, \
                                  self.width, self.height, self.bg, self.fg)
                        t2.font = fontC
                        self.multi.append(t2)
                        t3 = Text(self.text[pos[1]:], self.size, self.space, self.width, \
                                  self.height, self.bg, self.fg)
                        t3.font = fontA
                        self.multi.append(t3)
                        self.length -= 2
                    else:
                        self.font = fontC
                        self.text = self.text[:pos[0]] + self.text[pos[0]+1:pos[1]-1] + \
                                    self.text[pos[1]:]
            
    def draw(self, im, dr, top):
        font = ImageFont.truetype(font=self.font, size=self.size)
        self.length += len(self.text)
        # 末尾标点符号不计长度
        if self.length > 0 and self.text[-1] in "，,.。!！?？~……^@_—；;":
            self.length -= 1
        left = (self.width - self.length * self.size) // 2
        if self.multi:
            for each in self.multi:
                font = ImageFont.truetype(font=each.font, size=each.size)
                dr.text((left, top), each.text, font=font, fill=each.fg)
                left += font.getlength(each.text)
        else:
            dr.text((left, top), self.text, font=font, fill=self.fg)
        

def main():
    with open("text.txt", encoding="utf-8") as f:
        texts = f.readlines()

    logo = "logo.png"           # LOGO
    target = "output.png"       # 输出图片
    size = 30                   # 字体尺寸
    width = 600                 # 图片宽度
    height = 800                # 图片高度
    bg = (60, 195, 188)         # 背景颜色
    fg = (255, 255, 255)        # 字体颜色
    space = 10                  # 行间距

    im = Image.new("RGBA", (width, height), bg)
    dr = ImageDraw.Draw(im)

    top = (height - len(texts) * (size + space)) // 2 + 50

    # 绘制LOGO
    logo = Image.open(logo)
    logo_width, logo_height = logo.size
    im.alpha_composite(logo, ((width - logo_width) // 2, top-2*logo_height))

    # 绘制文本
    for each in texts:
        text = Text(each, size, space, width, height, bg, fg)
        text.parser()
        text.draw(im, dr, top)
        top += (text.size + text.space)

    im.save(target)
    

if __name__ == "__main__":
    main()
