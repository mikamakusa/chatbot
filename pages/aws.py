import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import json

st.title = "AWS Powered Chatbot"

st.sidebar.header('AWS Credentials')
aws_access_key = st.sidebar.text_input("AWS Access Key : ")
aws_secret_key = st.sidebar.text_input("AWS Secret Key : ")
aws_region = st.sidebar.text_input('AWS Region : ')


if st.sidebar.button('Connect'):
    if aws_access_key and aws_secret_key:
        try:
            session = boto3.Session(
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=aws_region
            )
            client = session.client("sagemaker-runtime")

        except NoCredentialsError:
            st.error('Invalid AWS credentials')
        except PartialCredentialsError:
            st.error('Incomplete AWS credentials')
        except Exception as e:
            st.error(f'An error occurred : {str(e)}')
    else:
        st.warning('Please fill out all fields')

if st.sidebar.button("back"):
    st.switch_page("main.py")


def query_sagemaker_endpoint(input_text):
    response = client.invoke_endpoint(
        EndpointName='your-endpoint-name',
        ContentType='application/json',
        Body=json.dumps({"input": input_text})
    )
    result = json.loads(response['Body'].read().decode())
    return result


user_input = st.text_area("Enter your text here")

if st.button("Submit"):
    if user_input:
        result = query_sagemaker_endpoint(user_input)
        st.write(result)
    else:
        st.write("Please enter some text.")