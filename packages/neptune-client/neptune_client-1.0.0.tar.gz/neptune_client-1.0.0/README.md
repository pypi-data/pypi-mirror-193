<div align="center">
    <img src="https://raw.githubusercontent.com/neptune-ai/neptune-client/assets/readme/github-banner.jpeg" width="1500" />
    &nbsp;
 <h1>neptune.ai</h1>
</div>

<div align="center">
  <a href="https://docs.neptune.ai/usage/quickstart/">Quickstart</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://neptune.ai/">Website</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://docs.neptune.ai/">Docs</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://github.com/neptune-ai/examples">Examples</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://neptune.ai/resources">Resource center</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://neptune.ai/blog">Blog</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://neptune.ai/events">Podcast</a>
&nbsp;
  <hr />
</div>

## ⚠️ This package has been renamed to [`neptune`](https://pypi.org/project/neptune)

With the `1.0` release of the Neptune client library, we changed the package name from `neptune-client` to `neptune`.

To upgrade your Neptune client from `0.x` to `1.x`:

```
pip uninstall neptune-client
```

```
pip install neptune
```

The neptune `1.0.0` release comes with numerous updates, notably:

- The `neptune.new` package is now just `neptune`.
- We tweaked the monitoring of system metrics and hardware consumption:
    - Better support for multi-process jobs.
    - Disabled by default if you start Neptune in an interactive session.
- Initialization and project management functions take keyword arguments instead of positional ones.
- Run states are changed to `"inactive"` and `"active"` instead of `"idle"` and `"running"`.
- If you attempt to log unsupported types, they're no longer implicitly cast to `string`. We offer utilities and workarounds for types that are not yet directly supported.

For the full list of changes, see the [neptune 1.0.0 upgrade guide](https://docs.neptune.ai/setup/neptune-client_1-0_release_changes).
