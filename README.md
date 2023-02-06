# spml_dlrm_attacks
Establishing attacks in DLRM inference

## Taobao Dataset: https://tianchi.aliyun.com/dataset/dataDetail?dataId=56&lang=en-us

## Steps: 
1. Download the user_profile.csv.tar.gz and behavior_log.csv.tar.gz
2. STATIC PROFILING - Creating distribution of brands(items) over attributes(like age or gender) (similar to Figure#4 -- would have lots of entries)
3. ATTACK CREATION - Using the static distributions, we can create the ambiguity distributions (Figure#5)

## TODO: 
1. Recreate the attack and validate with the results shown in the paper.(Figure#5)
2. Use the intersection operation to improve the attack.
