import fiftyone.operators as foo
import fiftyone.operators.types as types

from . import custom_plots


class GetPlotlyPlots(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="get_plotly_plots",
            label="Get serialized plotly plots",
            unlisted=True,
        )

    def execute(self, ctx):
        if ctx.dataset.view() == ctx.view:
            samples = ctx.dataset
        else:
            samples = ctx.view
        plots = custom_plots.get_figures(samples)
        ctx.trigger(
            "@ehofesmann/plotly_panel/update_plots",
            params=dict(plots=[plot.to_json() for plot in plots]),
        )


class OpenPlotlyPanel(foo.Operator):
    @property
    def config(self):
        return foo.OperatorConfig(
            name="open_plotly_panel",
            label="Open Plotly panel for %s" % self.plugin_name,
        )

    def resolve_placement(self, ctx):
        if self.plugin_name == "@ehofesmann/plotly_panel":
            if ctx.dataset.name != "quickstart":
                return None
        try:
            button = custom_plots.get_button()
        except:
            button = None

        if button is None:
            types.Button(
                label="Open plot panel",
                prompt=False,
            ),
        return types.Placement(
            types.Places.SAMPLES_GRID_SECONDARY_ACTIONS,
            button,
        )

    def execute(self, ctx):
        ctx.trigger(
            "@ehofesmann/plotly_panel/initial_setup",
            params=dict(
                plot_operator=f"{self.plugin_name}/get_plotly_plots",
            ),
        )
        ctx.trigger(
            "open_panel",
            params=dict(
                name="PlotlyPanel", isActive=True, layout="horizontal"
            ),
        )


def register(p):
    p.register(GetPlotlyPlots)
    p.register(OpenPlotlyPanel)
