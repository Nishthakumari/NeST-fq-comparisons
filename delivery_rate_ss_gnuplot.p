set datafile separator ','
plot 'ss_json_copy_fq_codel_ecn_off.csv' every ::1 u 1:7 w l title "FQ-CoDel ECN disabled", 'ss_json_copyfq_codel_ecn_on.csv' every ::1 u 1:7 w l title "FQ-CoDel ECN enabled"
set title "Socket Statistics"
set xlabel "Time (Seconds)"
set ylabel "Delivery Rate (Mbps)"
set xrange [0:40]
set yrange [0:1000]
set grid

set term png size 1200, 720
set output "DeliveryRate.png"
replot
