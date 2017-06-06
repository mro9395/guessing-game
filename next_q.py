def get_next_question(answersValues): 
    listQuestions = pd.DataFrame(answersValues.sum(axis = 0))
    filterQuestions = listQuestions.index.isin(importantQuestion_name_list)    
    listQuestions = listQuestions[~filterQuestions]
    importantQuestion_name = listQuestions[listQuestions[0] == listQuestions.max().loc[0]].index[0]
    print importantQuestion_name
    # importantQuestion_name = 'Accompany individuals or groups to activities.'
    importantQuestion_index = answersValues.columns.get_loc(importantQuestion_name)
    importantQuestion_name_list.append(importantQuestion_name)
    return importantQuestion_index, importantQuestion_name, importantQuestion_name_list
