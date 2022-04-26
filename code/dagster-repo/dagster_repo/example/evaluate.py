from dagster import Nothing, op
from sklearn.ensemble import RandomForestClassifier


@op
def evaluate_rfc(context, data_dict: dict, rfc: RandomForestClassifier) -> Nothing:
    test_score = rfc.score(data_dict["test_x"], data_dict["test_y"])
    context.log.info(
        f"The mean accuracy on the given test data and labels is {test_score}."
    )
