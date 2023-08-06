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
        

def get_file_from_s3(session, input_file_path, aws_filename, client_project_name='koya-canoa'):
    '''
    This function reads data contained within an S3 bucket.

    :param session: AWS temporary session token
    :type session: boto3.Session
    :param input_file_path: Key of the object to get.
    :type input_file_path: str
    :param aws_filename: Name of the specific folder where the data is contained.
    :type aws_filename: str
    :param client_project_name: Project name within s3.
    :type client_project_name: str
    :return: dictionary containing the file content
    :rtype: dict
    '''
    
    try:
        s3_client = session.client('s3')
        bucket = client_project_name

        return s3_client.get_object(Bucket=bucket, Key=input_file_path + aws_filename) 

    except Exception as err:
        error_message = f"{err}"
        raise Exception(error_message)
        
def put_file_in_s3(aws_session, df, input_file_path, aws_filename, client_project_name='koya-canoa'):

    '''
    This function sends data in csv format to a specific folder within s3.

    :param aws_session: AWS temporary session token.
    :type aws_session: boto3.Session
    :param df: dataframe that will be transformed into csv.
    :type df: pd.DataFrame
    :param input_file_path: Key of the object to get.
    :type input_file_path: str
    :param aws_filename: Name of the specific folder where the data is contained.
    :type aws_filename: str
    :param client_project_name: Project name within s3.
    :type client_project_name: str
    :return: None
    :rtype: None
    '''

    #TODO: fix it to work without self
    s3_resource = aws_session.resource()

    bucket = client_project_name

    try:
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)        
        s3_resource.Object(bucket, input_file_path + '/' + aws_filename).put(Body=csv_buffer.getvalue())

    except Exception as e:
        print(e)
        raise Exception('Fail while uploading file to S3')
        

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False

    message = f"{bucket_name} created"

    return message

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

def get_available_files_aws(bucket,profile_name=None,filter_by=None):
    
    """Retrieve a list of available files from an AWS S3 bucket

    :param bucket: Name of the S3 bucket to retrieve files from
    :param profile_name: AWS profile name to use for authentication, defaults to `os.getenv('AWS_PROFILE_NAME')`
    :param filter_by: String to filter file names by, defaults to `None`
    :return: List of available files in the specified S3 bucket
    """

    if profile_name is None:
        profile_name = os.getenv('AWS_PROFILE_NAME')
    
    aws_session = boto3.Session(profile_name=profile_name)
    s3 = aws_session.resource('s3')
    bucket_obj = s3.Bucket(bucket)
    
    l=[]
    for my_bucket_object in bucket_obj.objects.all():
        key = my_bucket_object.key
        if filter_by is not None:
            if filter_by in key:
                l.append(key)
        else:
            l.append(key)
    return l

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

    files = [k for k in available_files if source in k]
    if len(files)==0:
        raise ValueError(f'file not found for source: {source}')
        
    l=[]
    for k in files:
        d=re.search('(\d\d-\d\d-\d+).csv',k).group(1)
        l.append((k,pd.Timestamp(d)))
    l=(sorted(l, key = lambda x: x[1]))
    latest = l[-1][0]
    if source not in latest:
        return None
    return latest


def save_data_aws(data,stage,step,source,client_project_name,add_info=None,filename=None,profile_name=None):

    """Save Data to AWS S3

    This function saves a given data to S3 bucket, the file is saved in a specified
    path with a specified name. If no name is provided, the name of the file
    is generated based on the source, today's date and any additional information.

    :param data: pandas dataframe to be saved
    :param stage: String name of stage, e.g., 'development', 'prodution'
    :param step: String name of step, e.g., 'ingestion', 'normalization'
    :param source: String name of source, e.g., 'fanka', 'simon'
    :param client_project_name: String name of S3 bucket to save to e.g., 'koya-fermat'
    :param add_info: Optional string additional information to add to filename
    :param filename: Optional string filename, defaults to source_today's_date.csv
    :param profile_name: Optional string profile name for AWS access
    :return: None
    """
    
    if profile_name is None:
        profile_name = os.getenv('AWS_PROFILE_NAME')
    csv_buffer = io.StringIO()
    data.to_csv(csv_buffer, index=False)
    
    today = datetime.datetime.now().strftime('%m-%d-%Y')
    
    aws_session = boto3.Session(profile_name=profile_name)
    s3_resource = aws_session.resource('s3')
    output_file_path=f'{stage}/{step}/data/'
    if filename is None:
        if add_info is not None:
            filename = f'{add_info}_{source}_{today}.csv'
        else:
            filename = f'{source}_{today}.csv'
    print('saving to:',output_file_path+filename)
    
    s3_resource.Object(client_project_name, output_file_path+filename).put(Body=csv_buffer.getvalue())