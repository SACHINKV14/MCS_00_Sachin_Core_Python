#Create html from string
class Html:
    def create_html(self,title,body):
        var = f'''
        <html>
            <head>{title}</head>
            <body>{body}</body>
        </html>
        '''
        print(var)

t=input("enter title:")
b=input("enter body:")
s1=Html()
s1.create_html(t,b)

