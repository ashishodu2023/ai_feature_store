# Importing from the ai-feature-store package
from ai_feature_store.app.data_ingestion import load_data
from ai_feature_store.app.models import rank_features
from ai_feature_store.app.api import app
from uvicorn import run

# Example: Load data and rank features
def main():
    print("Loading data...")
    data = load_data()
    print("Data loaded successfully:")
    print(data.head())

    # Splitting features and target
    X, y = data.iloc[:, :-1], data['target']
    
    print("\nRanking features...") 
    feature_ranking = rank_features(X, y)
    print("Feature ranking completed:")
    print(feature_ranking)

    # Running the FastAPI server
    print("\nStarting FastAPI server...")
    run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()