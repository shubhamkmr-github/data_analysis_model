from csv_handler import read_csv
from statistics import calculate_statistics
from visualization import plot_histogram, plot_scatter, plot_line
from llm_integration import ask_llm

def main():
    file_path = input("Enter the path to the CSV file: ")
    data = read_csv(file_path)
    
    if data is not None:
        print("Data loaded successfully.")
        
        stats = calculate_statistics(data)
        print("Statistical Analysis:")
        for key, value in stats.items():
            print(f"{key.capitalize()}: {value}")
        
        plot_histogram(data, data.columns[0])
        plot_scatter(data, data.columns[0], data.columns[1])
        plot_line(data, data.columns[0])
        
        question = input("Ask a question about the data: ")
        answer = ask_llm(question)
        print(f"LLM Answer: {answer}")
    else:
        print("Failed to load data.")

if __name__ == "__main__":
    main()
