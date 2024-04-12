import difflib
import matplotlib.pyplot as plt

# Function to read text from .txt file
def read_txt_file(file_path):
    """Read the content of a .txt file and return it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Calculate error rates
def calculate_error_rates(reference_text, ocr_text):
    """Calculate error rates between reference text and OCR text."""
    # Calculate similarity between reference text and OCR text
    similarity = difflib.SequenceMatcher(None, reference_text, ocr_text)
    
    # Calculate Word Error Rate (WER)
    wer = 1 - similarity.ratio()
    
    # Calculate Character Error Rate (CER)
    cer = sum(1 for ref, ocr in zip(reference_text, ocr_text) if ref != ocr) / len(reference_text)
    
    return wer, cer

# Automate comparison
def automate_comparison(reference_files, ocr_files):
    """Compare reference and OCR files and calculate error rates."""
    results = []
    for ref_file, ocr_file in zip(reference_files, ocr_files):
        # Read texts from files
        reference_text = read_txt_file(ref_file)
        ocr_text = read_txt_file(ocr_file)
        
        # Calculate error rates
        wer, cer = calculate_error_rates(reference_text, ocr_text)
        results.append((wer, cer))
    return results

# Visualize results
def visualize_results(results, model_names):
    """Visualize error rates for different OCR models."""
    # Unpack results
    wer_results, cer_results = zip(*results)
    
    # Create a figure
    plt.figure()
    
    bar_width= 0.35
    x= range(len(model_names))
    
    plt.bar(x, wer_results, width=bar_width, alpha=0.6, label='WER', color='b')
    plt.bar([i + bar_width for i in x], cer_results, width=bar_width, alpha=0.6, label='CER', color='r')
    
    # Plot Word Error Rate (WER)
    #plt.bar(model_names, wer_results, alpha=0.6, label='WER')
    
    # Plot Character Error Rate (CER)
    #plt.bar(model_names, cer_results, alpha=0.6, label='CER')
    
    # Add labels and title
    plt.xlabel('Model')
    plt.ylabel('Error Rate')
    plt.title('OCR Models for Source Language Hindi')
    plt.legend()
    
    plt.xticks([i + bar_width / 2 for i in x], model_names)
    
    # Show the plot
    plt.show()

# Main function
def main():
    # Define file paths for reference texts and OCR outputs for each model
    reference_files = [r"C:\Users\shrutigupta15\Desktop\TestFilesOCR\ReferenceText.txt"]
    ocr_files_bhashini = [r"C:\Users\shrutigupta15\Desktop\TestFilesOCR\Bhashini_OCR_Hindi.txt"]
    ocr_files_iiith = [r"C:\Users\shrutigupta15\Desktop\TestFilesOCR\IIITH_OCR_Hindi.txt"]
    ocr_files_tesseract = [r"C:\Users\shrutigupta15\Desktop\TestFilesOCR\Tesseract_OCR_Hindi.txt"]
    
    # Define model names for visualization
    model_names = ['Bhashini OCR', 'IIITH OCR', 'Tesseract OCR']
    
    # Calculate error rates for each model
    results_bhashini = automate_comparison(reference_files, ocr_files_bhashini)
    results_iiith = automate_comparison(reference_files, ocr_files_iiith)
    results_tesseract = automate_comparison(reference_files, ocr_files_tesseract)
    
    # Combine results for visualization
    all_results = [results_bhashini[0], results_iiith[0], results_tesseract[0]]
    
    # Visualize the results
    visualize_results(all_results, model_names)

if __name__ == "__main__":
    main()
