import asyncio
from llama_parse import LlamaParse

# Initialize the parser
parser = LlamaParse(
    api_key="llx-CL0JMQdc01kXPHUkb9cX2xbGtTck8dqvzbKFInYXQMY6sVB0",  # Replace with your actual API key
    result_type="text",  # Use "text" for easier processing
    num_workers=1,  # Number of workers for batch processing
    verbose=True,
    language="it"  # Assuming the document is in Italian
)

async def parse_entire_document_async(pdf_path):
    """Asynchronously parse the entire PDF."""
    documents = await parser.aload_data(pdf_path)
    return documents if documents else []

def parse_entire_document_sync(pdf_path):
    """Synchronously parse the entire PDF."""
    documents = parser.load_data(pdf_path)
    return documents if documents else []

def extract_second_page_text(document_text):
    """Extract text from the second page of the document."""
    # Split the document text into pages assuming page breaks
    pages = document_text.split('\f')
    print(f"Debug: Number of pages found: {len(pages)}")  # Debug point
    if len(pages) > 1:
        print(f"Debug: Extracted text from second page:\n{pages[1][:1000]}...")  # Debug point
        return pages[1]
    else:
        return "Second page not found or the document has only one page."

def main_sync(pdf_path):
    """Main function for synchronous parsing and printing the second page."""
    extracted_documents = parse_entire_document_sync(pdf_path)
    print(f"Debug: Extracted Documents: {extracted_documents}")  # Debug point
    if extracted_documents:
        document_text = extracted_documents[0].text
        print(f"Debug: Full document text:\n{document_text[:1000]}...")  # Debug point
        extracted_text = extract_second_page_text(document_text)
        print("Extracted Text from Page 2:", extracted_text)
    else:
        print("No text extracted")

async def main_async(pdf_path):
    """Main function for asynchronous parsing and printing the second page."""
    extracted_documents = await parse_entire_document_async(pdf_path)
    print(f"Debug: Extracted Documents: {extracted_documents}")  # Debug point
    if extracted_documents:
        document_text = extracted_documents[0].text
        print(f"Debug: Full document text:\n{document_text[:1000]}...")  # Debug point
        extracted_text = extract_second_page_text(document_text)
        print("Extracted Text from Page 2:", extracted_text)
    else:
        print("No text extracted")

if __name__ == "__main__":
    pdf_path = "C:/Users/ribhu.kaul/RibhuLLM/Extraction_Program/Latest_Extraction/GeminiBased_PerformanceScenario_Extraction/input_tester/202302_MULTI-OBIETTIVO CRESCITA_Vera financial Multi - Obiettivo Personal.pdf"
    
    # Run synchronous parsing and extraction
    print("Running synchronous extraction...")
    main_sync(pdf_path)

    # Run asynchronous parsing and extraction
    print("Running asynchronous extraction...")
    asyncio.run(main_async(pdf_path))
