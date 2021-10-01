# NeST-fq-comparisons

## Requirements Setup
* nitk-nest

```bash
python3 -m pip install nitk-nest
```

* gnuplot

```bash
sudo apt-get update
sudo apt-get install gnuplot
```

* numpy
Install via pip:

```bash
pip install numpy
```



## Steps to use the script:
1. Clone the official git repository::

    $ git clone https://gitlab.com/nitk-nest/nest.git

2. Install NeST via pip in editable mode:

    $ python3 -m pip install -e .

3. Install iproute2 (version >= 5.5) and apply the custom flent patches as mentioned [here](./misc_patch_scripts/README.md)    

3. Download the 'fq-comparison.py' file.

4. To run the file with default argument, please use the following command:
```bash
sudo python3 ..........
```

## Parameters:
<<<<<<< HEAD
1. **bottleneckQueueType:** The Queue type used ("fq_codel" / "fq_pie" / "cake") [fq_pie].
=======
1. **bottleneckQueueType:** The Queue type used ("fq_codel" / "fq_pie" / "cake") [fqPie].
>>>>>>> 0bd097f28a2c6c9798114c612101e2bde9225cfb
2. **bottleneckDelay:** The delay on the bottleneck link ("Xms", where is X is the delay in milliseconds) [20ms].
3. **linkDelay:** The delay on the edge links ("Xms", where X is the delay in milliseconds) [10ms].
4. **bottleneckRate:** Data rate of bottleneck link ("XMbps", where X is the data rate in Mbps) [10Mbps].
5. **linkrate:** Data rate of edge link  ("XMbps", where X is the bandwidth in Mbps) [100Mbps].
6. **useEcn:** Boolean indicating whether ECN should be enabled or disabled ("true" / "false") [true].
7. **useOffload:** Boolean indicating whether Offload should be enabled or disabled ("true" / "false") [false].
8. **stopTime:** The duration of the experiment ("Xs", where X is the time in seconds) [70s].

## Generating a plot:
The steps to generate a plot using plotter-gnu is given below:
Assume we want to compare the following 3 dat files in a single graph: 
1. fqCodel_1_80Mbps_80ms_ECNEn_BQLDis/
2. fqPie_1_80Mbps_80ms_ECNEn_BQLDis/mark.dat
3. fqCobalt_1_80Mbps_80ms_ECNEn_BQLDis/mark.dat

In such a case we would have to run the following. Notice that we are running this command in a folder that contains all the three folders (fqCodel_1_80Mbps_80ms_EcnEn_OFLDis/, fqPie_1_80Mbps_80ms_ECNEn_OFLDis/, fqCobalt_1_80Mbps_80ms_ECNEn_OFLDis/). If you run from elsewhere, please adjust the paths accordingly when you run.

```bash
gnuplot -e "files = 'fqCodel_1_80Mbps_80ms_ECNEn_OFLDis/cwnd.dat fqPie_1_80Mbps_80ms_ECNEn_OFLDis/cwnd.dat fqCobalt_1_80Mbps_80ms_ECNEn_OFLDis/cwnd.dat' ; outputfile='MyPlot.png'; titles = 'FQ-CoDel FQ-Pie FQ-Cobalt'; X_axis_label='Time (Seconds)' ; Y_axis_label='CWND (Packets)'" plotter-gnu
```

