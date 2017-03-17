import MySQLdb
db = MySQLdb.connect('localhost','root','password','hackathon')
columns = ['Professionals.phoneNo','title','fullName','lastName','profession','keyword']
columnNames = ', '.join(columns)
cursor1 = db.cursor()
def getFreq(obvs,target,frm):
    sql = "SELECT {}, count({}) AS \'FREQUENCY\' FROM {} WHERE {} GROUP BY {} ORDER BY COUNT({})".format(target,target,frm,dictToWhere(obvs),target)
    cursor1.execute(sql)
    ans = cursor1.fetchall()
    return ans
def query(message):
    sql = "SELECT {} FROM Hackathon.Professionals, Hackathon.Keywords WHERE Professionals.phoneNo = Keywords.phoneNo AND Keywords.keyword = \'{}\'".format(columnNames,message)
    cursor1.execute(sql)
    ans=cursor1.fetchall()
    #print(sql)
    #print(ans)
    return ans
def dictToWhere(whereDict):
    for key, value in whereDict.iteritems():
        where = where+('{} = {} and ').format(key,value)
    where = where[:-4]
def advQuery(tables,columns,whereDict):
    fromTables =''
    for table in tables:
        fromTables = fromTables+', '+table 
    fromTables = fromTables[2:] 
    selection =''
    for column in columns:
        selection = selection + ', ' + column
    selection = selection[2:] 
    where =''
    for key, value in whereDict.iteritems():
        where = where+('{} = {} and ').format(key,value)
    where = where[:-4]
    sql = 'SELECT {} FROM {} WHERE {}'.format(selection,fromTables,where)
    print(sql)
    cursor1.execute(sql)
    ans = cursor1.fetchall()
    return ans 

def basicInsert(table,dicT):
    columns=''
    values =''

    for key, value in dicT:
        columns = columns +', ' + key
        values = values +', ' + value
    columns = '('+columns[2:]+')'
    values = '('+values[2:]+')'
    sql='Insert into {} {} values {}'.format(table,columns,values)
    print(sql)
    cursor1.execute(sql)
    db.commit
def update(table, upDict,eqDict):
    where =''
    for key, value in upDict:
        where = ('{} = {} and ').format(key,value)
    eq = ''
    #for key, value in 

def isProfession(m):
    return True
    