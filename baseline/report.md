## Web LAb1

组员：

陆文博	PB22000135

岳梓烨	PB22000159

陈禾一	PB22000176

### Part 1 实验过程

在loader_Embedding_based.py 中我按要求实现了 KG 的构建
首先为KG添加逆向三元组，即对于KG中任意三元组(h, r, t)，添加逆向三元组 (t, r+n_relations, h)，并将原三元组和逆向三元组拼接为新的DataFrame，保存在 self.kg_data 中。
根据注释，我们可以完成如下代码
![](./Report_img/594.png)
随后我们根据已有的数据计算出相关系数，实体数和三元组的数量
![](./Report_img/595.png)
根据 self.kg_data 构建字典 self.kg_dict ，其中key为h, value为tuple(t, r)，和字典 self.relation_dict，其中key为r, value为tuple(h, t)。
![](./Report_img/596.png)

在 Embedding_based.py 中我实现 TransE 算法，代码如图
![](./Report_img/597.png)
在calc_cf_loss，calc_score函数中我们尝试通过相加，逐元素乘积，拼接等方式为物品嵌入注入图谱实体的语义信息。
我们设置了一个参数method，通过在训练前修改method的值来实现不同的注入信息方式。
特别要注意的是，拼接的方法会导致的矩阵的维度发生变化，在代码处理的时候注意对齐。
calc_cf_loss函数
![](./Report_img/598.png)
calc_score函数
![](./Report_img/599.png)

### Part 2 不同的设计的图谱嵌入方法对知识感知推荐性能的影响

### Part 3 对比分析基础推荐方法和知识感知推荐的实验结果差异

