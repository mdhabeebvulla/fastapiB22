from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from processing.features import FeatureTransformer
from config.core import config

def create_pipeline():
    pipeline = Pipeline([
    ('feature_transformation',FeatureTransformer()),
    ('scaler',StandardScaler()),
    ('classifier',RandomForestClassifier(random_state=config.get('random_state')))
    ])
    return pipeline