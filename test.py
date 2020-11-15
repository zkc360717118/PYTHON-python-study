g = [{
    "name": "a",
    "child": "b"
},

    {
        "name": "c1",
        "child": "c1_2"
    },
    {
        "name": "c1",
        "child": "c1_1"
    },
    {
        "name": "b",
        "child": "c1"
    },
    {
        "name": "b",
        "child": "c2"
    },
]


def find_child(name, child_name, g):
    if not g: return {child_name: []}
    l = []
    g = [node for node in g if node['name'] != name]
    child_node_list = [node for node in g if node['name'] == child_name]
    other_list = [node for node in g if node['name'] != child_name and node not in child_node_list]
    child_list = [find_child(child_name, node['child'], other_list) for node in child_node_list]

    #     tmp_l=[find(x,[for x in g if x['name']!=child_name])]
    return {'name': child_name,
            'children': child_list}


root = g[0]

res = {'name': root['name'],
       'children': [
           find_child(root['name'], root['child'], g[1:])
       ]
       }
print(res)