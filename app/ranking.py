import pandas as pd

# Generate feature importance rankings
def generate_ranking(X, y, importances):
    ranking = pd.DataFrame({'Feature': X.columns, 'Importance': importances})
    return ranking.sort_values(by='Importance', ascending=False)
