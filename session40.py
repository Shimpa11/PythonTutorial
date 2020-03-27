import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
dataSet=pd.DataFrame()

dataSet['outlook']=['sunny','sunny','overcast','rainy','rainy','rainy',
                    'overcast','sunny','sunny','rainy','sunny',
                    'overcast','overcast','rainy']

dataSet['temperature']=['hot','hot','hot','mild','cool',
                      'cool','cool','mild','cool','mild',
                        'mild','mild','hot','mild']

dataSet['humidity']=['high','high','high','high','normal',
                     'normal','normal','high','normal','normal','normal',
                     'high','normal','high']

dataSet['windy']=['false','true','false','false','false',
                  'true','true','false','false','false','true','true',
                  'false','true']

dataSet['play']=['no','no','yes','yes','yes','no',
                 'yes','no','yes','yes','yes','yes','yes','no']
# X=dataSet.iloc[:,:-1]
Y=dataSet.iloc[:,:5]
#
# labelEncoder_X=LabelEncoder()
# X=X.apply(LabelEncoder().fit_transform())
# print(dataSet)


def computeEntropyDataSet():
    # out of 14 9 yes and 5 no
    # E(S)=-P(Yes)*log_base2(P(Yes))-P(No)*log_base2 (P(No))
    # E(s)=-9/14 *log_base2(9/14)-5/14*log_base2(5/14)

    # print(len(dataSet['play']))
    # print(len(dataSet[dataSet['play']=='yes']))
    # print(len(dataSet[dataSet['play']=='no']))

    total=len(dataSet['play'])
    numOfYes=len(dataSet[dataSet['play']=='yes'])
    numOfNo=len(dataSet[dataSet['play']=='no'])
    probabiltyYes=numOfYes/total
    probabiltyNo = numOfNo / total

    # print(probabiltyYes)
    # print(probabiltyNo)


    entropy=-(probabiltyYes*np.log2(probabiltyYes))-(probabiltyNo*np.log2(probabiltyNo))

    # entropy=-(numOfYes/total*np.log2(numOfYes/total))-(numOfNo / total*np.log2(numOfNo / total))

    # entropy=-(len(dataSet[dataSet['play']=='yes'])/len(dataSet['play']) * np.log2(len(dataSet[dataSet['play']=='yes'])/len(dataSet['play']))
    #           -(len(dataSet[dataSet['play']=='no'])/len(dataSet['play'])*np.log2((len(dataSet[dataSet['play']=='no'])/len(dataSet['play']))))

    # print("entropy of data set",entropy)
    return entropy



def informationGaininOutlook():
    y=dataSet[dataSet['outlook']=='sunny']
    # print(len(y))
    # print(len(y[y['play']=='yes']))
    # print(len(y[y['play']=='no']))
    total_sunny=len(y)
    yes_sunny=len(y[y['play']=='yes'])
    no_sunny=len(y[y['play']=='no'])
    entropySunny=-(yes_sunny/total_sunny*np.log2(yes_sunny/total_sunny))-(no_sunny/total_sunny*np.log2(no_sunny/total_sunny))
    # print("entropy of sunny",entropySunny)

    z = dataSet[dataSet['outlook'] == 'overcast']
    total_overcast=len(z)
    # print(len(z[z['play']=='yes']))
    yes_overcast=len(z[z['play']=='yes'])
    entropyOvercast=-(yes_overcast/total_overcast*np.log2(yes_overcast/total_overcast))
    # print("entropy of overcast",entropyOvercast)


    r=dataSet[dataSet['outlook'] == 'rainy']
    total_rainy=len(r)
    # print(len(r[r['play']=='yes']))
    yes_rainy=len(r[r['play']=='yes'])
    no_rainy=len(r[r['play']=='no'])
    entropyRainy=-(yes_rainy/total_rainy*np.log2(yes_rainy/total_rainy))-(no_rainy/total_rainy*np.log2(no_rainy/total_rainy))

    # print("entropy of rainy",entropyRainy)

    # information of outlook
    I_outlook=(total_sunny/len(dataSet['play'])*entropySunny)+(total_overcast/len(dataSet['play'])*entropyOvercast)+(total_rainy/len(dataSet['play'])*entropySunny)
    print("Information of outlook",I_outlook)


#     informartion gain from outlook
    gain_outlook=computeEntropyDataSet() -I_outlook
    print("gain from outlook is",gain_outlook)
    print()
