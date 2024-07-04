
import base64
import vertexai
import pandas as pd
from vertexai.generative_models import GenerativeModel, Part

def create_model(project, location, model_version):
    """Create a Generative Model instance.

    Args:
        project (str): project id as stated in GCP
        location (str): location of the model
        model_version (str): name of the vertexai model

    Returns:
        GenerativeModel: a Generative Model instance
    """
    vertexai.init(project=project, location=location)
    model = GenerativeModel(model_version)
    return model

def get_file(file_path):
    with open(file_path, "rb") as f:
        encoded_data = base64.b64encode(f.read()).decode("utf-8")
        document = Part.from_data(
            mime_type="application/pdf",
            data=base64.b64decode(encoded_data))

    return document

def generate(complete_prompt, generation_config, model):
    """Generates content using the Vertex AI Generative Models API.

    Args:
        complete_prompt (list): list containing textual prompt and documents
        generation_config (dict): generation configuration
        model (

    Returns:
        : _description_
    """

    response = model.generate_content(
        complete_prompt,
        generation_config=generation_config,
    )

    return response


def get_csv_file(file_path):
    """
    Reads a CSV file, encodes its content to base64, and returns a Part object
    that can be used with Vertex AI Generative Models API.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        Part: A Part object containing the encoded CSV data.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Convert DataFrame to CSV string
    csv_data = df.to_csv(index=False)
    
    # Encode the CSV data to base64
    encoded_data = base64.b64encode(csv_data.encode('utf-8')).decode('utf-8')
    
    # Create a Part object with the encoded CSV data
    document = Part.from_data(
        mime_type="text/csv",
        data=base64.b64decode(encoded_data)
    )
    return document


