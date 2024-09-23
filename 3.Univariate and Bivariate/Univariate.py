class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for columnName in dataset.columns:
            if dataset[columnName].dtype == 'O':
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan, qual

    
    def freqTable(colunName,dataset):
        freqTable=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Frequency","CumSum"])
        freqTable["Unique_Values"]=dataset[colunName].value_counts().index
        freqTable["Frequency"]=dataset[colunName].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"])/103
        freqTable["CumSum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable

    
    def Univariate(quan,dataset):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR",
                                "1.5Rule","LesserOutlierRange","GreaterOutlierRange","Min","Max","skew","kurtosis"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
        
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5Rule"]=1.5*descriptive[columnName]["IQR"]
            
            descriptive[columnName]["LesserOutlierRange"]=descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5Rule"]
            descriptive[columnName]["GreaterOutlierRange"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5Rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
            descriptive[columnName]["skew"]=dataset[columnName].skew()
            descriptive[columnName]["kurtosis"]=dataset[columnName].kurtosis()
        return descriptive


