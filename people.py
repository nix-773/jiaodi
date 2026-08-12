from abc import ABC, abstractmethod
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
def main():
    stu = Student("郑子鸣","河科院2#121室委书记")
    stu.hello()

if __name__ == "__main__":
    main()