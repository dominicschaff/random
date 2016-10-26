import sys
import simple_plot as p


types = ['bic','highspeed','htcp','hybla','illinois','lp','probe','scalable','vegas','veno','westwood','yeah']
t1 = types[int(sys.argv[1])]
t2 = types[int(sys.argv[2])]
try:
    f = open(t1+','+t2+'.txt','r')
    print 'Plotting: '+t1+','+t2+'.txt'
    data=[[],[],[]]
    for l in f:
        l = l.rstrip()
        d = l.split(' ')
        data[0].append(d[0])
        data[1].append(d[1])
        data[2].append(d[2])
    f.close()
    plot = p.simple_plot()
    plot.new_plot(True, t1 + " vs " + t2)
    plot.add_curve_data(data[0], data[1], t1, "Time (seconds)", "Throughput (Mbits/s")
    plot.add_curve_data(data[0], data[2], t2, "Time (seconds)", "Throughput (Mbits/s")
    plot.generate_plots()
    plot.save_plots("data")
except IOError as e:
    print "Could not open: " + t1+','+t2+'.txt'