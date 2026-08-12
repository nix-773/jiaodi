from abc import ABC, abstractmethod
import random
class People(ABC):
    def __init__(self,name : str):
        self.name = name
    @abstractmethod
    def hello(self):
        pass
class Student(People):
    def __init__(self,name: str,post: str):
        super().__init__(name)
        self.post = post
    def hello(self):
        print(f"你好,我是{self.post},{self.name},我的任务呢就是讲事实讲依据")
    def exam(self)->int:
        Lv = random.randint(1, 10)
        if Lv <=3:
            print(f"恭喜{self.name}同学挂科了")
            return random.randint(0,59)
        elif Lv >=9:
            print(f"不愧是{self.name}同学真有实力")
            return random.randint(85,100)
        else:
            print(f"喜报:恭喜{self.name}同学及格了")
            return random.randint(60,85)
def main():
    stu = Student("郑子鸣","河科院2#121室委书记")
    stu.hello()
    print(stu.exam())
if __name__ == "__main__":
    main()