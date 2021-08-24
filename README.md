# nitk-nest-experiments


#Comparison Plots for Fq-CoDel and Fq-Pie

# Nest tests on Dumbell Topology

## Requirements Setup

* nitk-nest
* gnuplot

bash
python3 -m pip install nitk-nest

sudo apt-get update
sudo apt-get install gnuplot


## Usage

- All *Bold* variable names are configurable network parameters

bash
sudo python3 TCP_flow.py


- Use the following optional command line arguments 
bash
sudo python3 TCP_flow.py <num_of_left_nodes> <num_of_right_nodes> <bottleneck-delay> <bottleneck-bandwidth> <edge-delay> <edge-bandwidth> <qdisc>


## Notes
- `FQ_PIE` AQM support in *iproute2* was added from version 5.5.
- To install iproute2 with fq_pie support (e.g: v5.7)

bash
wget http://in.archive.ubuntu.com/ubuntu/pool/main/i/iproute2/iproute2_5.7.0-1ubuntu1_amd64.deb
sudo apt install ./iproute2_5.7.0-1ubuntu1_amd64.deb

## To generate gnuplots:

- convert the json files obtained by running the above command to csv files using the .py files

python3 <filename>.py

- plot the comparison graphs for a particualr parameter using gnuplot through the csv files

gnuplot <parameter_name>.plt

