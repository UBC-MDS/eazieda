from eazieda import __version__
from eazieda.histograms import histograms
from vega_datasets import data
import pandas as pd
from pytest import raises

df = data.iris()
# Due to Altair bug, need to resample data for second Facet chart for it to not break.
df_sample = df.sample(df.shape[0], random_state=42)
features = df.columns
plot = histograms(df, features, plot_width=100, plot_height=100, num_cols=2)


def test_version():
    assert __version__ == "0.1.0"


def test_histograms_exceptions():
    with raises(ValueError):
        histograms(
            df,
            ["petals_misspelt"],
            plot_width=100,
            plot_height=100,
            num_cols=2,
        )
    with raises(ValueError):
        histograms(
            df,
            ["petalLength"],
            plot_width="100",
            plot_height=100,
            num_cols=2,
        )
    with raises(ValueError):
        histograms(
            df,
            ["petalLength"],
            plot_width=100,
            plot_height="100",
            num_cols=2,
        )


def test_histograms_data():
    chart_data = list(plot.to_dict()["datasets"].values())
    pd.testing.assert_frame_equal(df, pd.DataFrame(chart_data[0]))
    pd.testing.assert_frame_equal(
        df_sample.reset_index(drop=True), pd.DataFrame(chart_data[1])
    )