print("Entropy Of Data Set:", computeEntropyDataSet())
print()
informationGaininOutlook()

def informationGainTemp():
    h = dataSet[dataSet['temperature'] == 'hot']
    total_hot = len(h)

    yes_hot = len(h[h['play'] == 'yes'])
    no_hot = len(h[h['play'] == 'no'])
    entropyHot = -(yes_hot / total_hot * np.log2(yes_hot / total_hot)) - (
                no_hot / total_hot * np.log2(no_hot / total_hot))

    # print("entropy of hot", entropyHot)

    c = dataSet[dataSet['temperature'] == 'cool']
    total_cool = len(c)

    yes_cool = len(c[c['play'] == 'yes'])
    no_cool= len(c[c['play'] == 'no'])
    entropyCool = -(yes_cool / total_cool * np.log2(yes_cool / total_cool)) - (
            no_cool / total_cool * np.log2(no_cool / total_cool))

    # print("entropy of cool", entropyCool)

    m = dataSet[dataSet['temperature'] == 'mild']
    total_mild= len(m)

    yes_mild = len(m[m['play'] == 'yes'])
    no_mild = len(m[m['play'] == 'no'])
    entropyMild = -(yes_mild / total_mild * np.log2(yes_mild / total_mild)) - (
            no_mild / total_mild * np.log2(no_mild / total_mild))

    # print("entropy of Mild", entropyMild)

# information of temperature
    I_temperature=(total_hot/len(dataSet['play'])*entropyHot)+(total_cool/len(dataSet['play'])*entropyCool)+(total_mild/len(dataSet['play'])*entropyMild)
    print("information of temperature",I_temperature)
#     gain from temperature
    gainTemp=computeEntropyDataSet()-I_temperature
    print("gain from Temperature",gainTemp)
    print()
informationGainTemp()


def informationGainHumidity():
    h_high = dataSet[dataSet['humidity'] == 'high']
    total_high= len(h_high)

    yes_high = len(h_high[h_high['play'] == 'yes'])
    no_high = len(h_high[h_high['play'] == 'no'])
    entropyHigh = -(yes_high / total_high * np.log2(yes_high / total_high)) - (
                no_high / total_high * np.log2(no_high / total_high))

    # print("entropy of high", entropyHigh)

    n = dataSet[dataSet['humidity'] == 'normal']
    total_normal = len(n)

    yes_normal = len(n[n['play'] == 'yes'])
    no_normal= len(n[n['play'] == 'no'])
    entropyNormal = -(yes_normal / total_normal * np.log2(yes_normal / total_normal)) - (
            no_normal / total_normal * np.log2(no_normal / total_normal))

    # print("entropy of Normal", entropyNormal)


# information of humidity
    I_Humidity=(total_high/len(dataSet['play'])*entropyHigh)+(total_normal/len(dataSet['play'])*entropyNormal)
    print("information of Humidity",I_Humidity)


    # gain    from humidity
    gainHumidity = computeEntropyDataSet() - I_Humidity
    print("gain from Humidity", gainHumidity)
    print()


informationGainHumidity()



def informationGainWindy():
    windy_False = dataSet[dataSet['windy'] == 'false']
    total_false= len(windy_False)

    yes_false = len(windy_False[windy_False['play'] == 'yes'])
    no_false = len(windy_False[windy_False['play'] == 'no'])
    entropyFalse = -(yes_false / total_false * np.log2(yes_false / total_false)) - (
                no_false / total_false * np.log2(no_false / total_false))

    # print("entropy of false", entropyFalse)

    windy_true = dataSet[dataSet['windy'] == 'true']
    total_true = len(windy_true)

    yes_True = len(windy_true[windy_true['play'] == 'yes'])
    no_True= len(windy_true[windy_true['play'] == 'no'])
    entropyTrue = -(yes_True / total_true * np.log2(yes_True / total_true)) - (
            no_True / total_true * np.log2(no_True / total_true))

    # print("entropy of true", entropyTrue)


# information of windy
    I_Windy=(total_false/len(dataSet['play'])*entropyFalse)+(total_true/len(dataSet['play'])*entropyTrue)
    print("information of Windy",I_Windy)
    # gain    from windy
    gainWindy = computeEntropyDataSet() - I_Windy
    print("gain from Windy", gainWindy)


informationGainWindy()



# print(computeEntropyDataSet())


