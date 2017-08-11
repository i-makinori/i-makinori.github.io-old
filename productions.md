---

layout: default
---


# 過去の異物
[github](https://github.com/i-makinori)即ち、自分が作った作品達のうち、最も力作にあたるものを紹介していく。何故遺物では無いのかって?それは、貴方が此れの存在(及び存在しないこと)を仮定したからだ

## 点に接触するゲーム
![]({{site.url}}/assets/coin_gather_game.png)

青色の点を、桃色や黒色の点に接触させるだけの簡単なゲーム。  
もちろんAI(階層型ニューラルネットだが)を搭載させる実験も行っている。  
マルチエージェントにした上で、Forestを積みたいという野望に常に駆られている  

[github](https://github.com/i-makinori/coin_gather_game)  
[ブログ書きました](http://ikemaki.hatenablog.com/entry/2017/07/21/192159)


## パズル組み立て支援システム
![assets/procon_solve.png]({{site.url}}/assets/procon_solve.png)

[第27回 高専プロコン 競技部門](https://www.google.co.jp/search?q=%E7%AC%AC27%E5%9B%9E+%E9%AB%98%E5%B0%82%E3%83%97%E3%83%AD%E3%82%B3%E3%83%B3+%E7%AB%B6%E6%8A%80%E9%83%A8%E9%96%80)(おいgoogle)で作成したプログラム  
物理的に与えられたパズルを、各種の処理の後に、物理的に埋めていく競技である。  
自分は、パズルのピースを誤差を含むベクトルの情報として受け取って、最も接合する可能性の高い組み合わせを表示していくプログラムを作成した。  

- [ブログ](http://ikemaki.hatenablog.com/entry/2016/10/10/234703)
  - 何時・何をやって、どのような反省を持ったかを記述し、プログラムの概要を説明している
- [github](https://github.com/i-makinori/procon_solve)
  - `doc/` 以下の日本語は、古い方のアルゴリズムのメモである
  - `wiki` は何を担当しているかを説明している。(おい大会運営!)


## サッカーをするロボット(制御プログラム)
![]({{site.url}}/assets/soccer_robo.png)

理想
- raspberry PIを搭載
- 三方向にカメラを搭載
- 深層学習によるリアルタイムフィールド解析
- ロボット間のリアルタイム通信
-> 敵を完封

現実
- 動きませんでした、、、。

[github](https://github.com/i-makinori/redsight)

現在も絶賛製作中成


## makinori.github.io
即ちこのページ。　ある日に何らかの理由で一日にしてβ版が出来上がってしまい、今日もこうやって更新をしている。

何を言っているんだ私は

- [github](https://github.com/i-makinori/i-makinori.github.io) このサイトのソースが書かれている
- [commit log](https://github.com/i-makinori/i-makinori.github.io/commits) このサイトが如何にして立ち上がり、如何にして放置されたかを垣間見ることが出来る

# レポート・プレゼンなど

- [情報技術研究部の新入生歓迎会でのプレゼン]({{site.url}}/assets/welcome_presen.pdf)
  - その場のノリで作ってしまった。部員向けの自己紹介のプレゼン
- ["学校時代一番頑張ったことはなんですか？５分程度で説明して下さい"と言われて作ったプレゼンと原稿]({{site.url}}/assets/5min_intro.pdf)
  - カットされている部分も結構ある。5分で収めるのは難しい。
- ["存在が消された記事"]({{site.uel}}/404.html)
