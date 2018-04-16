# !---------------------------------------------------------------------!
# Importing all necessary packages -------------------------------------!
# !---------------------------------------------------------------------!

import numpy as np;
import pandas as pan;
import scipy.stats as spstats;
import csv;
import matplotlib.pyplot as plt;
import math;

# !---------------------------------------------------------------------!
# All Functions for the Program ----------------------------------------!
# !---------------------------------------------------------------------!

def printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD):
    printFirstDigitCounts(firstDigits, firstDigitFrequencies);
    meanFirstDigitCount = printMeanFirstDigitCount(firstDigitFrequencies);
    medianFirstDigitCount = printMedianFirstDigitCount(firstDigitFrequencies);
    skewnessFirstDigitCount = printSkewnessFirstDigitCount(firstDigitFrequencies);
    firstDigitCountMeanAD = printFirstDigitCountMeanAD(firstDigitFrequencies, meanFirstDigitCount);
    firstDigitCountMedianAD = printFirstDigitCountMedianAD(firstDigitFrequencies, medianFirstDigitCount);
    plotFirstDigitFrequencies(firstDigits, firstDigitFrequencies, benfordFrequencies, meanFirstDigitCount, medianFirstDigitCount, skewnessFirstDigitCount, firstDigitCountMeanAD, firstDigitCountMedianAD, benfordFirstDigitCountMeanAD);
    checkForConformity(benfordFirstDigitCountMeanAD, firstDigitCountMeanAD);

def printFirstDigitCounts(firstDigits, firstDigitFrequencies):
    firstDigitCounts = pan.DataFrame(list(zip(firstDigits, firstDigitFrequencies)), columns = ['Number', 'Probability']);
    print('FIRST DIGIT NUMBER FREQUENCIES : ');
    print('Number Frequency');
    for index, row in firstDigitCounts.iterrows():
        print(str(int(row['Number'])) + '       ' + str(row['Probability']));
    print();

def printMeanFirstDigitCount(firstDigitFrequencies):
    return np.mean(firstDigitFrequencies);

def printMedianFirstDigitCount(firstDigitFrequencies):
    return np.median(firstDigitFrequencies);

def printSkewnessFirstDigitCount(firstDigitFrequencies):
    return spstats.skew(firstDigitFrequencies);

def printFirstDigitCountMeanAD(firstDigitFrequencies, meanFirstDigitCount):
    firstDigitCountMeanADList = [];
    for firstDigitFrequenciesCount in firstDigitFrequencies:
        benfordFirstDigitCountMinusMean = abs(firstDigitFrequenciesCount - meanFirstDigitCount);
        firstDigitCountMeanADList.append(benfordFirstDigitCountMinusMean);
    return sum(firstDigitCountMeanADList)/len(firstDigitFrequencies);

def printFirstDigitCountMedianAD(firstDigitFrequencies, medianFirstDigitCount):
    firstDigitCountMedianADList = [];
    for firstDigitCount in firstDigitFrequencies:
        firstDigitCountMinusMedian = abs(firstDigitCount - medianFirstDigitCount);
        firstDigitCountMedianADList.append(firstDigitCountMinusMedian);
    return np.median(firstDigitCountMedianADList);

def plotFirstDigitFrequencies(firstDigits, firstDigitFrequencies, benfordFrequencies, meanFirstDigitCount, medianFirstDigitCount, skewnessFirstDigitCount, firstDigitCountMeanAD, firstDigitCountMedianAD, benfordFirstDigitCountMeanAD):
    width = 0.35;
    
    figure, axis = plt.subplots(figsize=(8, 8));
    statisticData = '''For First Digit Frequencies...
    Mean = ''' + str(meanFirstDigitCount) + '''
    Median = ''' + str(medianFirstDigitCount) + '''
    Skewness of Distribution = ''' + str(skewnessFirstDigitCount) + '''
    Median Absolute Deviation = ''' + str(firstDigitCountMedianAD) + '''
    Mean Aboslute Deviation (Mean AD) = ''' + str(firstDigitCountMeanAD) + '''
    Benford'\s Mean AD = ''' + str(benfordFirstDigitCountMeanAD) + '''
    Difference in Mean AD =''' + str(abs(benfordFirstDigitCountMeanAD - firstDigitCountMeanAD));
    textBoxProperties = dict(boxstyle = 'round', facecolor = 'wheat', alpha = 0.5);
    axis.text(0.05, 0.95, statisticData, transform=axis.transAxes,
        verticalalignment = 'top', bbox = textBoxProperties);
    
    subPlot001 = axis.bar(firstDigits, firstDigitFrequencies, width, color='red');
    subPlot002 = axis.bar(firstDigits + width, benfordFrequencies, width, color='yellow');
    # add some text for labels, title and axes ticks
    axis.set_xticks(firstDigits + width / 2);
    axis.set_yticks((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7));
    axis.set_xticklabels(tuple(range(1, 10)));
    axis.set_yticklabels((0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9));
    axis.legend((subPlot001[0], subPlot002[0]), ('Observed', 'Expected'));
    plt.show();
    
