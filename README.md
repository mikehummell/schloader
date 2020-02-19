# SCH Loader
There are two main parts in this libary. the DataFrame creater and the BI Loader

## Create Dataframe
Read CSV, SAP TXT Files and creates dataframe prepared for the bi

## Upload to BI
Upload the dataframe (Pandas) into a db and start the loading procedure

```
    objectToLoad = DBObject("yae2_repnn")
    objectToLoad.headerToSkip(3)

    #objectToLoad.loadFromCSV("transformedExcel.csv", ";")
    

    objectToLoad.loadFromSapTxt("yat1_ts_pernr_1500_w2.txt",3)
    objectToLoad.cleanHeader()

    objectToLoad.specifySQLServer("DRIVER={SQL Server};SERVER=SCHWSR0082;DATABASE=DBSCHBI;Trusted_Connection=yes;")

 
    biCon.loadIntoLoadTable(objectToLoad)
    biCon.loadIntoOdsTable()



    print(objectToLoad)
    print(objectToLoad.getDataFrame())
```