import fiftyone.operators.types as types
from fiftyone import ViewField as F
import fiftyone.utils.random as four

import plotly.express as px
import plotly.graph_objects as go


def get_button():
    # Return a FiftyOne operator placement Button oncluding the text and optional SVG to open your panel
    return types.Button(
        label="Evaluation plots",
        prompt=False,
    )


def get_figures(samples):
    # Return a list of plotly express or plotly graph_objects figures
    figures = []
    figures = add_confusion_matrix(figures, samples)
    figures = add_pr_curves(figures, samples)
    #figures = add_eval_table(figures, samples)

    return figures


def add_confusion_matrix(figures, samples):
    evaluations = samples.list_evaluations()
    if evaluations:
        eval_key = evaluations[0]
        results = samples.load_evaluation_results(eval_key)
        # The top-10 most common classes
        counts = samples.count_values("ground_truth.detections.label")
        classes = sorted(counts, key=counts.get, reverse=True)[:10]
        fig = results.plot_confusion_matrix(classes=classes)._figure
        figures.append(fig)
    return figures


def add_pr_curves(figures, samples):
    evaluations = samples.list_evaluations()
    if evaluations:
        eval_key = evaluations[0]
        results = samples.load_evaluation_results(eval_key)
        counts = samples.count_values("ground_truth.detections.label")
        classes = sorted(counts, key=counts.get, reverse=True)[:10]
        fig = results.plot_pr_curves(classes=classes)
        figures.append(fig)
    return figures


if __name__ == "__main__":
    import fiftyone.zoo as foz

    dataset = foz.load_zoo_dataset("quickstart")
    if not dataset.list_evaluations():
        dataset.evaluate_detections("predictions", eval_key="eval", compute_mAP=True)
        dataset.persistent = True
    figs = get_figures(dataset)
    for fig in figs:
        fig.show()