def checkForConformity(benfordFirstDigitCountMeanAD, firstDigitCountMeanAD):
    MeanADDifference = abs(benfordFirstDigitCountMeanAD - firstDigitCountMeanAD);
    print('Difference between Benford\'s MAD and Observed MAD: ' + str(MeanADDifference));
    if (MeanADDifference >= 0.000) and (MeanADDifference < 0.006):
        print("The data shows close conformity to Benford's Law.");
    elif (MeanADDifference >= 0.006) and (MeanADDifference < 0.012):
        print("The data shows acceptable conformity to Benford's Law.");
    elif (MeanADDifference >= 0.012) and (MeanADDifference < 0.015):
        print("The data shows marginal conformity to Benford's Law.");
    elif (MeanADDifference >= 0.015):
        print("The data does not conform to Benford's Law.");
    print();
    print('!---------------------------------------------------------------------!')
    print();

def resetFirstDigitFrequencies(firstDigitFrequencies):
    return [0, 0, 0, 0, 0, 0, 0, 0, 0];

# !---------------------------------------------------------------------!
# Important Global Variables used in the Program -----------------------!
# !---------------------------------------------------------------------!

firstDigits = np.arange(1, 10);
firstDigitChars = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
firstDigitFrequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0];
benfordFrequencies = list(math.log10(1 + 1 / number) for number in range(1, 10))
meanBenfordFrequencies = np.mean(firstDigitFrequencies);
medianBenfordFrequencies = np.median(firstDigitFrequencies);
firstDigitCountMeanADList = [];
for befordFirstDigitCount in benfordFrequencies:
    benfordFirstDigitCountMinusMean = abs(befordFirstDigitCount - meanBenfordFrequencies);
    firstDigitCountMeanADList.append(benfordFirstDigitCountMinusMean);
benfordFirstDigitCountMeanAD = (sum(firstDigitCountMeanADList) / len(firstDigitChars));
print('Benford Frequencies MeanAD: ' + str(benfordFirstDigitCountMeanAD));
print();
print('!---------------------------------------------------------------------!')
print();

# !---------------------------------------------------------------------!
# Main Program Code ----------------------------------------------------!
# !---------------------------------------------------------------------!
# Order of Data Sets :
#     1. Twitter Followers By Count
#     2. Passcode Data
#     3. Fundraising Loans
#     4. All Expired Loans
#     5. Corporate Payments
#     6. Apple Daily Returns
# !---------------------------------------------------------------------!
# !---------------------------------------------------------------------!

