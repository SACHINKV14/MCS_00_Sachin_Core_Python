'''
Flavors of Python:
    1.CPython:
    It is the standard flavor of Python. It can be used to work with C lanugage Applications
    2. Jython or JPython:
    It is for Java Applications. It can run on JVM
    3. IronPython:
    It is for C#.Net platform
    4.PyPy:
    The main advantage of PyPy is performance will be improved because JIT compiler is
    available inside PVM.
    5.RubyPython
     For Ruby Platforms
    6. AnacondaPython
    It is specially designed for handling large volume of data processing.

Python Versions:
    Python 1.0V introduced in Jan 1994
    Python 2.0V introduced in October 2000
    Python 3.0V introduced in December 2008

Identifiers
    A name in Python program is called identifier.
    It can be class name or function name or module name or variable name.
    Rules to define identifiers in Python:
    1. The only allowed characters in Python are
         alphabet symbols(either lower case or upper case)
         digits(0 to 9)
         underscore symbol(_)
     By mistake if we are using any other symbol like $ then we will get syntax error.
         cash = 10 √
         ca$h =20 
     2. Identifier should not starts with digit
         123total 
         total123 √
     3. Identifiers are case sensitive. Of course Python language is case sensitive language.
         total=10
         TOTAL=999
         print(total) #10
         print(TOTAL) #999

Reserved Words
    In Python some words are reserved to represent some meaning or functionality. Such type
    of words are called Reserved words.
    There are 33 reserved words available in Python.
         True,False,None
         and, or ,not,is
         if,elif,else
         while,for,break,continue,return,in,yield
         try,except,finally,raise,assert
         import,from,as,class,def,pass,global,nonlocal,lambda,del,with

Data Types
    Data Type represent the type of data present inside a variable.
    In Python we are not required to specify the type explicitly. Based on value provided,the
    type will be assigned automatically.Hence Python is Dynamically Typed Language.
    Python contains the following inbuilt data types
    1. int
    2. float
    3.complex
    4.bool
    5.str
    6.bytes
    7.bytearray
    8.range
    9.list
    10.tuple
    11.set
    12.frozenset
    13.dict
    14.None

Operators
    Operator is a symbol that performs certain operations.
    Python provides the following set of operators
        1. Arithmetic Operators
        2. Relational Operators or Comparison Operators
        3. Logical operators
        4. Bitwise oeprators
        5. Assignment operators
        6. Special operators

        1. Arithmetic Operators:
            + ==>Addition
            - ==>Subtraction
            * ==>Multiplication
            / ==>Division operator
            % ===>Modulo operator
            // ==>Floor Division operator
            ** ==>Exponent operator or power operator

        2.Relational Operators:
            >,>=,<,<=

        3.equality operators:
            == , !=

        4.Logical Operators:
            and, or ,not

            We can apply for all types.
            For boolean types behaviour:
            and ==>If both arguments are True then only result is True
            or ====>If atleast one arugemnt is True then result is True
            not ==>complement
            True and False ==>False
            True or False ===>True
            not False ==>True

            For non-boolean types behaviour:
            0 means False
            non-zero means True
            empty string is always treated as False

        5.Bitwise Operators:
            We can apply these operators bitwise.
            These operators are applicable only for int and boolean types.
            By mistake if we are trying to apply for any other type then we will get Error.
            &,|,^,~,<<,>>

            bitwise complement operator(~):
            We have to apply complement for total bits.




'''