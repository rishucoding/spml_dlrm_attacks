# spml_dlrm_attacks
Establishing attacks in DLRM inference

## Taobao Dataset: https://tianchi.aliyun.com/dataset/dataDetail?dataId=56&lang=en-us

# Steps to run the Association rule mining and Sensitive attribute analysis++:
We use Jupyter Notebook and conda environment to run the programming for the project. These are the main files required for sensitive attribute attack. Make sure buy_behavior_log and user_profile are in same location as SPML_two_brand_analysis and SPML_three_brand_analysis are there together. This will ensure you will get complete analysis of ambiguity values and how they were found. 

Similarly, for association rule mining analysis locate the taobao_dataset_with_orders**** , keep them in same location. Ensure relative path if issues arise. 

The scripts to run association rule mining are in ARM_analysis_scripts folder. These can be directly executed. mlxtend package needs to be installed to run apriori for association rule mining. 
All the generated datasets and analysis results are present in dataset and dataset/logs folder respectively.
