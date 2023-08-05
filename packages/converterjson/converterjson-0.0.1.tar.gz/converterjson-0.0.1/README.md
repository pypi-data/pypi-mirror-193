# Python packaging tutorial with an over-simplified converter

This is an over-simplified package just to convert json format to hierarchical tree Image.
It contains a python module to import and a CLI tool.

## Installation

You can easily install the module using `pip`.

## Using the Python module

Once installed, in your python script:

```
from converterJson import converter.
# "file_path" variable points to a path where the resource
# is to be stored.
 if parent_id is None:
        graph.node(str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color, shape=shape)
    else:
        graph.node(str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color, shape=shape)
        graph.edge(str(parent_id), str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color,
                   shape=shape)

    if "child" in json_data:
        for node in json_data["child"]:
            plot_hierarchy(node, graph, parent_id=json_data["nodeId"])

graph=plot_hierarchy(file_path)
#it will plot the graph (used recursion method)

graph. Render("sample.png")
#output Image generated in output dirctory same location
```

