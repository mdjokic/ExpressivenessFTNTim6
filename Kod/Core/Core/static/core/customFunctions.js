$(document).ready(function f(){
    var data; 
    $("#filter").on("click", function(){
            filterData(data);
            tree(data);
            doDraw(data);
            bird();
    });  
    $("#search").on("click", function(){
            searchData(data);
            tree(data);
            doDraw(data);
            bird();
    });  
    $("#save-data").on("click", function() {
        saveData();
    });
    $.ajax({
    url: 'http://localhost:8000/core/getGraph/',
    datatype: 'json',
    type: 'GET',
    success: function(d){
            data = transformData(d);
            draw(data);
    }
    });          
}); 

function doDraw(data){
    return;
}

function draw(data){
    bird();
    panZoom();
    tree(data);
    doDraw(data);
}

function transformData(d){
        var graph = d;
        var data = {
            "nodes":[],
            "links":[]
            }
        $.each(graph.graph.nodes, function(type, list){
            $.each(list, function(i, node){
                node.x = 0;
                node.y = 0;
                node.type = type;
                node.found = false;
                node.hidden = false;
                data.nodes.push(node);
            });
        });

        $.each(graph.graph.edges, function(type, list){
            $.each(list, function(index, edge){
                var src = edge.node1;
                var tgt = edge.node2;
                var srcIndex = NaN;
                var tgtIndex = NaN;
                $.each(data.nodes, function(i, node){
                    if(src == node.id){
                        srcIndex = i;
                    }
                    if(tgt == node.id){
                        tgtIndex = i;
                    }
                })

                data.links.push({
                    source: srcIndex,
                    target: tgtIndex,
                    hidden: false,
                    type: type
                });
            });
        });
        return data;
    }