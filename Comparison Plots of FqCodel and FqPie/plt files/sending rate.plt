set datafile separator ','
set terminal png font arial 8 size 1200, 700
set output "Ping_RTT_FQ-CoDel_ECN_ON_OFF.png"
set title "Ping"
set xlabel "Time (Seconds)"
set ylabel "RTT (ms)"
set xrange [0:40]
set yrange [0:9]
set grid
plot 'ping_FQ-CoDel_ECN_disabled.csv' every ::1 u 1:2 w l lw 3 title 'FQ-CoDel-ECN-off', 'ping_FQ-CoDel_ECN_enabled.csv' every ::1 u 1:2 w l lw 3 title 'FQ-CoDel-ECN-on'
