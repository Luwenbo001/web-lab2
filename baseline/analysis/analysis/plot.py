import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 读入数据
base = pd.read_csv('base.tsv', sep='\t')
add = pd.read_csv('add.tsv', sep='\t')
mul = pd.read_csv('mul.tsv', sep='\t')
joint = pd.read_csv('joint.tsv', sep='\t')
#设置绘图风格
plt.style.use('ggplot')
epoch = base.epoch_idx
print(epoch)
recall5_base = base.recall_5
recall10_base = base.recall_10
ndcg5_base = base.ndcg_5
ndcg10_base = base.ndcg_10
print(recall5_base)
recall5_add = add.recall_5
recall10_add = add.recall_10
ndcg5_add = add.ndcg_5
ndcg10_add = add.ndcg_10
print(recall5_add)
recall5_mul = mul.recall_5
recall10_mul = mul.recall_10
ndcg5_mul = mul.ndcg_5
ndcg10_mul = mul.ndcg_10
recall5_joint = joint.recall_5
recall10_joint = joint.recall_10
ndcg5_joint = joint.ndcg_5
ndcg10_joint = joint.ndcg_10
# 绘制水平交错条形图
# bar_width = 0.1
# plt.bar(x = np.arange(len(epoch)), height = recall5_base, label = 'base_recall@5', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width, height = recall5_add, label = 'add_recall@5', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*2, height = recall10_base, label = 'base_recall@10', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*3, height = recall10_add, label = 'add_recall@10', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*4, height = ndcg5_base, label = 'base_ndcg@5', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*5, height = ndcg5_add, label = 'add_ndcg@5', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*6, height = ndcg10_base, label = 'base_ndcg@10', width = bar_width)
# plt.bar(x = np.arange(len(epoch))+bar_width*7, height = ndcg10_add, label = 'add_ndcg@10', width = bar_width)

bar_width = 0.06
plt.bar(x = np.arange(len(epoch))+bar_width*0, height = recall5_add, label = 'add_recall@5', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*1, height = recall5_mul, label = 'mul_recall@5', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*2, height = recall5_joint, label = 'joint_recall@5', width = bar_width)

plt.bar(x = np.arange(len(epoch))+bar_width*4, height = recall10_add, label = 'add_recall@10', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*5, height = recall10_mul, label = 'mul_recall@10', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*6, height = recall10_joint, label = 'joint_recall@10', width = bar_width)

plt.bar(x = np.arange(len(epoch))+bar_width*8, height = ndcg5_add, label = 'add_ndcg@5', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*9, height = ndcg5_mul, label = 'mul_ndcg@5', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*10, height = ndcg5_joint, label = 'joint_ndcg@5', width = bar_width)

plt.bar(x = np.arange(len(epoch))+bar_width*12, height = ndcg10_add, label = 'add_ndcg@10', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*13, height = ndcg10_mul, label = 'mul_ndcg@10', width = bar_width)
plt.bar(x = np.arange(len(epoch))+bar_width*14, height = ndcg10_joint, label = 'joint_ndcg@10', width = bar_width)

# 添加x轴刻度标签（向右偏移0.4）
plt.xticks(np.arange(14)+0.4, epoch)
# 添加图形标题
plt.title('general table')
# 添加图例
plt.legend()
# 显示图形
plt.show()
