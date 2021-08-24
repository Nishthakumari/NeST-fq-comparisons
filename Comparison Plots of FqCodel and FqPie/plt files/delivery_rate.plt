set datafile separator ','
set terminal png font arial 8 size 1200, 700
set output "Delivery_Rate_FQ-CoDel_ECN_ON_OFF.png"
set title "Socket Statistics"
set xlabel "Time (Seconds)"
set ylabel "Delivery Rate (Mbps)"
set xrange [0:40]
set yrange [0:1000]
set grid
plot 'ss_FQ-CoDel_ECN_disabled.csv' every ::1 u 1:7 w l lw 3 title 'FQ-CoDel-ECN-off', 'ss_FQ-CoDel_ECN_enabled.csv' every ::1 u 1:7 w l lw 3 title 'FQ-CoDel-ECN-on'
