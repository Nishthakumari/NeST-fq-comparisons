## Notes
`FQ_PIE` AQM support in **iproute2** was added from _version 5.5_.
- To install iproute2 with fq_pie support (e.g: v5.7)

```bash
wget http://in.archive.ubuntu.com/ubuntu/pool/main/i/iproute2/iproute2_5.7.0-1ubuntu1_amd64.deb
sudo apt install ./iproute2_5.7.0-1ubuntu1_amd64.deb
```

- Apply the below patches to generate dat files automatically in NeST.
```bash
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/plotter/tc.py > tc.diff
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/plotter/ss.py > ss.diff
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/plotter/ping.py > ping.diff
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/plotter/iperf3.py > iperf3.diff
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/plotter/netperf.py > netperf.diff
sudo patch /usr/local/lib/python3.8/dist-packages/nest/experiment/pack.py > pack.diff
```
