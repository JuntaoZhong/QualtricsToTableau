import pandas as pd
import sys

#colName is the name of the first column response in that question
#follow is how many rows following first column you want to condense. condense 2 column, follow = 1
def simpleCondense(colName, follow):
    colNumber = 0
    colNumber = RawMatrix.columns.get_loc(colName)

    if colNumber == 0:
        print("hey, error! column name not found")

    for i in range(len(RawMatrix)):
        for j in range(follow):
            #print(RawMatrix.iloc[i,colNumber])
            if not(pd.isna(RawMatrix.iloc[i,colNumber+j+1])):
                RawMatrix.iloc[i,colNumber] = RawMatrix.iloc[i,colNumber+j+1]

    RawMatrix.drop(RawMatrix.iloc[:,(colNumber+1):(colNumber+follow+1)], axis = 1, inplace = True)
    
def degreeOfOpinion(colName1, colName2, retArray):
    colNum1 = RawMatrix.columns.get_loc(colName1)
    colNum2 = RawMatrix.columns.get_loc(colName2)
    if colNum1 == 0 or colNum2 == 0:
        print("hey, error! column name not found")

    for i in range(len(RawMatrix)):
        concatString = ""
        if RawMatrix.iloc[i,colNum1] == "Democrat" or RawMatrix.iloc[i,colNum1] == "Republican":
            concatString = RawMatrix.iloc[i,colNum2] + " " + RawMatrix.iloc[i,colNum1]
        elif RawMatrix.iloc[i,colNum1] == "Other political party" or RawMatrix.iloc[i,colNum1] == "Independent":
            concatString = RawMatrix.iloc[i,colNum1] + " and leans toward " + RawMatrix.iloc[i,colNum2]
        retArray.append(concatString)
    return retArray


#file name: phase_1_words_value_trimmed.csv
Qualtricsfile = sys.argv[1]
RawMatrix = pd.read_csv(Qualtricsfile)
#filter all unconsent/under 18 data, delete the row for "not consent"
RawMatrix = RawMatrix[RawMatrix.Q20_1.notnull()]
#keep only answers with "I paid attention and answered each question honestly"
RawMatrix = RawMatrix[RawMatrix.Q72_1.notnull()]

del RawMatrix['Q20_2']
RawMatrix.rename(columns={'Q20_1':'Q_20_Only_Consent'}, inplace = True)

#deal with Q_10
simpleCondense("Q10_1", 1)
RawMatrix.rename(columns={'Q10_1':'Q_10_condense'}, inplace = True)

#deal with Q_11
simpleCondense("Q11_1", 3)
RawMatrix.rename(columns={'Q11_1':'Q_11_condense'}, inplace = True)

#deal with Q_13, 14, 15
simpleCondense("Q13_1", 6)
#, if republican/democrat, how strong they are; if independent, what do they lean towards
RawMatrix.rename(columns={'Q13_1':'Following_Q13'}, inplace = True)
#make a more make-sense column:
concatArray = []
degreeOfOpinion("Q_11_condense", "Following_Q13", concatArray)
RawMatrix.insert(14, "more readable", concatArray, allow_duplicates=False)
#print(concatArray)

#deal with Q_21
simpleCondense("Q21_1", 4)
RawMatrix.rename(columns={'Q21_1':'Q_21_gun_condense'}, inplace = True)

#deal with Q_22, how important is gun issue
simpleCondense("Q22_1", 4)
RawMatrix.rename(columns={'Q22_1':'Q_22_gun_how_important'}, inplace = True)

#deal with Q_24
simpleCondense("Q24_1", 1)
RawMatrix.rename(columns={'Q24_1':'Q_24_immigrants_opinion'}, inplace = True)

#deal with Q_25, how important is immigrant issue
simpleCondense("Q25_1", 4)
RawMatrix.rename(columns={'Q25_1':'Q_25_immigrants_how_important'}, inplace = True)

#Q_26, whether you approve obamacare
simpleCondense("Q26_1", 6)
RawMatrix.rename(columns={'Q26_1':'Q_26_Approve_Obamacare?'}, inplace = True)

#Q_28, whether you approve the REPELL of obamacare
simpleCondense("Q28_1", 6)
RawMatrix.rename(columns={'Q28_1':'Q_28_Support_REPELLing_Obamacare'}, inplace = True)

#Q_29, how important is obamacare
simpleCondense("Q29_1", 4)
RawMatrix.rename(columns={'Q29_1':'Q_29_How_important_Obamacare_to_you'}, inplace = True)

#Q_30, Is global warming happening
simpleCondense("Q30_1", 1)
RawMatrix.rename(columns={'Q30_1':'Q_30_is_climate_change_happening'}, inplace = True)

#Q_31, how important is obamacare
simpleCondense("Q31_1", 2)
RawMatrix.rename(columns={'Q31_1':'Q_31_assume_happening_what is it caused by'}, inplace = True)

#Q_32
simpleCondense("Q32_1", 2)
RawMatrix.rename(columns={'Q32_1':'Q_32 should federal do more'}, inplace = True)

#Q_34
simpleCondense("Q34_1", 4)
RawMatrix.rename(columns={'Q34_1':'Q_34 how important to you'}, inplace = True)

#Q_36
simpleCondense("Q36_1", 4)
RawMatrix.rename(columns={'Q36_1':'Q_36 How often would you say that you follow what’s going on in government and public affairs?'}, inplace = True)

#Q_37
simpleCondense("Q37_1", 4)
RawMatrix.rename(columns={'Q37_1':'how intersted are you following the current political campaigns'}, inplace = True)

#Q_38, 40, 41, 43, 44
simpleCondense("Q38_1", 1)
simpleCondense("Q40_1", 1)
simpleCondense("Q41_1", 1)
simpleCondense("Q43_1", 1)
simpleCondense("Q44_1", 1)
RawMatrix.rename(columns={'Q38_1':'Did you register to vote in 2020(for example, state primary or other US/US city election)'}, inplace = True)
RawMatrix.rename(columns={'Q40_1':'Did you actually vote for 2020?'}, inplace = True)
RawMatrix.rename(columns={'Q41_1':'During political campaigns, do you typically talk to any people and try to show them why they should vote for or against one of the parties or candidates?'}, inplace = True)
RawMatrix.rename(columns={'Q43_1':'have you given money to an individual candidate running for public office in past 4 years?'}, inplace = True)
RawMatrix.rename(columns={'Q44_1':'did you or anyone in your household wear a campaign button, put a campaign sticker on your car or personal computer, or place a campaign sign in your window or in front of your (or your household\'s) house? in past 4 years'}, inplace = True)

#Q45_1-11
names = ["Joe Biden","Hillary Clinton","Kamala Harris","Jason Lewis","Mitch McConnell","Barack Obama","Nancy Pelosi","Mike Pence","Bernie Sanders","Tina Smith","Donald Trump"]
for i in range(len(names)):
    columnName = 'Q45_' + str(i+1)
    newColumnName = 'rank ' + names[i] + ' from 0-100'
    #print(columnName)
    #print(newColumnName)
    RawMatrix.rename(columns={columnName:newColumnName}, inplace = True)

#print(RawMatrix.head(5))

#delete meta-data columns that we don't need
RawMatrix.drop(columns=['StartDate','EndDate','Status','IPAddress','Progress','Finished','RecordedDate','Q72_2'], inplace = True)

#column 37-117 is analyze in with matrixCount.py
RawMatrix.drop(RawMatrix.columns[37:117], axis=1, inplace=True)


print(RawMatrix.iloc[2:20, 35:39])
RawMatrix.to_csv('phase_1_first_half_cleaned.csv', header=True)