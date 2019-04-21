import xml.sax as sax


class MovieHandler(sax.ContentHandler):

    def __init__(self):
        self.CurrentData = ''
        self.type = ''
        self.format = ''
        self.year = ''
        self.rating = ''
        self.starts = ''
        self.description = ''

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag

        if tag == 'movie':
            print('***movie')
            title = attributes['title']
            print('Title:'+title)

    def endElement(self, tag):
        if self.CurrentData == 'type':
            print('Type:'+self.type)

    def characters(self, content):
        if self.type == 'type':
            self.type = content


if __name__ == '__main__':
    # 创建一个XMLReader
    parser = sax.make_parser()
    # 关闭命名空间
    parser.setFeature(sax.handler.feature_namespaces, 0)

    # 重写ContextHandler
    handler = MovieHandler()
    parser.setContentHandler(handler)

    parser.parse('movies.xml')
