 # gnuplot -e "files = 'tcp-validation-first-tcp-cwnd-segcwnd-50ms-50Mbps-ecn.dat tcp-validation-first-tcp-cwnd-seginflight-1.dat' ; outputfile='Time (Seconds)pass.png'; titles = 'segcwnd seginflight'; X_axis_label='Time (Seconds)' ; Y_axis_label='something'" plotter-gnu

import os

def get_plots(files,titles,outputfile,X_axis_label,Y_axis_label):
    command = "gnuplot -e "
    command = command + "\""
    command = command + "files =" + files + "; "
    command = command + "titles =" + titles + "; "
    command = command + "outputfile =" + outputfile + "; "
    command = command + "X_axis_label =" + X_axis_label + "; "
    command = command + "Y_axis_label =" + Y_axis_label 
    command = command + "\" "
    command = command + "plotter-gnu"
    # print(command)
    os.system(command)


queue_disciplines = ["fqCodel","fqPie","fqCobalt"]
rates = ["80Mbps","160Mbps","1000Mbps"] 
ecn_values = ["ECNEn","ECNDis"]
offloads = ["OFLEn", "OFLDis"]
delays = ["4ms","40ms","80ms","800ms"] 
flows = ["1","3","16"]
datfiles = ["sending_rate.dat", "ping.dat", "cwnd.dat", "delivery_rate.dat", "dev_rtt.dat", "pacing_rate.dat", "rto.dat", "rtt.dat", "ssthresh.dat", "backlog.dat", "drops.dat", "ecn_mark.dat", "qlen.dat"]
y_lables = {"sending_rate.dat": "'Sending Rate (Mbps)'", "ping.dat": "' Ping RTT (ms)'", "cwnd.dat": "'CWND (Packets)'", "delivery_rate.dat" : "'Delivery Rate (Mbps)'", "dev_rtt.dat" : "'Dev RTT (ms)'", "pacing_rate.dat" : "'Pacing Rate (Mbps)'", "rto.dat" : "'Retransmission TimeOut (ms)'", "rtt.dat" : "'RTT (ms)'", "ssthresh.dat" : "'SSThresh (Packets)'", "backlog.dat" : "'Backlog (Bytes)'", "drops.dat" : "'Drops (Packets)'", "ecn_mark.dat": "'ECN Mark (Packets)'", "qlen.dat" : "'Queue Length (Packets)'"}

os.system("mkdir queue_disciplines_comparison")
os.system("mkdir rates_comparison")
os.system("mkdir ECN_comparison")
os.system("mkdir offload_comparison")
os.system("mkdir delay_comparison")
os.system("mkdir flows_comparison")

# files = "'" + input("Enter the file names space separated:") + "'"
# titles = "'" + input("Enter the titles space separated:") + "'"
# outputfile = "'" + input("Enter the output file name:") + "'"
# X_axis_label = "'" + input("Enter the X axis label:") + "'"
# Y_axis_label = "'" + input("Enter the Y axis label:") + "'"

for qd in queue_disciplines:
    for r in rates:
        for ecn in ecn_values:
            for offload in offloads:
                for d in delays:
                    for f in flows:
                        for df in datfiles:
                            for num in [0,1,2,3,4,5]:
                                if(num == 0):
                                    base = f + "_" + r + "_" + d + "_" + ecn + "_" + offload
                                    file1 = "fqCodel_" + base + "/" + df
                                    file2 = "fqPie_" + base + "/" + df 
                                    file3 = "fqCobalt_" + base + "/" + df 
                                    files =  "'" + file1 + " " + file2 + " " + file3 + "'"
                                    base = df[:-4] + "_queue_disclipline_" + base 
                                    get_plots(files,"'FQ\_CoDel FQ\_PIE FQ\_COBALT'","'queue_disciplines_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])
                                elif(num == 1):
                                    base1 = qd + "_" 
                                    base2 = r + "_" + d + "_" + ecn + "_" + offload
                                    file1 = base1 + "1_" + base2 + "/" + df
                                    file2 = base1 + "3_" + base2 + "/" + df
                                    file3 = base1 + "16_" + base2 + "/" + df
                                    files = "'" + file1 + " " + file2 + " " + file3 + "'"
                                    base = df[:-4] + "_" + base1 + "flows_" + base2
                                    get_plots(files,"'flows\_1 flows\_3 flows\_16'","'flows_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])
                                elif(num == 2):
                                    base1 = qd + "_" + f + "_"
                                    base2 = d + "_" + ecn + "_" + offload
                                    file1 = base1 + "80Mbps_" + base2 + "/" + df
                                    file2 = base1 + "160Mbps_" + base2 + "/" + df
                                    file3 = base1 + "1000Mbps_" + base2 + "/" + df
                                    files = "'" + file1 + " " + file2 + " " + file3 + "'"
                                    base = df[:-4] + "_" + base1 + "rate_" + base2
                                    get_plots(files,"'DataRate\_80Mbps DataRate\_160Mbps DataRate\_1000Mbps'","'rates_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])
                                elif(num == 3):
                                    base1 = qd + "_" + f + "_" + r + "_"
                                    base2 = ecn + "_" + offload
                                    file1 = base1 + "4ms_" + base2 + "/" + df
                                    file2 = base1 + "40ms_" + base2 + "/" + df
                                    file3 = base1 + "80ms_" + base2 + "/" + df
                                    file4 = base1 + "800ms_" + base2 + "/" + df
                                    files = "'" + file1 + " " + file2 + " " + file3 + " " + file4 + "'"
                                    base = df[:-4] + "_" + base1 + "delays_" + base2
                                    get_plots(files,"'RTT\_4ms RTT\_40ms RTT\_80ms RTT\_800ms'","'delay_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])
                                elif(num == 4):
                                    base1 = qd + "_" + f + "_" + r + "_" + d + "_"
                                    base2 = offload
                                    file1 = base1 + "ECNEn_" + base2 + "/" + df
                                    file2 = base1 + "ECNDis_" + base2 + "/" + df
                                    files = "'" + file1 + " " + file2 + "'"
                                    base = df[:-4] + "_" + base1 + "ECN_" + base2
                                    get_plots(files,"'ECN\_Enabled ECN\_Disabled'","'ECN_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])
                                elif(num == 5):
                                    base = qd + "_" + f + "_" + r + "_" + d + "_" + ecn + "_"
                                    file1 = base + "OFLEn" + "/" + df
                                    file2 = base + "OFLDis" + "/" + df
                                    files = "'" + file1 + " " + file2 + "'"
                                    base = df[:-4] + "_" + base + "Offload"
                                    get_plots(files,"'OFL\_Enabled OFL\_Disabled'","'offload_comparison/"+base+".png'","'Time (Seconds)'",y_lables[df])             
                                   
   

# get_plots(files,titles,outputfile,X_axis_label,Y_axis_label)
