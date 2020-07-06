$(document).ready(function(){
    //画面の高さを取得して、変数wHに代入
    var wH = $(window).height(); 
    //div#exampleの高さを取得を取得して、変数divHに代入
    var divH = $('div#intro-header').innerHeight();
    // ボックス要素より画面サイズが大きければ実行
    if(wH > divH){
    	// div#examplに高さを加える
    	$('div#intro-header').css('height',wH+'px'); 
    }
});