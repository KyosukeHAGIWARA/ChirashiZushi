#ちらしずし
<img src="https://github.com/KyosukeHagiwara/ChirashiZushi/blob/master/chirashizushi.png" width="200px">
##Description
+ カスミのチラシはカスミHPから見れますが、毎回毎回見に行くのも何なので、チラシの画像だけtwitterで見れればなぁと思って作りました。
+ HPをスクレイピングしてpdf拾ってきてpngに直して投稿みたいなちょっとめんどくさいことやってます。単に近道を知らないだけです。
+ pdf->pngはImagemagickを使いました。丸パクさせてもらったやつ->[ImageMagickでPDFを画像に変換する](http://qiita.com/polikeiji/items/cc0929bc0171b6348f33 "Qiita")
+ 他にもちょこちょこパクらせてもらったところもアリそうですがキリがないのでアレです。
+ 単にHTMLを拾ってくるだけだとチラシデータのリンクが手に入らなかったので、一度electronでchromiumに描画させるデータをローカルに保存して、それを美しいスープにあたためてなんやかんやしています。こういうのってどんなのが近道なんですかね。教えて下さい。
+ あとは適当にpythonで書きました。
+ ぐっちゃぐちゃです。リファクタリングは今度またします。
+ マルモ学園店にも対応しました。

##Usage
+ 毎日9/13/17時頃にその時発表されているチラシをtweetします。
+ それ以外にめぼしい機能はありません。
+ 直したい点もちょくちょくあるのでどうにかしたいです。

よろしくおねがいします。

##License
MIT

