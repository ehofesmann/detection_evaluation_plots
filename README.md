# Detection Evaluation Plots

Visualization of object detection evaluation plots in a FiftyOne App panel




https://github.com/ehofesmann/detection_evaluation_plots/assets/21222883/9337422c-31cc-479f-9b07-2a7d7235cab4



## Installation

This plugin requires `https://github.com/ehofesmann/plotly_panel` installed.

```shell
fiftyone plugins download https://github.com/ehofesmann/plotly_panel
fiftyone plugins download https://github.com/ehofesmann/detection_evaluation_plots
```

Refer to the [main README](https://github.com/voxel51/fiftyone-plugins) for
more information about managing downloaded plugins and developing plugins
locally.

## Run Example

After installing this plugin, you can try the example panel yourself on the `quickstart` dataset.
```python
import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")
results = dataset.evaluate_detections("predictions", gt_field="ground_truth", compute_mAP=True, eval_key="eval")
session = fo.launch_app(dataset)
```
