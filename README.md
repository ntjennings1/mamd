# MAMD

A Maritime AI model dashboard

## Software Requirements
```
- Python 3.13.0
- Cuda 12.4.1
- CudNN 9.21.1
- Dot 14.1.5
```

### Dot (pydot)

Dot is a tool in the Graphviz suite, optimized for rendering directed graphs with clear node and edge relationships. MAMD uses the dot framework to display a graphical representation of neural networks being tested.

#### Windows

On Windows machines, please use the [Graphviz Offical Site](https://graphviz.org/download/) to download and install Graphviz and all available tools.

#### Linux

For Linux machines, use the following command with sudo priviledges to install graphviz:
```
sudo apt install graphviz -y
```

Then verify the installation with these commands:
```
which dot
dot --version
```

## Usage

After satisfying initial requirements, it is recommend that Linux users use a virtual environment and Windows users stay in their base environment. Create a linux environment with the following command:
```
python -m venv venv
```

Then, users can boot the Maritime AI Model Dashboard with this command: 
```
python src\main.py
```

_*MAMD is currently limited to evaluating ONNX models.*_

## Troubleshooting

You may experience runtime errors.

### Packages

When using MAMD, users may experience missing or misconfigured packages. Software requirements must be installed by hand; however, in the event a package throws an error during installation, you should check these attributes on your device:
```
- Internet connectivity
- Remaining memory space
- CPU specifications
- GPU specifications
```

In the event a package throws an error during use, you should either install the package like this:
```
pip install xxxx
```

or simply reinstall the package like so:
```
pip install --upgrade --force-reinstall xxxx
```

_*Replace xxxx with the package in question.*_

#### Command culprits
```
dot
pydot
onnx
onnxruntime-gpu
```

### Environment Variables

Some dependencies require you to manipulate your systems environment variables. Please make sure you are using our designated Windows/Linux instructions depending on your machine.


## Acknowledgements

```
Noah Jennings
    njenn001@odu.edu
    Old Dominion University

Joseph McGee
    jmcge010@odu.edu
    Old Dominion University

Shoba Vatsa
    svatsa@odu.edu
    Old Dominion University

srip
    Flaticon
```