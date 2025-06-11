
class Instrument:
    def make_sound(self):
        pass

class Piano(Instrument):
    def make_sound(self):
        print("钢琴在发声")

class Drum(Instrument):
    def make_sound(self):
        print("drum 在发声")

class Guitar(Instrument):
    def make_sound(self):
        print("guita is making sound")

class Bird:
    def make_sound(self):
        print("bird is making sound")


#这里很有意思，这里tool也不检查是否传进来的对象一定有make_sound方法，只要执行的时候有，就行。 也不检查类型。不像java. 多态，鸭子类型。。。！！！！！！！！！
def play(tool):
    tool.make_sound()

if __name__ == '__main__':
    play(Drum())
    play(Guitar())
    play(Piano())
    play(Bird()) #bird 对象没有继承 ，也okay