import config
from extract.extract_file import ExtractFile
from transform.transform_model_casual import TransformModelCasual
from transform.transform_model_registered import TransformModelRegistered
from transform.transform_processing import TransformProcessing


def main():
    # Load
    load_file: ExtractFile = ExtractFile(config)
    dataset = load_file.load_data(config)

    # Transform
    transform: TransformProcessing = TransformProcessing(config)
    dataset = transform.transform(dataset)

    # Predict
    model_casual: TransformModelCasual = TransformModelCasual(config)
    result = model_casual.predict(dataset)

    print("Casual Model Result:=>")
    print(result)

    model_registered: TransformModelRegistered = TransformModelRegistered(config)
    result = model_registered.predict(dataset)

    print("Registered Model Result:=>")
    print(result)

if __name__ == '__main__':
    main()
