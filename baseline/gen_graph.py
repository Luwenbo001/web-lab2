import gzip
import pandas as pd
from tqdm import *
movie_entity = {}
with open('douban2fb.txt', 'rb') as f:
    for line in f:
        line = line.strip()
        list = line.decode().split('\t')
        movie_entity[list[1]] = list[0]

Graph=pd.DataFrame({"head_entity":[],"relation":[],"tail_entity":[]})

cons_str=r"<http://rdf.freebase.com/ns/"
with gzip.open('freebase_douban.gz', 'rb') as f:
    for line in tqdm(f):
        line = line.strip()
        list = line.decode().split('\t')[:3]
        if(cons_str not in list[0]) or (cons_str not in list[2]):
            continue
        head = list[0][len(cons_str):].strip('>')
        if head in movie_entity.keys():
            Graph.loc[len(Graph)]=list
delete_line=[]
head_count=Graph["head_entity"].value_counts()
tail_count=Graph["tail_entity"].value_counts()
relation_count=Graph["relation"].value_counts()

line_index=0
for head_entity in Graph["head_entity"]: 
    if head_entity in head_count:
        head_num=head_count[head_entity]
    else:
        head_num=0
    if head_entity in tail_count:
        tail_num=tail_count[head_entity]
    else:
        tail_num=0
    total_num=head_num+tail_num
    if(total_num<20):
        if(line_index not in delete_line):
            delete_line.append(line_index)
    line_index=line_index+1

line_index = 0
for tail_entity in Graph["tail_entity"]: 
    if tail_entity in head_count:
        head_num=head_count[tail_entity]
    else:
        head_num=0
    if tail_entity in tail_count:
        tail_num=tail_count[tail_entity]
    else:
        tail_num=0
    total_num=head_num+tail_num
    if(total_num<20):
        if(line_index not in delete_line):
            delete_line.append(line_index)
    line_index=line_index+1
    
line_index=0
for relation in Graph["relation"]: 
    total_num=relation_count[relation]
    if(total_num<50):
        if(line_index not in delete_line):
            delete_line.append(line_index)
    line_index=line_index+1

Graph.drop(index=delete_line,axis=0,inplace=True)
Graph.reset_index(drop=True, inplace=True)

Graph.to_csv("firstjump.csv")
cons_str=r"<http://rdf.freebase.com/ns/"

Graph=pd.read_csv(filepath_or_buffer="firstjump.csv",usecols=["head_entity","relation","tail_entity"])
