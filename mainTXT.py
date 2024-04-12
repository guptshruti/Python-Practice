import difflib
import matplotlib.pyplot as plt
import docx

# Function to read text from .txt file
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to read text from .docx file
def read_docx_file(file_path):
    doc = docx.Document(file_path)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)

# Calculate error rates
def calculate_error_rates(reference_text, ocr_text):
    # Calculate similarity between reference text and OCR text
    similarity = difflib.SequenceMatcher(None, reference_text, ocr_text)

    # Calculate Word Error Rate (WER)
    wer = 1 - similarity.ratio()

    # Calculate Character Error Rate (CER)
    cer = sum([1 for ref, ocr in zip(reference_text, ocr_text) if ref != ocr]) / len(reference_text)
    
    return wer, cer

# Automate comparison
def automate_comparison(reference_files, ocr_files, file_type='txt'):
    results = []
    
    # Read texts from files based on file type
    if file_type == 'txt':
        read_file = read_txt_file
    elif file_type == 'docx':
        read_file = read_docx_file
    
    for ref_file, ocr_file in zip(reference_files, ocr_files):
        # Read texts from files
        reference_text = read_file(ref_file)
        ocr_text = read_file(ocr_file)
        
        # Calculate error rates
        wer, cer = calculate_error_rates(reference_text, ocr_text)
        results.append((wer, cer))
    return results

# Visualize results
def visualize_results(results, model_names):
    # Unpack results
    wer_results, cer_results = zip(*results)
    
    # Create a figure
    plt.figure()
    
    # Plot Word Error Rate (WER)
    plt.bar(model_names, wer_results, alpha=0.6, label='WER')
    
    # Plot Character Error Rate (CER)
    plt.bar(model_names, cer_results, alpha=0.6, label='CER')
    
    # Add labels and title
    plt.xlabel('Model')
    plt.ylabel('Error Rate')
    plt.title('Word and Character Error Rates for OCR Models')
    plt.legend()
    
    # Show the plot
    plt.show()

# Main function
def main():
    # Define file paths for reference texts and OCR outputs for each model
    reference_files = ['reference_text_1.txt', 'reference_text_2.docx', ...]
    ocr_files_bhashini = ['ocr_text_bhashini_1.txt', 'ocr_text_bhashini_2.docx', ...]
    ocr_files_iiith = ['ocr_text_iiith_1.txt', 'ocr_text_iiith_2.docx', ...]
    ocr_files_tesseract = ['ocr_text_tesseract_1.txt', 'ocr_text_tesseract_2.docx', ...]

    # Define model names for visualization
    model_names = ['Bhashini OCR', 'IIITH OCR', 'Tesseract OCR']
    
    # Calculate error rates for each model
    results_bhashini = automate_comparison(reference_files, ocr_files_bhashini, file_type='txt')
    results_iiith = automate_comparison(reference_files, ocr_files_iiith, file_type='docx')
    results_tesseract = automate_comparison(reference_files, ocr_files_tesseract, file_type='txt')
    
    # Combine results for visualization
    all_results = [results_bhashini, results_iiith, results_tesseract]
    
    # Visualize the results
    visualize_results(all_results, model_names)

if you have any additional questions or concerns, please let me know.
