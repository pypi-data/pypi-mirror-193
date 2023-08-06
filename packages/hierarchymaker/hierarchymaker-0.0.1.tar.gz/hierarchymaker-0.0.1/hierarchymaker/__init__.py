import json
from graphviz import Digraph


import sys

#data = sys.argv[1]

#file_path="hier.json"
#file path

def plot_hierarchy():
     file_path=input("Enter the full path of Json file path-->  ")


     with open(file_path) as f:
       j = json.load(f)
     g = Digraph(format='png')
     g.attr(rankdir='TB')

     def plot_hierarchy2(json_data=j, graph=g, parent_id=None):
          shape = "rectangle"
          color = None

          if json_data["type"] == "TENANT":
            color = "gray"
          elif json_data["type"] == "BUSINESS_GROUP":
            color = "blue"
          elif json_data["type"] == "APPLICATION":
            color = "green"
          elif json_data["type"] == "ASSET_CATEGORY":
            color = "yellow"
          elif json_data["type"] == "ASSET":
            color = "purple"

          if parent_id is None:
            graph.node(str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color, shape=shape)
          else:
            graph.node(str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color, shape=shape)
            graph.edge(str(parent_id), str(json_data["nodeId"]), label=json_data["name"], style="filled", color=color,
                   shape=shape)

          if "child" in json_data:
              for node in json_data["child"]:

                  plot_hierarchy2(node, graph, parent_id=json_data["nodeId"])



     plot_hierarchy2(j, g)

     g.render("output/Hier_Img")
if __name__ == "__main__":
   plot_hierarchy()