from urllib.request import urlopen
import re
import pandas as pd
import numpy as np



def FileDwnLdFun(path):


    # Download the file from the URL
    file = urlopen(path)

    # Create a new file on the hard drive
    temp = pd.read_csv(file)

    # datacsv = pd.DataFrame(tempCsv)
    temp.to_csv('Testing.csv', index=False)

    filname = path
    fup = re.split('/', filname)
    filenm = (re.split('\.', fup[5]))
    fileup = filenm[0]+'.csv'
    upath = fileup
    return upath


def return_csv(path):
    upath = FileDwnLdFun(path=path)

    testDF = pd.read_csv('Testing.csv')

    # CustomerList
    custDF = pd.read_csv("liveCustomerList.csv")

    # custDUp = custDF.apply(lambda x: x.astype(str).str.upper()) DONT NEED UPPERCASE

    # Combined test with Customer data
    testCust = pd.merge(testDF, custDF, on='custID', how='left')

    # BankLogin Check

    BankLogin = pd.read_csv("liveBankAcct.csv")

    FraudCust1 = pd.merge(testCust, BankLogin, on=['firstName', 'lastName'], how='left')
    WrngLogin = FraudCust1.drop(columns=['firstName', 'lastName'])
    WrngLogin['rightAcctFlag'] = np.where(WrngLogin['loginAcct'] == WrngLogin['bankAcctID'], 1, 0)
    LoginSol = WrngLogin.drop(columns=['loginAcct', 'bankAcctID'])
    # print(upath)

    # Write into CV --->

    LoginSol.to_csv(upath, index=False)

    # getting  filename again

    filname = upath
    filenm = (re.split('\.', filname))
    fileup = filenm[0]

    return fileup


#return_csv('https://www.dropbox.com/s/5lqxn1bl55cuzwu/363500.csv?dl=1')
#upath =
#FileDwnLdFun(path='https://www.dropbox.com/s/8stypjhl2y6ceul/sampleBankAcctInput.csv?dl=1')
#print(fileup)