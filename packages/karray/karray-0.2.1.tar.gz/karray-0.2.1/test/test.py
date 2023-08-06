# %%
import karray as ka
import numpy as np

# %%
dc_symb = {'G_RES.csv':['n','tech','h'],'G_L.csv':['n','tech','h'],'con1a_bal.csv':['n','h'],'Z.csv':[], 'N_TECH.csv':['n','tech']}

# %%
kalist = {}
for k, dims in dc_symb.items():
    row_csv =  np.loadtxt(k, delimiter=',', skiprows=1, dtype=object)
    index = {}
    i = -1
    for dim in dims:
        i+=1
        index[dim] = row_csv[:,i]
    i+=1
    if dims:
        value = row_csv[:,i].astype('float64')
    else:
        value = row_csv[0:1].astype('float64')
    kalist[k] = dict(index=index,value=value)


# %%
G_RES = ka.Long(**kalist['G_RES.csv'])
G_L = ka.Long(**kalist['G_L.csv'])
con1a_bal = ka.Long(**kalist['con1a_bal.csv'])
Z = ka.Long(**kalist['Z.csv'])
N_TECH = ka.Long(**kalist['N_TECH.csv'])

# %%
G_RES

# %%
G_L

# %%
con1a_bal

# %%
con1a_bal.rows_display = 15
con1a_bal.decimals_display = 3
con1a_bal.oneshot_display = False
con1a_bal

# %%
Z

# %%
N_TECH

# %%
N_TECH.dims

# %%
N_TECH['n']

# %%
N_TECH['n',['CH', 'CZ', 'DE']]

# %%
N_TECH[N_TECH != 0.0]

# %%
N_TECH[N_TECH != 0.0]['tech']

# %%
N_TECH[:]

# %%
N_TECH[0:100]

# %%
arr = np.loadtxt('G_RES.csv', delimiter=',', skiprows=1, dtype=object, usecols=[0,1,2,3])
arr[:,-1] = arr[:,-1].astype(float)
N = ka.numpy_to_long(arr, ['n','tech','h'])
n = arr.copy()

# %%
arr = np.loadtxt('con1a_bal.csv', delimiter=',', skiprows=1, dtype=object, usecols=[0,1,2])
arr[:,-1] = arr[:,-1].astype(float)
P = ka.numpy_to_long(arr, ['n','h'])
p = arr.copy()

# %%
N

# %%
P

# %%
xn = ka.Array(N)
xp = ka.Array(P)

# %%
xn

# %%
xp

# %%
xn.long

# %%
xp.long

# %%
xx = xp*xn

# %%
# xx.dense

# %%
P.insert(j={'n':{'AT':'perro', 'BE':'loco', 'CH':'loco', 'CZ':'loco', 'DE':'loco', 'DK':'loco', 'FR':'loco', 'IT':'loco', 'LU':'loco', 'NL':'loco', 'PL':'zorro'}})

# %%
P.insert(j='lr')

# %%
lng = P.insert(j=2)
lng

# %%
nlng = lng.drop('j')
nlng

# %%
alng = nlng.rename(n='k')
alng

# %%
alng.dims

# %%
alng[['h','k'],:]

# %%
alng[['h','k'],0:10]

# %%
alng['k',['AT','PL']]

# %%
# New day: add_dim , insert

# %%
xx.dims

# %%
xx.long

# %%
xx.insert(z='a')

# %%
xx.add_dim(z='a')

# %%
xx.add_dim(z=2)

# %%
xx.insert(w={'n':{'AT':'n', 'BE':'m', 'CH':'q', 'CZ':'m', 'DE':'n', 'DK':'q', 'FR':'m', 'IT':'n', 'LU':'q', 'NL':'m', 'PL':'n'}})

# %%
xx.insert(w={'n':{'AT':1, 'BE':2, 'CH':3, 'CZ':1, 'DE':2, 'DK':3, 'FR':1, 'IT':2, 'LU':3, 'NL':1, 'PL':2}})

# %%
# xx.insert(casa=0.3)

# %%
ll = ka.Long(index={'a':[1]}, value=0.0)

# %%
ll

# %%
ll.ndim

# %%
zo = ka.Array(coords={'a':['d','g']})
zo

# %%
zo.long.value

# %%
sr = np.array(['a','b','c'])
ir = np.array([0,1,2])

# %%
sn = np.array(['a','b','c','a','b','c','a','b','c'])

# %%
sr.searchsorted(sn)

# %%
xx.long.index

# %%
long_stack = np.vstack([xx.coords[dim].searchsorted(xx.long._index[dim]) for dim in xx.dims])

# %%
long_stack

# %%
xx.dims

# %%
xx.shape

# %%
indexes = np.ravel_multi_index(long_stack, xx.shape)

# %%
capacity =  int(np.prod(xx.shape))

# %%
dense = np.zeros((capacity,), dtype=float)

# %%
dense[indexes] = xx.long.value

# %%
dense

# %%
tup = np.unravel_index(np.arange(capacity), xx.shape)

# %%
tup[0]

# %%
index = {dim:xx.coords[dim][idx] for dim, idx in zip(xx.dims,tup)}

# %%
index

# %%


# %%
long = ka.Long(index,dense)
long

# %%
xy = long[long!=0]




