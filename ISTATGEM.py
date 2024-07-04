from models.gemini.gemini_multimodal import get_file, create_model, get_csv_file
from extractors.models import Models
from extractors.general_extractors.config.prompt_config import table_schemas
from AWSInteraction.EnvVarSetter import EnvVarSetter
import json
import pandas as pd
from typing import List
from pydantic import BaseModel, Field
from typing import Optional
import os
import re



# Load the example prompts  
from prompts.certificates.test_prompt_complexity.example_prompt_1 import  prompt_example_7

# Create the generative model
project="pftpro-167412"
location="us-central1"
model_version = "gemini-1.5-pro-preview-0409"
# "gemini-1.5-flash"
# "gemini-1.5-pro-preview-0409"
model = create_model(project, location, model_version)

# Configuration for the generation
generation_config = {
    "max_output_tokens": 8000,
    "top_p": 0.95,
    "temperature": 0,
}

path3 = r"C:\Users\ribhu.kaul\RibhuLLM\Extraction_Program\Latest_Extraction\GeminiBased_ProductName\popolazione_Italia_2023.csv"


mid_processing = get_csv_file(path3)
prompt_example_7.append(mid_processing)

test_response3 = model.generate_content(prompt_example_7, generation_config=generation_config)
print(test_response3)

def extract_text_from_response(response):
    """ Safely extracts text from a nested response object. """
    try:
        # Accessing text assuming 'response' is a class with attribute access
        return response.candidates[0].content.parts[0].text
    except (AttributeError, IndexError) as e:
        # If the structure is different or parts are missing, return an empty string
        print(f"Error accessing text: {e}")
        return ""

# Let's assume test_response3 is already fetched and is a correct object
response_text = extract_text_from_response(test_response3)
print(response_text)