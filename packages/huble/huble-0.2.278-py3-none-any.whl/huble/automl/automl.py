import pandas as pd
from evalml.problem_types import detect_problem_type
from evalml.data_checks import DefaultDataChecks
from evalml.automl import AutoMLSearch
from evalml.pipelines.utils import generate_pipeline_code
from evalml.preprocessing import split_data

def Automl(data, target_column,task):
    #split into X and y
    X = data.drop(target_column, axis=1)
    y = data[target_column]  


    #train test split
    X_train, X_test, y_train, y_test = split_data(X, y, problem_type=task)

    #Datachecks
    objective=""
    if task =='binary':
      objective = objective+"log loss binary"
    elif task == 'multiclass':
      objective = objective+"log loss multiclass"
    elif task=='regression':
      objective = objective+"R2"
    data_checks = DefaultDataChecks(task, objective)
    messages = data_checks.validate(X_train, y_train)

    errors = [message for message in messages if message["level"] == "error"]
    warnings = [message for message in messages if message["level"] == "warning"]
    data_issues = [] 
    for warning in warnings:
        data_issues.append("Warning:" + warning["message"])

    for error in errors:
        data_issues.append("Error:" + error["message"])


    #AutoMl Search
    automl = AutoMLSearch(X_train=X_train, y_train=y_train, problem_type=task)
    automl.search()

    #Pipeline Rankings
    rankings = automl.rankings
    rankings_json = rankings.to_json(orient="table")

    #Best Pipeline
    best_pipeline = automl.best_pipeline
    
    steps_list=[]
    for step in best_pipeline:
      steps_list.append(step)
  
    #metrics
    objectives=[]
    if task =='binary':
      objectives.extend(['mcc binary',
                        'log loss binary',                
                        'auc',
                        'recall',
                        'precision',
                        'f1',
                        'balanced accuracy binary',
                        'accuracy binary'])
    elif task == 'multiclass':
      objectives.extend(['mcc multiclass',
                        'log loss multiclass',
                        'auc weighted',
                        'auc macro',
                        'auc micro',
                        'recall weighted',
                        'recall macro',
                        'recall micro',
                        'precision weighted',
                        'precision macro',
                        'precision micro',
                        'f1 weighted',
                        'f1 macro',
                        'f1 micro',
                        'balanced accuracy multiclass',
                        'accuracy multiclass'])
    elif task=='regression':
      objectives.extend(['expvariance',
                        'maxerror',
                        'medianae',
                        'mse',
                        'mae',
                        'r2',
                        'mean squared log error',
                        'root mean squared log error',
                        'root mean squared error',])
                        
    metrics = dict(best_pipeline.score(X_test, y_test, objectives)) 

    #Feature importance for best pipeline
    feature_imp = best_pipeline.feature_importance
    feature_imp_json = feature_imp.to_json(orient="table")

    #generating code for best_pipeline
    code = generate_pipeline_code(best_pipeline)

    return data_issues, task, rankings_json, steps_list, feature_imp_json, code, best_pipeline, metrics
