'''
Script for building table containing patient and drug/stress related data.
'''
import argparse
import pandas as pd
import os
import numpy as np
from sqlite3 import connect

parser = argparse.ArgumentParser(description='Build table containing patient and drug/stress related data from a specified scenario')
parser.add_argument('SCENARIO', choices=['1','2'], help='Build features from this scenario')
args = parser.parse_args()

SYNTHEA_DIR = '../../data/raw/synthea/'

scenario = args.SCENARIO
patients_path = os.path.join(SYNTHEA_DIR, f'scenario{scenario}/patients.csv')
conditions_path = os.path.join(SYNTHEA_DIR, f'scenario{scenario}/conditions.csv')
encounters_path = os.path.join(SYNTHEA_DIR, f'scenario{scenario}/encounters.csv')

conds_df = pd.read_csv(conditions_path, usecols=['PATIENT', 'DESCRIPTION', 'START'])

def match_substring(sub_str, s):
    return sub_str.lower() in s.lower()

conds_df['OPIOID'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('opioid', x))
conds_df['ALCOHOL'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('alcohol', x))
conds_df['MISUSE'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('misuse', x))
conds_df['OVERDOSE'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('overdose', x))
conds_df['TOBACCO'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('tobacco', x))
conds_df['VIOLENCE'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('violence', x))
conds_df['PARTNER'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('partner abuse', x))
conds_df['DEPRESSION'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('depression', x))
conds_df['ANXIETY'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('anxiety', x))
conds_df['STRESS'] = conds_df['DESCRIPTION'].apply(lambda x: match_substring('stress', x))

drug_conds_df = conds_df.sort_values(by='START').groupby('PATIENT').aggregate({
    'OPIOID': lambda x: np.sum(x)>0,
    'ALCOHOL': lambda x: np.sum(x)>0,
    'MISUSE': lambda x: np.sum(x)>0,
    'OVERDOSE': 'sum',
    'TOBACCO': lambda x: np.sum(x)>0,
    'VIOLENCE': 'sum',
    'PARTNER': 'sum',
    'DEPRESSION': lambda x: np.sum(x)>0,
    'ANXIETY': lambda x: np.sum(x)>0,
    'STRESS': lambda x: np.sum(x)>0,
})
del conds_df

conn = connect(':memory:')
drug_conds_df.to_sql('drug_conditions', conn, if_exists='replace')
del drug_conds_df

patients_df = pd.read_csv(patients_path, usecols=['Id', 'BIRTHDATE', 'DEATHDATE'])
patients_df.to_sql('patients', conn, if_exists='replace')
del patients_df

encounters_df = pd.read_csv(encounters_path, usecols=['PATIENT', 'START'])
encounters_df.to_sql('encounters', conn, if_exists='replace')
del encounters_df

patient_drugs = pd.read_sql(
    '''
    SELECT p.Id, p.birthdate, p.deathdate, d.OPIOID,
        d.ALCOHOL, d.MISUSE, d.OVERDOSE, d.TOBACCO,
        d.VIOLENCE, d.PARTNER, d.DEPRESSION, d.ANXIETY, d.STRESS,
        e.start
    FROM patients p
    JOIN drug_conditions d on p.Id = d.patient
    JOIN encounters e on p.Id = e.patient
    ''',
    conn
)

patient_drugs['prognostic'] = (~pd.isna(patient_drugs['DEATHDATE'])) * (
    (patient_drugs['DEATHDATE'].astype(np.datetime64) - patient_drugs['START'].astype(np.datetime64)) / np.timedelta64(1,'D')
)
patient_drugs['prognostic'].fillna(-1, inplace=True)
patient_drugs.to_csv(f'../../data/interim/scenario{scenario}/patient-drugs.csv', index=False)