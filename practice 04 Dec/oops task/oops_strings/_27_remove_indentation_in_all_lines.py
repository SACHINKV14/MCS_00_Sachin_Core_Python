class String:
    def remove_indentation(self,var):
        print(f'original string:{var}')
        var = var.split("\n")
        # print(var)
        for i in var:
            i = i.lstrip()
            print(i)

var="""    sachin
         is very
  good boy
"""
s1=String()
s1.remove_indentation(var)
