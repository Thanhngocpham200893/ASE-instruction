import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
#import seaborn as sns

#sns.set()
#sns.set_style('whitegrid')
#sns.set_palette('gray')

x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12 = np.loadtxt('res.txt', usecols =(0,1,2,3,4,5,6,7,8,9,10,11,12),unpack = True)
x1,y11,y21,y31,y41,y51 = np.loadtxt('res_partial.txt', usecols =(0,1,2,3,4,5),unpack = True)
fig = plt.figure(figsize = [7,3.5])
ax = fig.gca()

ax.tick_params(labelsize=8, direction = 'in',width=1)
ax.spines['top'].set_linewidth(1)
ax.spines['bottom'].set_linewidth(1)
ax.spines['right'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

ax.tick_params(which='both', direction = 'in',width=1, labelsize=6)
ax.tick_params(which='major', length=4, labelsize=6)
ax.tick_params(which='minor',direction = 'in', length=6)


font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

font2 = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 10,
        }


ax= plt.subplot(1,3,1)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

ax.tick_params(which='both', direction = 'in',width=1, labelsize=6)
ax.tick_params(which='major', length=3, labelsize=6)
ax.tick_params(which='minor',direction = 'in', length=2)
xll = 0.5
xlr = 13.5
ylb = -0.5
ylt = 3.0
plt.xlim(xll,xlr)
plt.ylim(ylb,ylt)
plt.xticks(np.linspace(1,13,7),fontsize = 8)
plt.yticks(np.linspace(-0.5,3.0,8),fontsize = 8)
plt.ylabel('$E_\mathrm{f}$ per Pd atom /eV', fontdict = font)
plt.text(xlr*0.5, ylt+0.1, '$\mathrm{Pd}$',ha = 'center')
#plot
s1 =  np.isfinite(y1)
plt.plot(x[s1],y1[s1], '--o',   label ='$\mathrm{SrO}$'  ,color = 'blue', markersize = 5,linewidth=2)
s1 =  np.isfinite(y7)
plt.plot(x[s1],y7[s1], '--x',   label ='$\mathrm{\gamma-Al_2O_3[100]}$'  ,color = 'black', markersize = 5,linewidth=2)
s1 =  np.isfinite(y3)
plt.plot(x[s1],y3[s1], '--s',   label ='$\mathrm{TiO_2}$'  ,color = 'green', markersize = 5,linewidth=2)
s1 =  np.isfinite(y9)
plt.plot(x[s1],y9[s1], '--o',   label = '$\mathrm{SrO-PdO_2}$'  ,color = 'magenta', markersize = 5,linewidth=2)
s1 =  np.isfinite(y11)
plt.plot(x[s1],y11[s1], '--s',   label = '$\mathrm{PdO_2}$'  ,color = 'red', markersize = 5,linewidth=2)


plt.legend(loc = 0, bbox_to_anchor = (-0.4,0.5),fontsize = 8)
plt.grid()

ax = plt.subplot(1,3,2)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

ax.tick_params(which='both', direction = 'in',width=1, labelsize=6)
ax.tick_params(which='major', length=3, labelsize=6)
ax.tick_params(which='minor',direction = 'in', length=2)
xll = 0.5
xlr = 13.5
ylb = -0.5
ylt = 3.0
plt.xlim(xll,xlr)
plt.ylim(ylb,ylt)
plt.xticks(np.linspace(1,13,7))
plt.yticks(np.linspace(-0.5,3.0,8))
plt.xlabel('$N\mathrm{_{Pd}}$', fontdict = font)
plt.text(xlr*0.5, ylt+0.1, '$\mathrm{PdO_{0.5-0.6}}$',ha = 'center')
plt.xticks(np.linspace(1,13,7),fontsize = 8)
plt.yticks(np.linspace(-0.5,3.0,8),labels = [],fontsize = 8)
#plt.ylabel('$E_\mathrm{f}$ per Pd atom', fontdict = font)
s1 =  np.isfinite(y11)
plt.plot(x1[s1],y11[s1], '--o',   label ='$\mathrm{SrO}$'  ,color = 'blue', markersize = 5,linewidth=2)
s1 =  np.isfinite(y31)
plt.plot(x1[s1],y31[s1], '--x',   label ='$\mathrm{Al_2O_3}$'  ,color = 'black', markersize = 5,linewidth=2)
s1 =  np.isfinite(y21)
plt.plot(x1[s1],y21[s1], '--s',   label ='$\mathrm{TiO_2}$'  ,color = 'green', markersize = 5,linewidth=2)

s1 =  np.isfinite(y41)
plt.plot(x1[s1],y41[s1], '--o',   label = '$\mathrm{SrO-PdO_2}$'  ,color = 'magenta', markersize = 5,linewidth=2)
s1 =  np.isfinite(y51)
plt.plot(x1[s1],y51[s1], '--s',   label = '$\mathrm{PdO_2}$'  ,color = 'red', markersize = 5,linewidth=2)


plt.grid()

ax = plt.subplot(1,3,3)
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

ax.tick_params(which='both', direction = 'in',width=1, labelsize=6)
ax.tick_params(which='major', length=3, labelsize=6)
ax.tick_params(which='minor',direction = 'in', length=2)

xll = 0.5
xlr = 13.5
ylb = -0.5
ylt = 3.0
plt.xlim(xll,xlr)
plt.ylim(ylb,ylt)
plt.xticks(np.linspace(1,13,7),fontsize = 8)
plt.yticks(np.linspace(-0.5,3.0,8),labels = [],fontsize = 8)
plt.text(xlr*0.5, ylt+0.1, '$\mathrm{PdO}$',ha = 'center')
s1 =  np.isfinite(y2)
plt.plot(x[s1],y2[s1], '--o',   label ='$\mathrm{SrO}$'  ,color = 'blue', markersize = 5,linewidth=2)
s1 =  np.isfinite(y6)
#plt.plot(x[s1],y6[s1], '--s',   label ='$\mathrm{Pd-V_O@TiO_2}$'  ,color = 'cyan', markersize = 5,linewidth=2)
s1 =  np.isfinite(y8)
plt.plot(x[s1],y8[s1], '--x',   label ='$\mathrm{\gamma-Al_2O_3[100]}$'  ,color = 'black', markersize = 5,linewidth=2)
s1 =  np.isfinite(y4)
plt.plot(x[s1],y4[s1], '--s',   label ='$\mathrm{TiO_2}$'  ,color = 'green', markersize = 5,linewidth=2)

s1 =  np.isfinite(y10)
plt.plot(x[s1],y10[s1], '--o',   label = '$\mathrm{SrO-PdO_2}$'  ,color = 'magenta', markersize = 5,linewidth=2)
s1 =  np.isfinite(y12)
plt.plot(x[s1],y12[s1], '--s',   label = '$\mathrm{PdO_2}$'  ,color = 'red', markersize = 5,linewidth=2)


plt.subplots_adjust(wspace=None, hspace=None)
plt.tight_layout()
plt.grid()
plt.savefig('combine.png', dpi=300)
plt.show()
