import os
import langchain
#from langchain_community.llms import HuggingFaceHub
#from langchain_huggingface import HuggingFaceHub
from langchain_huggingface import HuggingFacePipeline
from langchain_huggingface import ChatHuggingFace

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

llm = HuggingFacePipeline(repo_id="tiiuae/falcon-7b-instruct")
query = "There was a boy who went to school"
output = llm.invoke(query)
print(output)