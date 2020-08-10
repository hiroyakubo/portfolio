$(document).ready(function () {
    hsize = $(window).height();
    $(".monitor-height").css("height", hsize + "px");
    $(".monitor-height h1").css("padding-top", hsize/2 -100 + "px");
    $(".monitor-height h1").css("padding-bottom", hsize/2 -100 + "px");
    $(".monitor-height p").css("padding-top", hsize/2 -100 + "px");
    $(".monitor-height p").css("padding-bottom", hsize/2 -100 + "px");
  });