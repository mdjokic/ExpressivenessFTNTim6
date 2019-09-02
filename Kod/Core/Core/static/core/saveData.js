function saveData() {
    var fileName = $("#data-name").val();

    if (fileName != "") {
        $.ajax({
            type: "GET",
            url: "../core/saveData/",
            success: function(response) {
                var a = document.createElement("a");
                var JSONfile = new Blob([response.graph], {type : "application/json"});
                a.href = URL.createObjectURL(JSONfile);
                a.download = fileName + ".json"
                a.click();
            }
          })
    }  
}