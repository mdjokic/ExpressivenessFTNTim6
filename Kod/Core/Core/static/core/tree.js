function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

function tree(data) {

        $('#treeview').empty();

        if(data != null) {
            let topLevel = [];
            $.each(data.links, function (i, link) {
                if(topLevel.indexOf(link.source) === -1){
                    topLevel.push(link.source);
                    let name = "";
                    let li = "";
                    if(!data.nodes[link.source].hidden){
                        var myEle = document.getElementById(link.source + "li");
                        if(myEle != null) {
                            li = '<ul class="list-group child notFound" id="' + link.source +'liUL"> </ul>';
                            name = "#" + link.source +"li";
                            $(name).append(li);

                            if(data.nodes[link.source].found)
                                myEle.setAttribute("class", "list-group-item parent boldFound");
                            else
                                myEle.setAttribute("class", "list-group-item parent notFound");
                            name += 'UL';
                        }else{
                            if(data.nodes[link.source].found){
                               li  = ('<li class="list-group-item parent boldFound" id= "' + link.source + 'li">' + data.nodes[link.source].name + "</li>");
                            }else{
                                li  = ('<li class="list-group-item parent" id= "' + link.source + 'li">' + data.nodes[link.source].name + "</li>");
                            }
                            $('#treeview').append(li);

                            li = '<ul class="list-group child notFound" id="' + link.source +'liUL"> </ul>';
                            name = "#" + link.source +"li";
                            $(name).append(li);

                            name += 'UL';
                         }
                     }
                    $.each(data.links, function (i, link2) {
                        if(link2.source == link.source){
                            let ful = link.source + "li";
                            if(!data.nodes[link.source].hidden){
                                if(!data.nodes[link2.target].hidden){
                                    if(data.nodes[link2.target].found){
                                        li = '<li class="list-group-item boldFound" id= "' + link2.target + 'li">' + data.nodes[link2.target].name +'</li>';
                                    }else {
                                        li = '<li class="list-group-item notFound" id= "' + link2.target + 'li">' + data.nodes[link2.target].name +'</li>';
                                    }
                                    $(name).append(li);
                                }
                            }else{
                                if(!data.nodes[link2.target].hidden){
                                    if(data.nodes[link2.target].found){
                                        li  = ('<li class="list-group-item boldFound" id= "' + link2.target + 'li">' +  data.nodes[link2.target].name + "</li>");
                                    }else{
                                        li  = ('<li class="list-group-item" id= "' + link2.target + 'li">' + data.nodes[link2.target].name + "</li>");
                                    }
                                    $('#treeview').append(li);
                                 }
                            }
                        }
                    });
                  }
                });

                //provera cvorova koji nemaju vezu

                 $.each(data.nodes, function (i, node) {
                    name = "#" + i + "li";
                    if($(name).length <= 0){
                           if(!node.hidden){
                                if(node.found){
                                    li  = ('<li class="list-group-item boldFound" id= "' + i + 'li">' +  node.name + "</li>");
                                }else{
                                    li  = ('<li class="list-group-item" id= "' + i + 'li">' + node.name + "</li>");
                                }
                                $('#treeview').append(li);
                             }
                       }
                   });

             }

        $(document).ready(function(){
        let parents = document.getElementsByClassName("parent");
        let i;

        for (i = 0; i < parents.length; i++) {
            parents[i].addEventListener("click", function(event) {
            event.stopPropagation();
            this.querySelector(".child").classList.toggle("active");
            this.classList.toggle("parent-down");
            });
        }

        });
};