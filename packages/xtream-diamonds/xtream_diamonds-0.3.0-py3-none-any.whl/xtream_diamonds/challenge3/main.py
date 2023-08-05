from .dataset_ingestion import ingest
from .dataset_split import split
from .training import train
from .serialization import save
from .evaluation import evaluate
from .configuration import test_size, seed, target
from .cli_arguments import parse_cli_arguments


def main():
    """
    The assignment-train CLI command runs this function:
    - parse the dataset path cli argument
    - cleans the dataset
    - splits the dataset
    - trains the model on the training set
    - evaluates the model on the test set
    - saves the model as a json file 'model.json'
    - prints the model score on the test set to the standard output
    Warning: this function may take several minutes to execute (~ 3 minutes on AMD Ryzen 7 PRO 6850U)
    """
    dataset_path = parse_cli_arguments()

    dataset = ingest(dataset_path)

    samples_train, targets_train, samples_test, targets_test = split(
        dataset, target, test_size, seed
    )

    model = train(samples_train, targets_train, seed)

    score = evaluate(model, samples_test, targets_test)

    save(model, "./model.json")

    print("Model score: " + str(score))
