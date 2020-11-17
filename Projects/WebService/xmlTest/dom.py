import xml.dom.minidom as dom

# 获取属性值 ele.getAttribute('')
# 获取节点值 ele.childNodes[0].data
# 获取子节点 ele.getElementsByTagName('')

doc = dom.parse('movies.xml')

# 根节点
root = doc.documentElement
if root.hasAttribute('shelf'):
    print('the root element is '+root.getAttribute('shelf'))

movies = root.getElementsByTagName('movie')
for movie in movies:
    if movie.hasAttribute('title'):
        print('Title is '+movie.getAttribute('title'))

    the_type = movie.getElementsByTagName('type')[0]
    print('Type is '+the_type.childNodes[0].data)

    the_format = movie.getElementsByTagName('format')[0]
    print('Format is s'+the_format.childNodes[0].data)

