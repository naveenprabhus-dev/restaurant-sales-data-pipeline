from clean import clean_data
from transform import transform_data
from feature_engineering import engineer_features
from validate import validate_data

def run_pipeline():
    print("Starting Restaurant Sales ETL Pipeline...\n")
    print("---Cleaning---\n")
    clean_data()

    print("\n---Transformation---\n")
    transform_data()

    print("\n---Feature Engnineering---\n")
    engineer_features()

    print("\n---Final Validation---\n")
    validate_data()

    print("----ETL Pipeline completed successfully----")
if __name__=="__main__":
    run_pipeline()