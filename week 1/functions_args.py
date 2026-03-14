def student_info(*args,**kwargs):
    """Understanding *args and **kwargs, how they are implemented"""
    print(args)
    print(kwargs)

student_info('History','Geography','Economics',name='Rohit',group='Social Welfare')


def enter(greetings,name='You'):
    """Using Format to display the content in he arguments"""

    return "{}, {}".format(greetings,name)
print(enter('Hi!',name = 'Raj'))
