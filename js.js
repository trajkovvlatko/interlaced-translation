$(document).ready(function(){
  $(".translate").click(function(){
    var text = $.trim($(".text").val());
    var sentences = text.split(".");
    var lang = $(".lang").val()

    $.each(sentences, function(i, sentence){
      sentences[i] = $.trim(sentence);
    });
    sentences = $.grep(sentences,function(n){ return(n) });
    text = $.trim(sentences.join(". "));

    $.post("http://localhost:1234", {
      text: text,
      lang: lang
    }, function(data){
      $(".sentences").html("");
      var translations = data.split(".");
      $.each(translations, function(i, item){
        $(".sentences").append("<li class='original'>" + sentences[i] + ".</li>")
        $(".sentences").append("<li class='translation'>" + item + ".</li>")
      });
    });
  });


  $("body" ).on( "click", ".original", function() {
    $(this).next().toggle();
  });

});
