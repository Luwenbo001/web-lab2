## Web LAb1

组员：

陆文博	PB22000135

岳梓烨	PB22000159

陈禾一	PB22000176

### Part 1 知识图谱子图三元组的生成和索引值映射

在本次实验中，我们首先需要根据实验一中提供的电影 ID 列表，匹配获得 Freebase 中对应的实体。

因此我们先建立电影的id和电影实体名称的映射，并创建和初始化第一跳子图三元组的集合Graph：

![1](C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\1.png)

然后读取freebase的数据集，将头实体是电影实体的三元组加进Graph中，同时确保三元组的每个实体都以" http://rdf.freebase.com/ns/ "字符串开头，来保证图谱的质量：

![2](C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\2.png)

由于第一跳实体符合上述条件的不多，故可以直接在循环中用    Graph.loc[len(Graph)]=list   直接添加到Graph中。

由此我们初步得到了第一跳的子图，接下来我们分别对其头尾实体和关系进行计数：

![3](C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\3.png)

然后我们采用了20核的设置，筛掉了出现次数不超过50次的头实体和尾实体 ：

<img src="C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\4.png" alt="4" style="zoom:67%;" /><img src="C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\5.png" alt="5" style="zoom:67%;" />

最后删掉出现次数小于50次的关系，并重置索引值：

![6](C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\6.png)

由此我们得到了由一跳生成的子图firstjump.csv。

接下来我们需要根据movie_id_map.txt提供的映射关系，将得到的子图映射为由索引值构成的三元组。

首先我们先分别得到电影实体到id，id到映射id的字典：

![7](C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\7.png)

然后我们就可以对firstjump.csv生成对应的kg_final1.txt了:

<img src="C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\8.png" alt="8" style="zoom: 50%;" /><img src="C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\9.png" alt="9" style="zoom: 50%;" />

得到的kg_final1.txt的片段如图所示：

<img src="C:\Users\DELL\Desktop\大三计算机作业与实验\WEB信息处理与应用\实验\Lab2\web-lab2\baseline\report_pictures\10.png" alt="10" style="zoom:67%;" />

### Part 2 不同的设计的图谱嵌入方法对知识感知推荐性能的影响

### Part 3 对比分析基础推荐方法和知识感知推荐的实验结果差异

