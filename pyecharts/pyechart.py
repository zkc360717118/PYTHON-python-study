
def drawGraphRelation2():
    from pyecharts import Graph
    import pyecharts.options as opts

    nodes = [
                {"name": "rule1", "symbolSize": 20},
                {"name": "rule2", "symbolSize": 20},
                {"name": "rule3", "symbolSize": 20},
                {"name": "rule4", "symbolSize": 20},
                {"name": "rule5", "symbolSize": 20},
                {"name": "rule6", "symbolSize": 20},
                {"name": "rule7", "symbolSize": 20},
                {"name": "rule8", "symbolSize": 20},
                {"name": "rule9", "symbolSize": 20},
                {"name": "rule1_1", "symbolSize": 10},
                {"name": "rule1_2", "symbolSize": 10},
                {"name": "rule1_3", "symbolSize": 10},
                {"name": "rule2_1", "symbolSize": 10},
                {"name": "rule2_2", "symbolSize": 10},
                {"name": "rule2_1_1", "symbolSize": 10},
                {"name": "rule2_1_2", "symbolSize": 10},
                {"name": "rule2_1_3", "symbolSize": 10},
                {"name": "rule2_2_1", "symbolSize": 10},
                {"name": "rule3_1", "symbolSize": 10},
                {"name": "rule3_2", "symbolSize": 10},
                {"name": "rule0", "symbolSize": 30}
            ]
    links = []

    links.append({"source": "rule0", "target": "rule1"})
    links.append({"source": "rule0", "target": "rule2"})
    links.append({"source": "rule0", "target": "rule3"})
    links.append({"source": "rule0", "target": "rule4"})
    links.append({"source": "rule0", "target": "rule5"})
    links.append({"source": "rule0", "target": "rule6"})
    links.append({"source": "rule0", "target": "rule7"})
    links.append({"source": "rule0", "target": "rule8"})
    links.append({"source": "rule0", "target": "rule9"})
    links.append({"source": "rule1", "target": "rule1_1"})
    links.append({"source": "rule1", "target": "rule1_2"})
    links.append({"source": "rule1", "target": "rule1_3"})
    links.append({"source": "rule2", "target": "rule2_1"})
    links.append({"source": "rule2", "target": "rule2_2"})
    links.append({"source": "rule2_1", "target": "rule2_1_1"})
    links.append({"source": "rule2_1", "target": "rule2_1_2"})

    links.append({"source": "rule2_1", "target": "rule2_2_1"})
    links.append({"source": "rule3", "target": "rule3_1"})
    links.append({"source": "rule3", "target": "rule3_2"})

    graph = Graph("Demo of Pyechart - Rule relationship", init_opts=opts.InitOpts(width='1800px',height='800px'))
    graph.add(
        "",
        nodes,
        links,
        is_label_show=True,
        #graph_repulsion=8000,
        graph_repulsion=80000,
        graph_layout="circular",
        label_text_color=None,
    )
    print("xx")
    graph.render()