var args = phantom.args;
url = args[0]

// headlessブラウザを作成
var page = require('webpage').create();

//URLを開く
page.open(url, function(status) {
  //ブラウザ内でJSを介してデータを取得
  //console.log("weiwei")
  console.log(page.content);
  phantom.exit();
});
