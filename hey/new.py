#Happy Friday
# N = int(input())
# lst = [input() for i in range(N)]
# new = []

# for i in lst:
#     i = i.split()
#     if i[0] == 'insert':
#         new.insert(int(i[1]),int(i[2]))
#     if i[0] == 'print':
#         print(new)
#     if i[0] == 'remove':
#         new.remove(int(i[1]))
#     if i[0] == 'append':
#         new.append(int(i[1]))
#     if i[0] == 'sort':
#         new.sort()
#     if i[0] == 'pop':
#         new.pop()
#     if i[0] == 'reverse':
#         new.reverse()


# print(new)
# t = tuple([1,2])
# # print(hash(t))
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = tuple(map(int, input().split()))
#     print(hash(integer_list))

# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
  
  
  
  
  
  
  
  
  
  
# html = ""       
# for i in range(int(input())):
#     html += input().rstrip()
#     html += '\n'
    
# parser = MyHTMLParser()
# parser.feed(html)
# parser.close()

# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(f'解析中のタグは"{tag}"です')

#     def handle_endtag(self, tag):
#         print(f'解析したタグは"{tag}"です')

#     def handle_data(self, data):
#         print(f'解析中のテキストは"{data}"です')

# parser = MyHTMLParser()
# parser.feed('<html><head><title>本日は晴天なり</title></head></html>')

# #クラスの定義を学ぶ

# class Person():
#     def __init__(self, name, age):

#         self.name = name
#         self.age = age
#     def hello(self):
#         print('Hi! My name is {} :)'.format(self.name))

# class Talk(Person):
#     def __init__(self, name, age): #init呼び込みの時点でPersonのが利用されてる
#         super().__init__(name, age)
#     def talktalk(self):
#         print("{}:Why don't we have a private chat together({})".format(self.name,self.age))

# Bomin = Talk('Bomin',21)
# Bomin.talktalk() #この中でsuper()はPersonからインスタンスから呼び出しを行えるが
# #talktalk()の機能はボミンがTalk()がベースでないと動かない
# Person('Achu','20').hello() #<-そのままPersonにHelloもできる



