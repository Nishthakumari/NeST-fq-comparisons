set datafile separator ','
set terminal png font arial 8 size 1200, 700
set output "Qlen_FQ-CoDel_ECN_ON_OFF.png"
set title "Traffic Control"
set xlabel "Time (Seconds)"
set ylabel "Queue Length (Packets)"
set xrange [0:40]
set yrange [0:100]
set grid
plot 'tc_FQ-CoDel_ECN_disabled.csv' every ::1 u 1:9 w l lw 3 title 'FQ-CoDel-ECN-off', 'tc_FQ-CoDel_ECN_enabled.csv' every ::1 u 1:9 w l lw 3 title 'FQ-CoDel-ECN-on'
