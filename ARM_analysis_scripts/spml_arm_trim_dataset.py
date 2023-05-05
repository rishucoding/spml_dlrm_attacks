import pandas as pd

buy_log = pd.read_csv('../dataset/buy_behavior_log.csv')

print(buy_log.head())
print(buy_log.shape)
# buy_log = buy_log[:400000]

# sort entire buy log with time
buy_log = buy_log.sort_values(by=['time_stamp'], ascending=True)
# buy_log.sort_values('time_stamp')
print(buy_log.head())
print(buy_log.shape)

# 5 400k, 200k, 100k
# trim required amount of dataset
# buy_log = buy_log[1600001:2000000]
buy_log = buy_log[:200000]
print(buy_log.head())
print(buy_log.shape)

print("min: ", buy_log['time_stamp'].min())
print("max: ", buy_log['time_stamp'].max())

# buy_log = buy_log.sort_values(['time_stamp', 'user'])
buy_log.head()
df = buy_log

# Sort the dataset by user ID and timestamp
df = df.sort_values(['user', 'time_stamp'])

# Define the time threshold (e.g., 30 minutes)
# prev 3 hours
time_threshold = pd.Timedelta('23 hours')

# Initialize the order ID to 0
order_id = 0

# Create a new column to store the order ID
df['order_id'] = 0
# no of users = no of orders

# 1 - 1
# 2 - 2
# 1 - 3

# Loop over each user and create orders based on the timestamp
for user_id, user_df in df.groupby('user'):
    # Initialize the order start time to the first log timestamp
    order_start_time = user_df.iloc[0]['time_stamp']
    order_id += 1

    # Loop over each log for the user
    for i, row in user_df.iterrows():
        # Calculate the time difference between the current log and the previous log
        time_diff = pd.Timedelta(row['time_stamp'] - order_start_time)

        # If the time difference is greater than the time threshold, create a new order
        if time_diff > time_threshold:
            order_id += 1
            order_start_time = row['time_stamp']

        # Assign the order ID to the current log
        df.at[i, 'order_id'] = order_id

# Save the modified dataset to a new CSV file
df.to_csv('taobao_dataset_with_orders_400k_2.csv', index=False)
