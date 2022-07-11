import pandas as pd
df = pd.read_csv("./Input_1.csv")
a = pd.melt(df, id_vars =["Name","id","Chapter Tag"])
a = a.sort_values(["Name","variable"])
a.reset_index(drop=True)

name=""
idd = ""
chapter =""
test=""
val =0
li =[]
da =[]
for ind in a.index:
    name = a['Name'][ind]
    idd = a['id'][ind]
    chapter = a['Chapter Tag'][ind]
    test = a['variable'][ind]
    li.append(a['value'][ind])
    val+=1
    if val==6:
        if "-" in li:
            val =0
            li = []
        else:
            da.append([name,idd,chapter,test.split("-")[0],li[3],li[1],li[3],li[4],li[2],li[5]])
            val = 0
            li = []
ans = pd.DataFrame(da,columns=['Name', 'Username', 'Chapter Tag','Test_Name','answered','correct','score','skipped','time-taken (seconds)','wrong'])
ans.to_csv('output.csv',index=False)
