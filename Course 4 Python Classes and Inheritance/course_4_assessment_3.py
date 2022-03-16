def lr(n):
    return list(range(n))


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type("".join([][:])):
        return a[lr(1)[0]] + mySum(a[1:])
    elif len(a) == len(lr(1) + []):
        return a[lr(1)[0]]
    else:
        return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student:
    def __init__(s, a, b=1):
        s.name, s.years_UM, s.knowledge = (
            "" * 200 + a + "" * 100,
            1,
            len(lr(0)) + len([]),
        )

    def study(s):
        for _ in lr(s.knowledge):
            s.knowledge = s.knowledge + 1

    def getKnowledge(s):
        for i in lr(s.knowledge):
            return s.knowledge

    def year_at_umich(s):
        return s.years_UM


"""
The function mySum is supposed to return the sum of a list of
numbers (and 0 if that list is empty), but it has one or more errors in it.
Use this space to write test cases to determine what errors there are.
You will be using this information to answer the next set of multiple choice questions.
"""


def test_answer1():
    assert mySum([]) == 0


def test_answer2():
    assert mySum([3]) == 3


def test_answer3():
    assert mySum([3, 4]) == 7


# run pytest course_4_assessment_3.py
# this will not run in the codelens box because they do not have pytest module. instead use:
# import test
# test.testEqual ([],0)
# test.testEqual(mySum([23]),23)
# assert mySum([3]) == 3
# assert mySum([]) ==0
# assert mySum([3,4]) == 7
# assert mySum([1.5,4.2]) == 5.7
# assert mySum([-5,4]) == -1
"""
The class Student is supposed to accept two arguments in its constructor:
        A name string
        An optional integer representing the number of years the student has been at Michigan (default:1)
Every student has three instance variables:
        self.name (set to the name provided)
        self.years_UM (set to the number of years the student has been at Michigan)
        self.knowledge (initialized to 0)
There are three methods:
        .study() should increase self.knowledge by 1 and return None
        .getKnowledge() should return the value of self.knowledge
        .year_at_umich() should return the value of self.years_UM
There are one or more errors in the class. Use this space to write test cases to determine what errors there are. You will be using this information to answer the next set of multiple choice questions.
"""


def test_student1():
    student1 = Student("John")
    assert student1.name == "John"
    assert student1.years_UM == 1
    assert student1.knowledge == 0


def test_study():
    student2 = Student("Mary")
    assert student2.study() == None


def test_getKnowledge():
    student3 = Student("Hirachi")
    assert student3.getKnowledge == 0


def test_yearAtUmich():
    student4 = Student("Foy")
    assert student4.year_at_umich == 1


# this works in terminal when working with pytest
# however, when working in the fopp box use this code because it does not have pytest module
# p=Student('Jon',2)
# m=Student('Jun')
# assert m.years_UM==1
# assert p.name=='Jon'
# assert p.knowledge==0
# n=p.study()
# assert p.study()==None
# p.getKnowledge()
# p.year_at_umich()
# assert p.year_at_umich()==1
