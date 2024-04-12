import matplotlib.pyplot as plt

def read_text(file_path):
    """Reads text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_accuracy(reference_text, ocr_text):
    """Calculates character-level accuracy and error rate."""
    if len(reference_text) != len(ocr_text):
        raise ValueError("Reference and OCR text must have the same length for comparison.")

    correct_count = sum(1 for ref, ocr in zip(reference_text, ocr_text) if ref == ocr)
    total_count = len(reference_text)
    
    accuracy = correct_count / total_count
    error_rate = 1 - accuracy
    
    return accuracy, error_rate

def visualize_results(accuracy, error_rate):
    """Visualizes accuracy and error rate using a bar chart."""
    labels = ['Accuracy', 'Error Rate']
    values = [accuracy, error_rate]
    
    plt.bar(labels, values, color=['green', 'red'])
    plt.ylabel('Percentage')
    plt.title('OCR Performance Metrics')
    plt.show()

def main():
    # Specify file paths for reference and OCR text files
    reference_file_path = 'reference_text.txt'
    ocr_file_path = 'ocr_text.txt'
    
    # Read texts from files
    reference_text = read_text(reference_file_path)
    ocr_text = read_text(ocr_file_path)
    
    # Calculate accuracy and error rate
    accuracy, error_rate = calculate_accuracy(reference_text, ocr_text)
    
    # Print results
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Error Rate: {error_rate * 100:.2f}%")
    
    # Visualize results
    visualize_results(accuracy, error_rate)

if __name__ == '__main__':
    main()
