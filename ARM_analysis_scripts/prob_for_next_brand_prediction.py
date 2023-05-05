import pandas as pd

df = pd.read_csv('../dataset/taobao_dataset_with_orders_400k_3.csv')

brand_combos = [(11299, 14328),
                (93068, 11299),
                (207241, 11299),
                (77625, 18593),
                (124290, 18593),
                (392793, 18593),
                (18595, 143597),
                (75603, 160582),
                (92746, 132243),
                (300159, 93068),
                (95766, 168008),
                (95766, 370203),
                (124290, 392793),
                (129994, 132243),
                (129994, 286752),
                (257414, 132243),
                (313898, 132243),
                (340073, 132243),
                (442842, 156936),
                (168008, 370203),
                (224985, 370203),
                (247789, 370203),
                (248775, 286752),
                (370203, 366684),
                (370203, 388700),
                (370203, 425589),
                (437724, 370203),
                (437724, 388700),
                (416410, 416414)]

order_df = df.loc[df.duplicated(subset='order_id', keep=False)]
x = []
for b1, b2 in brand_combos:
    b1_brand_count = 0
    b2_brand_count = 0
    temp = b1
    b1 = b2
    b2 = temp
    for order_id, order_df2 in order_df.groupby('order_id'):
        b1_count = order_df2[order_df2['brand'] == b1].shape[0]
        b2_count = order_df2[order_df2['brand'] == b2].shape[0]

        if b1_count > 0:
            b1_brand_count += 1
            if b2_count > 0:
                b2_brand_count += 1
        # if b1_count>0 and b2_count>0:
        #     print(order_id)
        #     print(b1_count)
        #     print(b2_count)
    # for order in order_df:
    #     if (order['brand'] == b1).sum() > 0:
    #         b1_count += 1
    #         if len(order[order['brand'] == b2]) > 0:
    #             b2_count += 1

    # b1_count = 0
    # b2_count = 0
    # for order in order_df:
    #     if (order['brand'] == b1).sum() > 0:
    #         b1_count += 1
    #         if len(order[order['brand'] == b2]) > 0:
    #             b2_count += 1

    # print(f"{iteration} iterations completed")
    # print("Probability of b|a :")
    print(f"{b2} = {b2_brand_count}, {b1} = {b1_brand_count}")
    prob = float("{:.2f}".format(b2_brand_count / b1_brand_count))
    print(f"Probability of b|a {b2}|{b1} :", prob)
    x.append(prob)


import matplotlib.pyplot as plt

x = sorted(x, reverse=True)
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = list(range(1, len(x)+1))

plt.scatter(y, x)
plt.savefig('Probability_400k_3_2.png')
plt.show()
