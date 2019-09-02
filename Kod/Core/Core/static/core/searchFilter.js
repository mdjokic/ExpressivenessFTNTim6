function searchData(data){
        var txt = $("#txtSearch").val();
        $.each(data.nodes, function(i, node){
            if(node.name.toLowerCase().includes(txt.toLowerCase()) && txt!=""){
                node.found = true;
            }else{
                node.found = false;
            }
        });
    }
    
function filterData(data){
    var txt = $("#txtFilter").val();
    $.each(data.nodes, function(i, node){
        if(!node.name.toLowerCase().includes(txt.toLowerCase()) && txt!=""){
            node.hidden = true;
        }else{
            node.hidden = false;
        }
    }); 
    $.each(data.links, function(i, link){
        if(data.nodes[link.source].hidden == true || data.nodes[link.target].hidden == true){
            link.hidden = true;
        }else{
            link.hidden = false;
        }
    });
}
