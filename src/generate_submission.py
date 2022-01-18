'''
Пример генерации файла со скорами для отложенной выборки
python src/generate_submission.py
'''
from random import random

import pandas as pd

input_fields = ['INPUT:diff1', 'INPUT:diff2', 'INPUT:query1', 'INPUT:query2']


def get_model_scores(text: str, correction: str, query: str, query_corrected: str) -> float:
    # Cырой скор модельки, если есть
    # Сюда можно встроить вашу модель
    return 0.5


def get_model_prediction(text: str, correction: str, query: str, query_corrected: str) -> str:
    # Пример с заглушкой вместо вашей модели
    # Сюда можно встроить вашу модель
    return 'yes' if random() > 0.5 else 'no'


def generate_submission(submission_name: str):
    df = pd.read_csv('data/holdout.tsv', '\t')
    df['OUTPUT:result'] = df.apply(
        lambda row: get_model_prediction(
            text=row['INPUT:diff1'],
            correction=row['INPUT:diff2'],
            query=row['INPUT:query1'],
            query_corrected=row['INPUT:query2'],
        ), axis=1)
    df['OUTPUT:score'] = df.apply(
        lambda row: get_model_scores(
            text=row['INPUT:diff1'],
            correction=row['INPUT:diff2'],
            query=row['INPUT:query1'],
            query_corrected=row['INPUT:query2'],
        ), axis=1)
    df.to_csv(f'data/{submission_name}.tsv', '\t', index=False)


if __name__ == '__main__':
    generate_submission('sample_submission')
