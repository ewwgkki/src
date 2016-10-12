'''
Created on Oct 6, 2016

@author: ewwgkki
'''
import csv
import logging
import os
import os.path
import sys
import glob

##########logging module##############

#set logging system
logger1=logging.getLogger('Parameter:')
logger2=logging.getLogger('SUM:')
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)

#set logging file
fileheader=logging.FileHandler('test.log')
fileheader.setLevel(logging.DEBUG)

#set handler
ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#set format
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
ch.setFormatter(formatter)
fileheader.setFormatter(formatter) 

#add header
logger1.addHandler(fileheader)
logger1.addHandler(ch)
logger2.addHandler(fileheader)
logger2.addHandler(ch)

#Parameters need to be caculated
parameter_list = ['LTEHybridFailureDueToSanityCheck','LTEAGPSUEAssistedFailureDueToSanityCheck','LTEAGPSUEBasedFailureDueToSanityCheck','LTEOTDOAFailureDueToSanityCheck','GeneralLCSAPLocationRequestNonEmergency','GeneralLCSAPLocationRequestEmergency','GeneralLCSAPLocationResponseSuccessfulEmergency','GeneralLCSAPLocationResponseSuccessfulNonEmergency','LTEAGPSUEBasedAttempts','LTEAGPSUEBasedSuccessful','LTEHybridAttempts','LTEHybridSuccessful','LTEOTDOAAttempts','LTEOTDOASuccessful']
list_length = len(parameter_list)

def Calculation():
    path=raw_input('Please input the path:')
    directory=os.path.join(path)
    print directory
    print 'Calculating:'
    for i in range(list_length):
        #Sum_allfiles means all sum of that parameter in all files.
        Sum_allfiles=0
        for root,dirs,files in os.walk(directory):
            #Sum_allfiles means all sum of that parameter in one file.
            SumTot=0
            for file in files:
                if file.endswith(".csv"):                 
                    #print "Searching file:",file
                    os.chdir(directory)
                    reader=csv.DictReader(open(file))
                    a=[column[parameter_list[i]] for column in reader]
                    ParameterCont=a
                    #print parameter_list[i]
                    #SumTot=0
                    line=0
                    line_length=len(a)
                    #print line_length
                    for x in range(line_length-1):
                        line=x+2
                        if ParameterCont[x]=='':
                            ParameterCont[x]=0
                        SumTot=SumTot+float(ParameterCont[x])
                        #print SumTot
            Sum_allfiles=Sum_allfiles+SumTot
        logger1.info(parameter_list[i])
        logger2.info(Sum_allfiles)                


def main():
    
    Calculation()    
     
main()


