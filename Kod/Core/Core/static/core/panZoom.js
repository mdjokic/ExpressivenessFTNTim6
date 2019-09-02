function panZoom(){
    var svg = d3.select("#vizualizator")
    .call(d3.behavior.zoom().on("zoom", function (d, i) {      
        svg.attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")");                 
    }))
    .append("g"); 
}