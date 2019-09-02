function bird(){
    var mainNode = d3.select("#vizualizator").node();
    MutationObserver = window.MutationObserver || window.WebKitMutationObserver;

    var observer = new MutationObserver(function(mutations, observer) {
        var main = d3.select("#vizualizator").html();
        var bird = d3.select("#bird").html(main);
        
        var mainWidth = d3.select("#vizualizator").select("g").node().getBBox().width;
        var birdWidth = $("#bird")[0].clientWidth;

        var mainHeight = d3.select("#vizualizator").select("g").node().getBBox().height;
        var birdHeight = $("#bird")[0].clientHeight;

        var scaleWidth = birdWidth / mainWidth;
        var scaleHeight = birdHeight / mainHeight;

        if(scaleWidth < scaleHeight){
            scale = scaleWidth;
        }else{
            scale = scaleHeight;
        }   

        var x = d3.select("#bird").select("g").node().getBBox().x;
        var y = d3.select("#bird").select("g").node().getBBox().y;

        d3.select("#bird").select("g").attr("transform", "translate ("+[-x*scale, -y*scale]+") scale("+ scale +")");
    });

    observer.observe(mainNode, {
        subtree: true,
        attributes: true
    });
}