from eazieda import __version__
from eazieda import histograms

df = data.iris()
features = df.columns
plot = histograms(df, features, plot_width=100, plot_height=100, num_cols=2)


def test_version():
    assert __version__ == "0.1.0"


def test_histograms():
    assert (
        histograms(
            df,
            ["petals_misspelt"],
            plot_width=100,
            plot_height=100,
            num_cols=2,
        )
        == Exception("All features must be present in dataframe")
    )

    assert (
        histograms(
            df,
            ["petalLength"],
            plot_width="100",
            plot_height=100,
            num_cols=2,
        )
        == Exception("plot_width and plot_height must be numeric")
    )

    pd.testing.assert_frame_equal(df, plot.data)
