from extractors.models import Models
from extractors.general_extractors.extractor import Extractor
import PyPDF2
from langchain_core.prompts import PromptTemplate
import os

class WamDerivatiRettifiche(Extractor):


    def __init__(self, doc_path, predefined_language='it'):
        self.tenant = "wamderivati"
        self.extractor = "rettifichebi"
        super().__init__(doc_path, predefined_language, tenant=self.tenant, extractor=self.extractor)
    
    
    def extract_text_from_pdf_selected_pages(self, pdf_path,page_from, page_to):
        text = ""

        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            page_from = max(1, page_from)
            page_to = min(len(pdf_reader.pages), page_to)

            for page_number in range(page_from-1, page_to):
                page = pdf_reader.pages[page_number]
                if page.extract_text() is not None:
                    text += page.extract_text()
                else:
                    text += ' '  # Aggiungi uno spazio se non c'è testo in una pagina
        return text


    def process(self):

        # Create prompt
        system_message = self.extraction_config["prompt"]["rettifichebi_system"]
        human_message =  self.extraction_config["prompt"]["rettifichebi_human"]
        complete_prompt = system_message + human_message
        prompt_kid = PromptTemplate(input_variables=["input"], template=complete_prompt)

        # Get response and tag
        response = Models.general_extract(self.file_id, "gpt-4-turbo", prompt=prompt_kid, input=self.text[1])
        rettifichebi_schema = self.extraction_config["tag"]["rettifichebi"]
        tags  = Models.tag(response, rettifichebi_schema, self.file_id)

        api_costs = self._process_costs()

        filename = os.path.splitext(os.path.basename(self.doc_path))[0]
        complete_results  = {
                "file_name": filename,
                **dict(tags),
                "api_costs": api_costs
            }

        formatted_output = self.create_output(complete_results)

        Models.clear_resources_file(filename)


        return formatted_output

