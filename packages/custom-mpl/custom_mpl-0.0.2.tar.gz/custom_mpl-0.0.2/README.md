# <b>Custom Matplotlib Stylesheets</b>
This repository contains a collection of custom stylesheets for Matplotlib, a powerful visualization library in Python.

The stylesheets in this repository are designed to provide a consistent and professional look to your Matplotlib visualizations. Each stylesheet is optimized for a different use case, so you can choose the one that best fits your needs.

## <b>Stylesheets</b>
<br>
Here are the stylesheets currently included in this repository:

* `powerbi.mplstyle`: This style is optimized for use with Power BI visualizations, and contains colors related to Shell company colors.
* `powerbi_dark.mplstyle`: This style is optimized for use with Power BI visualizations with a dark background, and also contains colors related to Shell company colors.

## <b>How to Use</b>
<br>
To use either of these stylesheets, copy them into your working directory or a directory in your Matplotlib style path. You can then use the plt.style.use() function to apply the style to your plots.

For example, to use the `powerbi.mplstyle` stylesheet, you would use the following code:

```python
import custom_mpl
import matplotlib.pyplot as plt

plt.style.use('custom_mpl.powerbi')
```
To use the `powerbi_dark.mplstyle` stylesheet, you would use the following code:

```python
import custom_mpl
import matplotlib.pyplot as plt

plt.style.use('custom_mpl.powerbi_dark')
```

## <b>Contributing</b>
Contributions to this repository are welcome. If you have a new style to add or an improvement to an existing style, please feel free to submit a pull request.

Please ensure that your style follows the same format as the existing stylesheets and that it has a descriptive name that accurately reflects its use case.

## <b>License</b>
This repository is licensed under the MIT License.