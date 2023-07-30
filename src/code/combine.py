import random
import sys
import os 
import shamirs
import pickle
import sqlite3
from database_service import DatabaseService
database = DatabaseService()

MODULUS = 1319572433731810224709718299072702623166519064149438739750138186267581522745145352176726739501958309852329389784536171949938480185325121031483786028002875104855775730945659703755771119598821454670487103532250771335416922730226724812416219164572155444110904661688252014518101032482336157864283618721464502979848307615806811956680059102951238118188599778667250729992153247664779010950781180934699430134539310367706362519136212067448892401579678549279206900956365670681244800383057627189685415755829843684129324916179604751097267360659391693428966914273909457212059146988297876120031704034244479072374531645102331484364761361634361852645070786883687338725379721405033054727107808321216149498679063405779443156830933583938817659762925995845544928513265756731738309123121078594193568317376462119529653732892680415018689377890476251299412669625835857218222194583686341245415213544416872730876934066749641759172824616083484411953265873331075083369189075765563399204897437610522159919879792705727817949398829587258127054659018537209977812928197178628625029268435929766205670403047834679576391353379169016658761899075907052931700301890708928061800821028517195149443992333868411857855551243573750852966059942557045677447097380171308641179606211026663825959143744964638609357299513262283787890486465105592619746550297778078466049296861436585201231523380082670155555013275325461217488995903498592261630288566379921654438567185409072087002264434023608330882754628108280232391680971979081214591322840403743394269817840174729849925357168306932037570108738858751157530107953611112518441426087545618626266789901602368382954426390646805215598347174663440208460182769601398391885948408444725807687511629016766690848367008261320421064345368433841844520963343695483884998825744119991003970900446182091961254917052647377251828670465453846583319872266941016688805677536965668892905005506512763888272837587409983075606344245751401319106044710385805719764535513291

# change cwd
os.chdir("..")

# Get argument
target_ID = sys.argv[1]
target = sys.argv[2] # retrive which number
pick = int(sys.argv[3]) # pick how many shares  

# list
file_list = []

# Count total number of DB
num_shares = len(next(os.walk("database"))[1])
for i in range(num_shares):
    file_list.append(i)

# Randomly pick files in DB
pick_num = random.sample(range(0, len(file_list)), pick)
#pick_num = []
#pick_num.append(0)
pick_list = []
for i in pick_num:
    data = database._fetch(target, target_ID, i)
    data_list = data.split(", ")
    data_list[0] = int(data_list[0].replace("share(", ""))
    data_list[1] = int(data_list[1])
    data_list[2] = int(data_list[2].replace(")", ""))
    obj = shamirs.share(data_list[0], data_list[1], MODULUS)
    pick_list.append(obj)



# Combine them
combine_s = shamirs.interpolate(pick_list)

# Write the combined file to "combine"
if not os.path.exists("combine"):
    os.makedirs("combine")
with open(f"combine/{target_ID}_combined_{target}", "wb") as f:
    pickle.dump(combine_s, f)

# Terminal
#print(f"[ ID {target_ID} ] The shares of {target} are combined: {combine_s}")
#print(f"[ ID {target_ID} ] The shares of {target} are combined.")