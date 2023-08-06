import boto3
import logging
from botocore.exceptions import ClientError
import pandas as pd
import os
import re
import io
import datetime


def config_aws_env(profile_name):
    '''
    This function creates a boto3 session based on the profile name. If profile name is not provided, the default profile is used.

    :param profile_name: The name of the profile to use.
    :type profile_name: str
    :return: boto3 session object
    :rtype: boto3.Session
    '''
    
    try:
        response = boto3.Session(profile_name=profile_name)
        
        return response

    except Exception as err:
        error_message = f"{err}"
        raise Exception(error_message)
        
        

def load_data_aws(stage='development'
                  ,step='ingestion'
                  ,source='scottdental'
                  ,context='aws'
                  ,client_project_name='koya-faliam'
                  ,date=None
                  ,profile_name=None
                  ,get_latest_file=False):

    '''
    Load data from AWS S3, either the latest file or a file with a specified date.
    :return: DataFrame with the loaded data
    :rtype: pandas.DataFrame

    stage: The stage of the data processing (e.g. development, production).
    type: str, optional

    step: The step in the data processing (e.g. ingestion, cleaning, analysis).
    type: str, optional

    source: The source of the data (e.g. scottdental, johns Hopkins, etc.).
    type: str, optional

    context: The location where the data is stored (e.g. AWS, GCP, etc.).
    type: str, optional

    client_project_name: The name of the project within the cloud storage.
    type: str, optional

    date: The date of the file to be loaded (YYYY-MM-DD). If None, the latest file will be loaded if get_latest_file is True.
    type: str, optional

    profile_name: The name of the AWS profile to use. If None, the default profile is used.
    type: str, optional

    get_latest_file: If True, the latest file will be loaded if date is None.
    type: bool, optional
    '''
    if profile_name is None:
        profile_name = os.getenv('AWS_PROFILE_NAME')
        
    aws_session = config_aws_env(profile_name=profile_name)

    if date is None and get_latest_file==True:
        available_files = get_available_files_aws(client_project_name,filter_by=step)
        latest_file = get_latest_file_aws(available_files,source)
        if latest_file is None:
            raise ValueError('not file match the criteria')
        else:
            aws_filename=latest_file[latest_file.find('data')+5:]

    else:
        aws_filename = f'{source}_{date}.csv'

    print(f'reading: {stage}/{step}/data/{aws_filename}')

    koya_s3_obj = get_file_from_s3(client_project_name=client_project_name
                                   ,session=aws_session
                                   ,input_file_path=f'{stage}/{step}/data/'
                                   ,aws_filename=aws_filename)
    s3_data = koya_s3_obj.get('Body')
    data = pd.read_csv(s3_data,lineterminator='\n')
    data.columns = [k.strip('\r') for k in data.columns]
    return data



def get_latest_file_aws(available_files,source):

    """Get the latest file for a source from the list of available files.

    This function filters the list of available files by checking if the source string
    is in the file name. The filtered files are then sorted by date and the latest file
    is returned.

    :param available_files: List of strings containing the names of the available files
    :param source: String to match with the available files to get the latest file
    :return: String with the name of the latest file or None if no match is found.
    :raises: ValueError if no file is found for the specified source.
    """

    files = [k for k in available_files if (source in k) and ("______" in k)]
    
    if len(files) == 0:
        files = [k for k in available_files if (source in k)]
    
    if len(files)==0:
        raise ValueError(f'file not found for source: {source}')

    l=[]
    for k in files:
        d=re.search('(\d{2})-(\d{2})-(\d{4})',k)
        if d:
            date = f"{d.group(1)}-{d.group(2)}-{d.group(3)}"
            l.append((k,pd.Timestamp(date)))
            
    l=(sorted(l, key = lambda x: x[1]))
    latest = l[-1][0]
    if source not in latest:
        return None
    return latest