import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
def animate(i):
    if(not debug):
        ssh = SSHClient()
        #print(ssh)
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect("raspberrypi.local", 22, "pi", "chungus69")
        stdin, stdout, stderr = ssh.exec_command("cat ~/Documents/ads1115/text_data.txt")
        graphlines = stdout.readlines()                
    else:
 

        graph_data = open('data.txt','r').read()
        graphlines = graph_data.split('\n')
    xs = []
    ys = []
    i = 0
    for line in graphlines:
        if len(line) > 1:
            ys.append(float(line))
            xs.append(i)
            i += 1
    ax1.clear()
    ax1.plot(xs, ys)
from paramiko import SSHClient, AutoAddPolicy, Transport

debug = False
graphlines = ""

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()