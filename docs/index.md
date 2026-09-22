# mypackage

> Descriptive statistics, smoothing filters, and composable transforms for
> one-dimensional numeric series — with zero runtime dependencies.

`mypackage` is the worked example that ships with this project template. It is
small enough to read in one sitting and complete enough that every tool in the
template has something real to chew on: `mkdocstrings` renders its docstrings,
`ty` checks its annotations, `pytest` exercises its branches, and every
`Examples:` block on this site is executed on each test run.

!!! tip "Using this as a template"
    Replace `mypackage` with your own package and delete what you don't need.
    The point of keeping a real library here is that the docs build, the API
    reference, the notebooks, and the coverage gate all start out *working* —
    so when they break, it's because of something you changed.

## Installation

=== "uv"

    ```bash
    uv add mypackage
    ```

=== "pip"

    ```bash
    pip install mypackage
    ```

=== "From source"

    ```bash
    git clone https://github.com/jejjohnson/pypackage_template.git
    cd pypackage_template
    make install
    ```

## Quickstart

```python
import mypackage as mp

series = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]

summary = mp.summarize(series)
print(summary.mean, summary.std)     # 5.0 2.138...

smoothed = mp.moving_average(series, window=3)
pipeline = mp.chain(mp.Standardize(), mp.Clip(-2.0, 2.0))
scaled = pipeline.fit_apply(series)
```

Or from the shell:

```bash
echo "2 4 4 4 5 5 7 9" | mypackage summarize - --json
```

## The three layers

<div class="grid cards" markdown>

- :material-chart-box: **Statistics**

    Batch summaries and a streaming accumulator.
    [`summarize`][mypackage.summarize] · [`quantile`][mypackage.quantile] ·
    [`zscores`][mypackage.zscores] ·
    [`RunningStats`][mypackage.RunningStats]

    [:octicons-arrow-right-24: Statistics guide](guide/statistics.md)

- :material-chart-bell-curve: **Smoothing**

    Linear and non-linear filters with explicit boundary handling.
    [`moving_average`][mypackage.moving_average] ·
    [`exponential_moving_average`][mypackage.exponential_moving_average] ·
    [`median_filter`][mypackage.median_filter]

    [:octicons-arrow-right-24: Smoothing guide](guide/smoothing.md)

- :material-pipe: **Transforms**

    A fit/apply lifecycle with structural typing.
    [`Standardize`][mypackage.Standardize] ·
    [`MinMaxScale`][mypackage.MinMaxScale] · [`Clip`][mypackage.Clip] ·
    [`Pipeline`][mypackage.Pipeline]

    [:octicons-arrow-right-24: Transforms guide](guide/transforms.md)

</div>

## Design rules

The library follows four rules, and the test suite enforces all of them:

1. **Pure where possible.** Every function returns a new list and never
   mutates its input. Stateful objects confine their state to a `fit` step.
2. **Validate once, at the boundary.** Public entry points coerce and check
   their inputs through [`as_floats`][mypackage.as_floats] and friends, so
   internal helpers can assume well-formed data.
3. **Fail with a typed exception.** Everything raised derives from
   [`MypackageError`][mypackage.MypackageError] *and* from the closest
   standard-library exception, so `except ValueError` still works.
4. **Structural, not nominal, typing.** [`Pipeline`][mypackage.Pipeline]
   accepts anything with an `apply` method — no base class, no registry.

## Where to go next

| I want to… | Start here |
|---|---|
| See it all in 5 minutes | [Quickstart](guide/quickstart.md) |
| Understand the filters | [Smoothing](guide/smoothing.md) |
| Build my own transform | [Transforms](guide/transforms.md) |
| Use it from the shell | [CLI](guide/cli.md) |
| Read the full API | [API Reference](api/reference.md) |
| Run an executable example | [Quickstart notebook](notebooks/quickstart.ipynb) |
