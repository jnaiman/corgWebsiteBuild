# how many entries do we wanna output
nentries = 6000


# were are we saving data?
saveFilejsonLarge = '/Users/jillnaiman1/corgWebsiteBuild/data/corgiData_countries_large.json'
saveFilejsonSmall = '/Users/jillnaiman1/corgWebsiteBuild/data/corgiData_countries.json'

#-----------------------------------------------------------
            
# save to json
import json

with open(saveFilejsonLarge) as json_file:
    data = json.load(json_file)

import numpy as np

indicies = np.random.choice(range(len(data)-1), nentries, replace=False)

# make new data
data_out = []
for i in indicies:
    data_out.append(data[i])

# dump to file
f = open(saveFilejsonSmall,'w')
f.write(json.dumps(data_out,indent=2))
f.close()
    
