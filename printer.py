class Printer():
    def __init__(self, num1, num2, priority):
        print("입력")
        self.num1 = num1
        self.num2 = num2
        self.priority = priority
        print("작업 수 / 작업 번호  : {0}/{1}".format(self.num1,self.num2))
        print("작업 우선순위 :{0}".format(self.priority))
    def printing(self):
        file_1 = list(range(0,self.num1))
        time = 0
        while True: 
            if self.priority[0] == max(self.priority):  
                time += 1 
                if file_1[0] == self.num2:
                    print("출력")
                    print(time,"분") 
                    break 
                else:              
                    file_1.pop(0) 
                    self.priority.pop(0)
            else: 
                file_1.append(file_1.pop(0)) 
                self.priority.append(self.priority.pop(0))


num1 = int(input("작업 수를 입력해주세요 :"))
num2 = int(input("작업 번호를 입력해주세요 : "))
prior1 = list(map(int,input("작업 우선순위를 입력해주세요 :").split()))
print1 = Printer(num1,num2,prior1)
print1.printing()
print(print1)
