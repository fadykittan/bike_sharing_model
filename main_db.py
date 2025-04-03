import config
from extract.extract_db import ExtractDB
from load.load_result_db import LoadResultDB
from transform.transform_model_casual import TransformModelCasual
from transform.transform_model_registered import TransformModelRegistered
from transform.transform_processing import TransformProcessing


def main():
    # Load
    load_file: ExtractDB = ExtractDB(config)
    dataset = load_file.load_data(config)

    # Transform
    transform: TransformProcessing = TransformProcessing(config)
    dataset = transform.transform(dataset)

    # Predict
    model_casual: TransformModelCasual = TransformModelCasual(config)
    result_casual = model_casual.predict(dataset)

    print("Casual Model Result:=>")
    print(result_casual)

    model_registered: TransformModelRegistered = TransformModelRegistered(config)
    result_registered = model_registered.predict(dataset)

    print("Registered Model Result:=>")
    print(result_registered)

    # Load Result
    load_file: LoadResultDB = LoadResultDB(config)
    load_file.save(result_casual, config.OUTPUT_FILE_NAME_CASUAL)
    load_file.save(result_registered, config.OUTPUT_FILE_NAME_REGISTERED)

if __name__ == '__main__':
    main()
