
from random import randint
class Magic:
    def fortune(self):
        str1="""It is certain.It is decidedly so.Without a doubt.Yes definitely.You may rely on it.
        As I see it, yes.Most likely.Outlook good.Yes.Signs point to yes.
        Reply hazy, try again.Ask again later.Better not tell you now.Cannot predict now.Concentrate and ask again.
        Don't count on it.My reply is no.My sources say no.Outlook not so good.Very doubtful
        """
        str1=str1.replace('\n',"")
        str1=str1.split(".")
        lst1=list(str1)
        lst2=[x for x in range(1,21)]

        dict1={x1:y1 for (x1,y1) in zip(lst2,lst1)}
        # print(dict1)

        p1=randint(1,20)

        return dict1[p1]