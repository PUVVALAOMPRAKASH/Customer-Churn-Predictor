from src.data_loader import load_data
from src.preprocessing import preprocess
from src.model import train_and_evaluate
from src.visualize import plot_confusion_matrix

def main():
    data = load_data("data/Churn_Modelling.csv")
    X, y = preprocess(data)
    model, acc, cm, cr = train_and_evaluate(X, y)

    print("Accuracy:", acc)
    print("Classification Report:\n", cr)
    plot_confusion_matrix(cm)

if __name__ == "__main__":
    main()
