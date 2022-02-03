
##-----import library here
import numpy as np
import matplotlib.pyplot as plt
##-----end load library

        #h          #z            #Eint       #Ebackground    #U        #Otip_NO_ESM  #Otip_Cu_ESM
e1,s,px,py,pz = np.loadtxt('0020-end', usecols = (0,1,2,3,4), unpack = True)
e,pix,piy,sig,pisx,pisy = np.loadtxt('pdos-end-c9.dat', usecols = (0,3,4,5,6,7), unpack = True)
e,cpix,cpiy,cs,cpisx,cpisy = np.loadtxt('coop-end-c9.dat', usecols = (0,3,4,5,6,7), unpack = True)


fig = plt.figure(figsize=(2,2))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

ax1.tick_params(labelsize='small', direction = 'in',width=1)
ax1.spines['top'].set_linewidth(1)
ax1.spines['bottom'].set_linewidth(1)
ax1.spines['right'].set_linewidth(1)
ax1.spines['left'].set_linewidth(1)

ax2.tick_params(labelsize='small', direction = 'in',width=1)
ax2.spines['top'].set_linewidth(1)
ax2.spines['bottom'].set_linewidth(1)
ax2.spines['right'].set_linewidth(1)
ax2.spines['left'].set_linewidth(1)

ax3.tick_params(labelsize='small', direction = 'in',width=1)
ax3.spines['top'].set_linewidth(1)
ax3.spines['bottom'].set_linewidth(1)
ax3.spines['right'].set_linewidth(1)
ax3.spines['left'].set_linewidth(1)
#set font
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"

#set xrange
###ax1
xll = -15
xlr  = 5
ylb  = 0
ylt  = 0.3
ax1.set_xlim(xll,xlr)
ax1.set_xticks(ticks = np.linspace(xll,xlr,21))
ax1.set_yticklabels([])
ax1.set_xticklabels('')
ax1.set_ylim(ylb,ylt)
ax1.plot(np.linspace(ylb,ylt,3)*0,np.linspace(ylb,ylt,3), '--', color = 'gray', linewidth=1)

###ax2
xll = -15
xlr  = 5
ylb  = 0
ylt  = 1.5
ax2.set_xlim(xll,xlr)
ax2.set_xticks(ticks = np.linspace(xll,xlr,21))
ax2.set_yticklabels([])
ax2.set_xticklabels('')
ax2.set_ylim(ylb,ylt)
ax2.plot(np.linspace(ylb,ylt,3)*0,np.linspace(ylb,ylt,3), '--', color = 'gray', linewidth=1)

###ax3
xll = -15
xlr  = 5
ylb  = -0.3
ylt  =  0.3
ax3.set_xlim(xll,xlr)
ax3.set_xticks(ticks = np.linspace(xll,xlr,21))
ax3.set_xticklabels([])
ax3.set_yticklabels([])
ax3.set_ylim(ylb,ylt)
ax3.plot(np.linspace(ylb,ylt,3)*0,np.linspace(ylb,ylt,3), '--', color = 'gray', linewidth=1)
ax3.plot(np.linspace(xll,xlr,3) ,np.linspace(xll,xlr,3)*0, '--', color = 'gray', linewidth=1)




#set label
#plt.xlabel('$E - E_F$ /eV')
#ax2.set_ylabel('PDOS')
#ax3.set_ylabel('COOP')

ax1.plot(e1,s,   '-', color = 'black',   label = 'B $2s}$',markersize = 5, linewidth=2)
ax1.plot(e1,px,  '-', color = 'blue',  label = 'B $2p\mathrm{_{x}}$',markersize = 5, linewidth=2)
ax1.plot(e1,py,  '-', color = 'red',    label = 'B $2p\mathrm{_{y}}$',markersize = 5, linewidth=2)
ax1.plot(e1,pz,  '-', color = 'green',   label = 'B $2p\mathrm{_{z}}$',markersize = 5, linewidth=2)
#ax1.legend(loc='best', handlelength=2, borderpad=0.1, labelspacing=0.1, ncol = 2,fontsize=10,frameon = False)


#e,pix,piy,s,pisx,pisy
ax2.plot(e,pix,  '-', color = 'black', label = '$\mathrm{ \pi _{x}}$',markersize = 5, linewidth=2)
ax2.plot(e,piy,  '-', color = 'purple', label = '$\mathrm{ \pi _{y}}$',markersize = 5, linewidth=2)
ax2.plot(e,sig,    '-', color = 'blue', label = '$\mathrm{ \sigma}$',markersize = 5, linewidth=2)
ax2.plot(e,pisx, '-', color = 'green', label = '$\mathrm{ \pi ^*_{x}}$',markersize = 5, linewidth=2)
ax2.plot(e,pisy, '-', color = 'red', label = '$\mathrm{ \pi ^*_{y}}$',markersize = 5, linewidth=2)
#ax2.legend(loc='best', handlelength=2, borderpad=0.1, labelspacing=0.1, ncol = 2,fontsize=10,frameon = False)

ax3.plot(e,cpix,  '-', color = 'black', label = '$\mathrm{ \pi _{x}}$',markersize = 5, linewidth=2)
ax3.plot(e,cpiy,  '-', color = 'purple', label = '$\mathrm{ \pi _{y}}$',markersize = 5, linewidth=2)
ax3.plot(e,cs,    '-', color = 'blue', label = '$\mathrm{ \sigma}$',markersize = 5, linewidth=2)
ax3.plot(e,cpisx, '-', color = 'green', label = '$\mathrm{ \pi ^*_{x}}$',markersize = 5, linewidth=2)
ax3.plot(e,cpisy, '-', color = 'red', label = '$\mathrm{ \pi ^*_{y}}$',markersize = 5, linewidth=2)
#ax3.legend(loc='best', handlelength=2, borderpad=0.1, labelspacing=0.1, ncol = 2,fontsize=10,frameon = False)


fig.subplots_adjust(top=0.95, bottom=0.05, left=0.17, right=0.845,wspace=0.0,
                    hspace=0.0)

fig.tight_layout()
plt.savefig('test.png', dpi=300)
plt.show()
