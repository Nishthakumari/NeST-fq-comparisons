set datafile separator ','
set terminal png font arial 8 size 1200, 700
set output "SSThresh_FQ-CoDel_ECN_ON_OFF.png"
set title "Socket Statistics"
set xlabel "Time (Seconds)"
set ylabel "SSThresh (Packets)"
set xrange [0:40]
set yrange [0:1600]
set grid
plot 'ss_FQ-CoDel_ECN_disabled.csv' every ::1 u 1:5 w l lw 3 title 'FQ-CoDel-ECN-off', 'ss_FQ-CoDel_ECN_enabled.csv' every ::1 u 1:5 w l lw 3 title 'FQ-CoDel-ECN-on'
