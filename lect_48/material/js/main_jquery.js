$(document).ready(function(){
    $('#button_for_jq').click(function(){
        alert('Hello, it is jQuery!)))');
    });
//
    $('#button-hide').click(function(){
        $("#hide-element").hide();
    });
//
    $('#mouse-element2').mouseenter(function(){
        alert("You entered p1!");
    });
//
    $('#button-fadeout').click(function(){
        $("#fadein-element").fadeOut();
        $("#fadein-element").fadeOut("slow");
        $("#fadein-element").fadeOut(3000);
    });
    //
    $('#button-fadein').click(function(){
        $("#fadein-element").fadeIn();
        $("#fadein-element").fadeIn("slow");
        $("#fadein-element").fadeIn(3000);
    });
    //
    $("#button-slide").click(function(){
        $("#slide-element").slideUp();
    });
    //
    $("#button-anim").click(function(){
        $("#anim-element").animate({
            opacity: '0.5',
            height: '250px',
            width: '250px'
        });
    });
    $("#button-anim").click(function(){
        var div = $("#anim-element");
        div.animate({height: '300px', opacity: '0.4'}, "slow");
        div.animate({width: '300px', opacity: '0.8'}, "slow");
        div.animate({height: '100px', opacity: '0.4'}, "slow");
        div.animate({width: '100px', opacity: '0.8'}, "slow");
    });
    $("#button-anim-chain").click(function(){
        $("#anim-element-chain").css("color", "red")
        .slideUp(2000)
        .slideDown(2000);
    });
    //
    $("#button-test-text1").click(function(){
        alert("Text: " + $("#test-text").text());
    });
    $("#button-test-text2").click(function(){
        alert("HTML: " + $("#test-text").html());
    });
    function appendText(){
        var txt1 = "<b>I </b>";                    // Create element with HTML
        var txt2 = $("<i></i>").text("love ");     // Create with jQuery
        var txt3 = document.createElement("b");    // Create with DOM
        txt3.innerHTML = "jQuery!";    // Append the new elements
    }
    //
    $("#button-ajax").click(function(){
        $("#div1").load("demo_text.txt", function(responseTxt, statusTxt, xhr){
            if(statusTxt == "success")
            alert("External content loaded successfully!");
            if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
        });
    });
    //
    //
    $("#button-ajax2").click(function(){
        $.get("demo_test.asp", function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
    //
    $("#button-ajax3").click(function(){
        $.post("demo_test_post.asp",
        {
            name: "Donald Duck",
            city: "Duckburg"
        },
        function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        });
    });
});
//
