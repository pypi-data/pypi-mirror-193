# circuitsim

A simple CLI electronic circuit simulator for AC and DC linear circuits.

## Installation

```shell
pip install circuitsim_janq0
```

## Usage

Run circuitsim using the `python -m circuitsim_janq0` command.
Read about all the command line options using the `-h` flag.

The netlist file should contain a newline-separated list of components.
Each line should contain a space-separated list of keywords.
The first keyword always denotes the type of component and the remaining keywords are the arguments to that component.
Below are all the supported components with their arguments.
If an argument is enclosed in parenthesis, it means that it's optional.

```
U voltage pos_node neg_node branch
I current pos_node neg_node (branch)
R resistance pos_node neg_node (branch)
L inductance pos_node neg_node (branch)
C capacitance pos_node neg_node (branch)
```