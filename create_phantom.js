var system = require('system');
var args = system.args;
url = args[1];

// headlessブラウザを作成
var page = require('webpage').create();

//URLを開く
page.open(url, function(status) {
  //ブラウザ内でJSを介してデータを取得
  console.log(page.content);
  phantom.exit();
});
