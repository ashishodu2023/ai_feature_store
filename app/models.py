import torch
import torch.nn as nn
from sklearn.ensemble import GradientBoostingClassifier

# Autoencoder definition
class Autoencoder(nn.Module):
    def __init__(self, input_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, input_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

# Gradient Boosted Classifier for feature ranking
def rank_features(X, y):
    gbc = GradientBoostingClassifier()
    gbc.fit(X, y)
    return gbc.feature_importances_
