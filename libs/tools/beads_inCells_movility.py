from sub.cor2img import transfpar,coincidROI

wdirs = ["/mnt/data/Anastasia/18_11_29_pd23_11_div6_25Hzsqwave/",
"/mnt/data/Anastasia/QDs_prelabsem1811/","/mnt/data/Anastasia/Initial/","/mnt/data/Anastasia/Glass/",
"/mnt/data/Anastasia/test_18_07_11_pd29_06_div12_WISSNR","/mnt/data/Anastasia/19_02_20_pd15_02_div5_NR_BeRST_MOVILITYONLY"]

dfiles = []
for dirt in wdirs:
    basedir = dirt
    files = os.listdir(basedir)
    if dirt[-1] != '/':
        dirt = dirt+'/'
    for f in files:
        if f[-4:]=='.tif': 
            try:
                i = int(f[-5])
                dfiles.append(dirt+f)
            except:
                pass

cfile = dfiles[-1]
wdir = ''
cf2 = cfile.split(".")[0].split("/")
for fs in cf2[:-1]:
    wdir = wdir+fs+'/'
wdir = wdir+cf2[-1]+'output/sptrack/'

%pylab
a = loadtxt(wdir+'../posA.dat')
b = loadtxt(wdir+'../../cell8_beads.dat')
selection = coincidROI(b,a,err = 2)


cfile = dfiles[-2]
a = loadtxt(wdir+'../posA.dat')
b = loadtxt(wdir+'../../cell8_beads.dat')
selection = coincidROI(b,a,err = 2)
