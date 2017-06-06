samples = pd.concat(load_pickle('list_df_major_classes.pkl'))
samples.set_index('id_soc_major')

optimalNumber = 20
importantQuestion_name_list = []
answers = []

data = pd.read_excel('DWA.xlsx')
data['count'] = 1
data = pd.pivot_table(data, index = ['O*NET-SOC Code','Title','Major'], columns = ['DWA Title'], values =  'count')
data = data.fillna(0).reset_index().set_index(['O*NET-SOC Code'])
answersValues = data.iloc[:,2:]
target = data.iloc[:,1].values
shape = answersValues.shape

scaler = StandardScaler()
scaler.fit(answer_values)
answer_values = scaler.transform(answer_values)
clf = MLPClassifier(solver='adam', learning_rate='adaptive', alpha = 0, hidden_layer_sizes=(1000,), max_iter=500)
clf.fit(answer_values, target)

answersUser = pd.DataFrame(index=answersValues.index, data=np.zeros(shape))
answersMatchMatrix = pd.DataFrame(index=answersValues.index)
answersMatchMatrix_weight = pd.DataFrame(index=answersValues.index)

importantQuestion_index, importantQuestion_name, importantQuestion_name_list = get_next_question(answersValues)

for i in xrange(optimalNumber):    
    answer = int(raw_input(importantQuestion_name))
    answers.append(answer)
    print i
    answersUser[importantQuestion_index] = answer
    answersMatch = np.where(answersUser[importantQuestion_index] == answersValues[importantQuestion_name], 1, 0)
    answersMatchMatrix[importantQuestion_index] = answersMatch
    probableSamples = answersMatchMatrix[answersMatchMatrix[importantQuestion_index]==1].index.tolist()
    answersValues = answersValues.ix[probableSamples]
    answersUser = answersUser.ix[probableSamples]
    answersMatchMatrix = answersMatchMatrix.ix[probableSamples]
#     data = data.ix[probableSamples]
#     print data.iloc[:,0]
    importantQuestion_index, importantQuestion_name, importantQuestion_name_list = get_next_question(answersValues)
answer = int(raw_input(importantQuestion_name))
answers.append(answer)
q = random.randint(0,1)
if q == 1:
    print 'Ese es uno complicado'
else:
    print 'Creo que ya lo tengo'