print('Twitter Followers...');
print();
with open(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\Twitter Users By Friends Count.txt", "r") as dataFile:
    twitterUsersByFollowerCount = csv.reader(dataFile, delimiter="\t");
    twitterUsersByFollowerCountList = list(twitterUsersByFollowerCount);

numberOfReadings = len(twitterUsersByFollowerCountList);
for listElement in twitterUsersByFollowerCountList:
    followerCountString = listElement[1];
    firstDigitFrequencies[int(followerCountString[0]) - 1] = firstDigitFrequencies[int(followerCountString[0]) - 1] + (1 / numberOfReadings);

del followerCountString;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# ------------------------------------------------------------------------ #

print('Passcode Data...');
print();
passcodeDataFrame = pan.DataFrame(pan.read_excel(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\passcodeData.xls"));

for index, row in passcodeDataFrame.iterrows():
    if row['Passcode'] < 1000:
        passcodeDataFrame.drop(index, inplace = True);

numberOfReadings = sum(passcodeDataFrame['Frequency']);
for index, row in passcodeDataFrame.iterrows():
    passcodeString = str(row['Passcode']);
    firstDigitFrequencies[int(passcodeString[0]) - 1] = firstDigitFrequencies[int(passcodeString[0]) - 1] + (row['Frequency'] / numberOfReadings);

del passcodeString;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# ------------------------------------------------------------------------ #

print('Fundraising Loans...');
print();
with open(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\fundraising_loans.csv", encoding = "latin1") as dataFile:
    reader = csv.reader(dataFile);
    dataHolder = [row for row in reader];

dataColumn = [dataHolder[0].index(element) for element in dataHolder[0] if element in ['Loan Amount']][0];
dataHolder.pop(0);
numberOfReadings = len(dataHolder);
for row in dataHolder:
    loanAmountString = str(row[dataColumn]);
    firstDigitFrequencies[int(loanAmountString[0]) - 1] = firstDigitFrequencies[int(loanAmountString[0]) - 1] + (1 / numberOfReadings);

del loanAmountString;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# !---------------------------------------------------------------------!

print('All Expired Loans...');
print();
with open(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\all_expired_loans.csv", encoding = "latin1") as dataFile:
    reader = csv.reader(dataFile);
    dataHolder = [row for row in reader];

dataColumn = [dataHolder[0].index(element) for element in dataHolder[0] if element in ['loan_amount']][0];
dataHolder.pop(0);
numberOfReadings = len(dataHolder);
for row in dataHolder:
    loanAmountString = str(row[dataColumn]);
    firstDigitFrequencies[int(loanAmountString[0]) - 1] = firstDigitFrequencies[int(loanAmountString[0]) - 1] + (1 / numberOfReadings);

del loanAmountString;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# !---------------------------------------------------------------------!

print('Corporate Payments...');
print();
corporatePaymentsDataFrame = pan.DataFrame(pan.read_excel(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\CorporatePaymentsData.xlsx", sheet_name = "Data"));

for index, row in corporatePaymentsDataFrame.iterrows():
    if row['Amount'] == 0.00:
        corporatePaymentsDataFrame.drop(index, inplace = True);

numberOfReadings = len(corporatePaymentsDataFrame['Amount']);
for index, row in corporatePaymentsDataFrame.iterrows():
    amountPaidString = str(row['Amount']);
    position = 0;
    while amountPaidString[position] not in firstDigitChars:
        if position is len(amountPaidString) - 1:
            break;
        else:
            position = position + 1;
    firstDigitFrequencies[int(amountPaidString[position]) - 1] = firstDigitFrequencies[int(amountPaidString[position]) - 1] + (1 / numberOfReadings);

del amountPaidString, position;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# !---------------------------------------------------------------------!

print('Apple Daily Returns...');
print();
appleDailyReturnsDataFrame = pan.DataFrame(pan.read_excel(r"D:\UniSA, Mawson Lakes\Statistical Programming for Data Science\Assignment 1\AppleReturns.xlsx", sheet_name = "Sheet1"));

for index, row in appleDailyReturnsDataFrame.iterrows():
    if row['Returns'] == 0.00:
        appleDailyReturnsDataFrame.drop(index, inplace = True);

numberOfReadings = len(appleDailyReturnsDataFrame['Returns']);
for index, row in appleDailyReturnsDataFrame.iterrows():
    returnsString = str(row['Returns']);
    position = 0;
    while returnsString[position] not in firstDigitChars:
        if position is len(returnsString) - 1:
            break;
        else:
            position = position + 1;
    firstDigitFrequencies[int(returnsString[position]) - 1] = firstDigitFrequencies[int(returnsString[position]) - 1] + (1 / numberOfReadings);

del returnsString, position;
printStatisticalOutput(firstDigits, firstDigitFrequencies, benfordFrequencies, benfordFirstDigitCountMeanAD);
firstDigitFrequencies = resetFirstDigitFrequencies(firstDigitFrequencies);

# !---------------------------------------------------------------------!