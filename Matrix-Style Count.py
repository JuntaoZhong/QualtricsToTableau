import pandas as pd
import sys
import csv

def counter(Q_list, source, Scale_list):
    choice = len(Scale_list)
    countMatrix = []
    for i in range(len(Q_list)):
        print(Q_list[i])
        Q_count_array = n_choice_counter(choice, i*choice, source)
        countMatrix.append(Q_count_array)
    outMatrix = pd.DataFrame(countMatrix, index = Q_list, columns =Scale_list)
    return outMatrix

def n_choice_counter(choice, startColumn, source):
    print(startColumn)
    countArray = [0]*choice
    numRows = len(source)
    for i in range(choice):
        count = 0
        for j in range(1, numRows):
            if source[j][startColumn + i]:
                count = count + 1
            if startColumn==40: 
                print("this is i: " + i + ", this is j: " + j)
        countArray[i] = count
        print(countArray)
    return countArray

def cal_sum(pdMatrix, column_list):
    pdMatrix["sum"] = pdMatrix[column_list].sum(axis=1)
    return pdMatrix

def main():
    QList_48_66 = ["Joe Biden opposes efforts to repeal the Affordable Care Act (sometimes known as Obamacare)"
    ,"Donald Trump opposes efforts to repeal the Affordable Care Act (sometimes known as Obamacare)"
    ,"Jason Lewis opposes efforts to repeal the Affordable Care Act (sometimes known as Obamacare)"
    ,"Tina Smith opposes efforts to repeal the Affordable Care Act (sometimes known as Obamacare)"
    ,"Joe Biden supports supports legislation to achieve net-zero greenhouse gas emissions by no later that 2050"
    ,"Donald Trump supports supports legislation to achieve net-zero greenhouse gas emissions by no later that 2050"
    ,"Jason Lewis supports supports legislation to achieve net-zero greenhouse gas emissions by no later that 2050"
    ,"Tina Smith supports supports legislation to achieve net-zero greenhouse gas emissions by no later that 2050"]
    SList_48_66 = ["Completely INACCURATE", "Mostly INACCURATE", "Mostly ACCURATE", "Completely ACCURATE", "I do not know"]
    
    input_48_66 = []
    with open('Matrix Q48-66.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            input_48_66.append(row)
    countMatrix = counter(QList_48_66, input_48_66, SList_48_66)
    withSum = cal_sum(countMatrix, SList_48_66)
    print(withSum)
    countMatrix.to_csv('Q48_66_count.csv', header=True)

    QList_62_70 = ["Discrimination against women is no longer a problem in the United States",
    "Women often miss out on good jobs due to sexual discrimination",
    "It is rare to see women treated in a sexist manner on television",
    "On average, people in our society treat husbands and wives equally",
    "Society has reached the point where women and men have equal opportunities for achievement",
    "It is easy to understand the anger of women’s groups in America",
    "It is easy to understand why women’s groups are still concerned about societal limitations of women’s opportunities",
    "Over the past few years, the government and the news media have been showing more concern about the treatment of women than is warranted by women’s actual experiences"]
    SList_62_70 = ["Strongly disagree","Disagree","Neither agree nor disagree","Agree","Strongly agree"]
    input_62_70 = []
    with open('Q_62_70.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            input_62_70.append(row)
    countMatrix = counter(QList_62_70, input_62_70, SList_62_70)
    withSum = cal_sum(countMatrix, SList_62_70)
    print(withSum)
    countMatrix.to_csv('Q62_70_count.csv', header=True)

    SList_17 = ["Very liberal","Somewhat liberal","A little liberal","Neither liberal nor conservative","A little conservative","Somewhat conservative","Very conservative"]
    input_17 = []
    QList_17 = ["Yourself","Democrats","Republicans","Joe Biden","Kamala Harris","Jason Lewis","Mike Pence","Tina Smith","Donald Trump","Barack Obama"]
    with open('Q17.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            input_17.append(row)
    countMatrix = counter(QList_17, input_17, SList_17)
    withSum = cal_sum(countMatrix, SList_17)
    print(withSum)
    countMatrix.to_csv('Q17_count.csv', header=True)

if __name__ == "__main__":
    main()