var window_h = $(window).height();
$("#wh span").text(window_h);

//スクロールイベント
//header固定
$(window).on('scroll',function(){     
  var heroBottom = $('header').height();
  if($(window).scrollTop() > heroBottom){
      $('.nav-list').addClass('header-fixed'); 
  }
  else{
    $('.nav-list').removeClass('header-fixed');   
  }
});

$(window).trigger('scroll');

function switchByWidth(){
  if (window.matchMedia('(max-width: 767px)').matches) {
      //スマホ処理
      //service フェードイン処理
      $(window).on("scroll", function() {
        var scroll_top = $(window).scrollTop();
        $("#scroll span").text(scroll_top);

        $(".box").each(function() {
          var elem_pos = $(this).offset().top;
          $(this).find(".box_pos span").text(Math.floor(elem_pos));
        　
          //どのタイミングでフェードインさせるか
          if (scroll_top >= elem_pos - window_h+200) {
            $(this).addClass("fadein");
          } else {
            $(this).removeClass("fadein");
            ;
          }
        });
      });
  } else if (window.matchMedia('(min-width:768px)').matches) {
      //PC処理
      //service フェードイン処理
      $(window).on("scroll", function() {
        var scroll_top = $(window).scrollTop();
        $("#scroll span").text(scroll_top);

        $(".box").each(function() {
          var elem_pos = $(this).offset().top;
          $(this).find(".box_pos span").text(Math.floor(elem_pos));
        　
          //どのタイミングでフェードインさせるか
          if (scroll_top >= elem_pos - window_h+200) {
            $(this).addClass("fadein");
          } else {
            $(this).removeClass("fadein");
          }
        });
      });
  }
}

//ロードとリサイズの両方で同じ処理を付与する
window.onload = switchByWidth;
window.onresize = switchByWidth;

//header表示場所
$(document).ready(function () {
  hsize = $(window).height();
  $("header").css("height", hsize+50 + "px");
});
$(window).resize(function () {
  hsize = $(window).height();
  $("header").css("height", hsize+50 + "px");
});

$(document).ready(function () {
  hsize = $(window).height();
  $("#header-title").css("height", hsize + "px");
  $("#header-title h1").css("top", hsize/2 -100 + "px");
});
$(window).resize(function () {
  hsize = $(window).height();
  $("#header-title").css("height", hsize + "px");
  $("#header-title h1").css("top", hsize/2 -100 + "px");
});