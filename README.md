
# gdbの使い方を学ぶためのROS 2サンプルノード

- [gdbの使い方を学ぶためのROS 2サンプルノード](#gdbの使い方を学ぶためのros-2サンプルノード)
  - [gdbを使うための準備](#gdbを使うための準備)
    - [パッケージをクローンする](#パッケージをクローンする)
    - [CMAkeLists.txtにコンパイルオプションを追加する](#cmakeliststxtにコンパイルオプションを追加する)
    - [パッケージをビルドする](#パッケージをビルドする)
  - [gdbなしでノードを実行する](#gdbなしでノードを実行する)
  - [gdbありでノードを実行する](#gdbありでノードを実行する)
    - [Ctrl+Cでノードを停止](#ctrlcでノードを停止)
    - [Enterを押しても何も起きない](#enterを押しても何も起きない)
    - [continueでノードを再開](#continueでノードを再開)
    - [quitでgdbを終了](#quitでgdbを終了)
  - [ブレークポイントを設定して、ノードの動きを止める](#ブレークポイントを設定してノードの動きを止める)
    - [breakを使って、関数を実行するタイミングで止める](#breakを使って関数を実行するタイミングで止める)
    - [nextで1行ずつコードを実行する](#nextで1行ずつコードを実行する)
    - [stepで1行ずつコードを実行し、RCLCPP\_INFOの中に潜り込む](#stepで1行ずつコードを実行しrclcpp_infoの中に潜り込む)
    - [info breakpointsでブレークポイントの一覧を表示する](#info-breakpointsでブレークポイントの一覧を表示する)
    - [deleteでブレークポイントを削除する](#deleteでブレークポイントを削除する)
    - [break (ファイル名):(行番号)でソースコードの特定の行にブレークポイントを設定する](#break-ファイル名行番号でソースコードの特定の行にブレークポイントを設定する)
  - [変数の値を見る](#変数の値を見る)
    - [ブレークポイントの設定](#ブレークポイントの設定)
    - [printで変数の値を見る](#printで変数の値を見る)
    - [break if で条件付きブレークポイントを設定する](#break-if-で条件付きブレークポイントを設定する)
    - [setで変数を書き換える](#setで変数を書き換える)
  - [ブレークポイントを設定した状態でノードを起動する](#ブレークポイントを設定した状態でノードを起動する)
  - [Segmentation faultが起こる原因を探る](#segmentation-faultが起こる原因を探る)
    - [バグが仕込まれたノードをgdbありで実行する](#バグが仕込まれたノードをgdbありで実行する)
    - [【要ヘルプ】backtrace コマンドで異常終了するまでの軌跡をたどる](#要ヘルプbacktrace-コマンドで異常終了するまでの軌跡をたどる)


## gdbを使うための準備

### パッケージをクローンする

```sh
$ cd ~/ros2_ws
$ git clone https://github.com/ShotaAk/cpp_pubsub_gdb.git
```

### CMAkeLists.txtにコンパイルオプションを追加する

```cmake
add_compile_options(-g)
```

### パッケージをビルドする

```sh
$ cd ~/ros2_ws
$ colcon build
```

## gdbなしでノードを実行する

トピックのPublisher（`talker`）

```sh
$ ros2 run cpp_pubsub_gdb talker
[INFO] [1676386306.238464629] [minimal_publisher]: Publishing: 'Hello, world! 0'
[INFO] [1676386306.738459235] [minimal_publisher]: Publishing: 'Hello, world! 1'
[INFO] [1676386307.238401345] [minimal_publisher]: Publishing: 'Hello, world! 2'
[INFO] [1676386307.738453686] [minimal_publisher]: Publishing: 'Hello, world! 3'
```

トピックのSubscriber（`listener`）

```sh
$ ros2 run cpp_pubsub_gdb listener
[INFO] [1676386320.738795411] [minimal_subscriber]: I heard: 'Hello, world! 29'
[INFO] [1676386321.238512059] [minimal_subscriber]: I heard: 'Hello, world! 30'
[INFO] [1676386321.738819764] [minimal_subscriber]: I heard: 'Hello, world! 31'
[INFO] [1676386322.238853708] [minimal_subscriber]: I heard: 'Hello, world! 32'
```

## gdbありでノードを実行する

`talker`は変更なし

```sh
$ ros2 run cpp_pubsub_gdb talker
```

`listner`をgdbありで実行する

```sh
$ ros2 run --prefix 'gdb -ex run --args' cpp_pubsub_gdb listener      

GNU gdb (Ubuntu 12.1-0ubuntu1~22.04) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from /home/shotaak/hoge_ws/install/cpp_pubsub_gdb/lib/cpp_pubsub_gdb/listener...
Starting program: /home/shotaak/hoge_ws/install/cpp_pubsub_gdb/lib/cpp_pubsub_gdb/listener 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff68a2640 (LWP 7092)]
[New Thread 0x7ffff60a1640 (LWP 7093)]
[New Thread 0x7ffff5819640 (LWP 7094)]
[New Thread 0x7ffff5018640 (LWP 7095)]
[New Thread 0x7ffff4817640 (LWP 7096)]
[New Thread 0x7ffff4016640 (LWP 7097)]
[New Thread 0x7ffff3815640 (LWP 7098)]
[New Thread 0x7ffff3014640 (LWP 7099)]
[New Thread 0x7ffff2733640 (LWP 7100)]
[New Thread 0x7ffff1e96640 (LWP 7101)]
[INFO] [1676386557.173134623] [minimal_subscriber]: I heard: 'Hello, world! 203'
[INFO] [1676386557.673330333] [minimal_subscriber]: I heard: 'Hello, world! 204'
[INFO] [1676386558.173299070] [minimal_subscriber]: I heard: 'Hello, world! 205'
[INFO] [1676386558.673030019] [minimal_subscriber]: I heard: 'Hello, world! 206'
[INFO] [1676386559.173356053] [minimal_subscriber]: I heard: 'Hello, world! 207'
[INFO] [1676386559.672940593] [minimal_subscriber]: I heard: 'Hello, world! 208'
...
```

### Ctrl+Cでノードを停止

`Ctrl+C`を押してもノードはシャットダウンされない。

```sh
[INFO] [1676386561.173294316] [minimal_subscriber]: I heard: 'Hello, world! 211'
[INFO] [1676386561.673362125] [minimal_subscriber]: I heard: 'Hello, world! 212'
^C
Thread 1 "listener" received signal SIGINT, Interrupt.
__futex_abstimed_wait_common64 (private=0, cancel=true, abstime=0x0, op=393, expected=0, futex_word=0x555555926f10) at ./nptl/futex-internal.c:57
57	./nptl/futex-internal.c: そのようなファイルやディレクトリはありません.
(gdb) 
```

`(gdb)`と表示されている間は、gdbのコマンドをいろいろ実行できる。

### Enterを押しても何も起きない

gdbのコマンドを入力してないので改行されるだけ

```sh
Thread 1 "listener" received signal SIGINT, Interrupt.
__futex_abstimed_wait_common64 (private=0, cancel=true, abstime=0x0, op=393, expected=0, futex_word=0x55555592d0e0) at ./nptl/futex-internal.c:57
57	./nptl/futex-internal.c: そのようなファイルやディレクトリはありません.
(gdb) 
(gdb) 
(gdb) 
(gdb) 
(gdb) 
(gdb) 
(gdb) 
```

### continueでノードを再開

ノードを再開するので、トピックのパブリッシュが再開される

```sh
(gdb) 
(gdb) 
(gdb) continue
Continuing.
[INFO] [1676386976.006033567] [minimal_subscriber]: I heard: 'Hello, world! 232'
[INFO] [1676386976.006214015] [minimal_subscriber]: I heard: 'Hello, world! 233'
[INFO] [1676386976.006258028] [minimal_subscriber]: I heard: 'Hello, world! 234'
[INFO] [1676386976.006293492] [minimal_subscriber]: I heard: 'Hello, world! 235'
[INFO] [1676386976.006330565] [minimal_subscriber]: I heard: 'Hello, world! 236'
```

### quitでgdbを終了

Ctrl+Cでノードを停止したあと、quitで終了

```sh
[INFO] [1676386985.494998802] [minimal_subscriber]: I heard: 'Hello, world! 257'
[INFO] [1676386985.995128438] [minimal_subscriber]: I heard: 'Hello, world! 258'
[INFO] [1676386986.494971630] [minimal_subscriber]: I heard: 'Hello, world! 259'
^C
Thread 1 "listener" received signal SIGINT, Interrupt.
__futex_abstimed_wait_common64 (private=0, cancel=true, abstime=0x0, op=393, expected=0, futex_word=0x55555592d084) at ./nptl/futex-internal.c:57
57	in ./nptl/futex-internal.c
(gdb) quit
A debugging session is active.

	Inferior 1 [process 8262] will be killed.

Quit anyway? (y or n) y
```

## ブレークポイントを設定して、ノードの動きを止める

`talker`は変更なし

```sh
$ ros2 run cpp_pubsub_gdb talker
```

`listner`をgdbありで実行する

```sh
$ ros2 run --prefix 'gdb -ex run --args' cpp_pubsub_gdb listener      
```

### breakを使って、関数を実行するタイミングで止める

Ctrl+Cでノードを停止し、`break topic_callback`を実行。

`topic_callback`は、`subscriber_member_function.cpp`に書かれているコールバック関数名。

```sh
[INFO] [1676387174.591286964] [minimal_subscriber]: I heard: 'Hello, world! 14'
^C
Thread 1 "listener" received signal SIGINT, Interrupt.
__futex_abstimed_wait_common64 (private=0, cancel=true, abstime=0x0, op=393, expected=0, futex_word=0x55555592d130) at ./nptl/futex-internal.c:57
57	./nptl/futex-internal.c: そのようなファイルやディレクトリはありません.
(gdb) break topic_callback
Breakpoint 1 at 0x55555556e000: file /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp, line 22.
```

`continue`でノードを再開。そしてすぐに止まる。

```sh
(gdb) continue
Continuing.

Thread 1 "listener" hit Breakpoint 1, MinimalSubscriber::topic_callback (this=0x5555556b1400, msg=...) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp:22
22	    void topic_callback(const std_msgs::msg::String & msg) const
(gdb) 
```

### nextで1行ずつコードを実行する

コールバック関数内で`RCLCPP_INFO()`が実行されていることがわかる。

左端に書かれている数字は、ソースコード内でそのコードが書かれている行番号である。

```sh
22	    void topic_callback(const std_msgs::msg::String & msg) const
(gdb) next
24	      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
(gdb) next
[INFO] [1676387534.216844913] [minimal_subscriber]: I heard: 'Hello, world! 44'
25	    }
```

さらにnext。

とても複雑な出力が見えてくる。

```sh
[INFO] [1676387534.216844913] [minimal_subscriber]: I heard: 'Hello, world! 44'
25	    }
(gdb) next
std::__invoke_impl<void, void (MinimalSubscriber::*&)(std_msgs::msg::String_<std::allocator<void> > const&) const, MinimalSubscriber*&, std_msgs::msg::String_<std::allocator<void> > const&> (__f=@0x55555591f6e0: (void (MinimalSubscriber::*)(const MinimalSubscriber * const, const std_msgs::msg::String_<std::allocator<void> > &)) 0x55555556dfe0 <MinimalSubscriber::topic_callback(std_msgs::msg::String_<std::allocator<void> > const&) const>, __t=@0x55555591f6f0: 0x5555556b1400) at /usr/include/c++/11/bits/invoke.h:75
75	    }
```

これ以上nextを繰り返しても切りがないので、continueを実行してもとに戻す。

```sh
t /usr/include/c++/11/bits/invoke.h:75
75	    }
(gdb) continue
Continuing.

Thread 1 "listener" hit Breakpoint 1, MinimalSubscriber::topic_callback (this=0x5555556b1400, msg=...) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp:22
22	    void topic_callback(const std_msgs::msg::String & msg) const
(gdb) 
```

### stepで1行ずつコードを実行し、RCLCPP_INFOの中に潜り込む

`step`を実行すると、呼び出した関数内のコードも1行ずつ実行できる

```sh
22	    void topic_callback(const std_msgs::msg::String & msg) const
(gdb) step
24	      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
(gdb) step
rclcpp::Logger::get_name (this=0x7fffffffc230) at /opt/ros/humble/include/rclcpp/rclcpp/logger.hpp:140
140	    if (!name_) {
(gdb) step
std::__shared_ptr<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, (__gnu_cxx::_Lock_policy)2>::operator bool (this=0x7fffffffc230) at /usr/include/c++/11/bits/shared_ptr_base.h:1300
1300	      { return _M_ptr != nullptr; }
(gdb) 
```

あまり深く探索してもきりがないので、continueでもとに戻る


```sh
std::__shared_ptr<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, (__gnu_cxx::_Lock_policy)2>::operator bool (this=0x7fffffffc230) at /usr/include/c++/11/bits/shared_ptr_base.h:1300
1300	      { return _M_ptr != nullptr; }
(gdb) continue
Continuing.
[INFO] [1676388053.373434776] [minimal_subscriber]: I heard: 'Hello, world! 1550'

Thread 1 "listener" hit Breakpoint 1, MinimalSubscriber::topic_callback (this=0x5555556b1400, msg=...) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp:22
22	    void topic_callback(const std_msgs::msg::String & msg) const
(gdb) 
```

### info breakpointsでブレークポイントの一覧を表示する

ブレークポイントは複数設定できる。
そのため、各ブレークポイントに番号`Num`が振られる。
今は一つしか設定していないので1番が設定されている。

```sh
(gdb) info breakpoints
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x000055555556e000 in MinimalSubscriber::topic_callback(std_msgs::msg::String_<std::allocator<void> > const&) const 
                                                   at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp:22
	breakpoint already hit 8 times
```

### deleteでブレークポイントを削除する

```sh
(gdb) delete 1
(gdb) info breakpoints
No breakpoints or watchpoints.
```

### break (ファイル名):(行番号)でソースコードの特定の行にブレークポイントを設定する

`subscriber_member_function.cpp`の24行目で止めてみる。
ファイル名を入力するのは大変なので、`TAB`を使って補完しよう。

```sh
(gdb) break subscriber_member_function.cpp:24
Breakpoint 2 at 0x55555556e00f: file /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp, line 24.
(gdb) continue
Continuing.

Thread 1 "listener" hit Breakpoint 2, MinimalSubscriber::topic_callback (this=0x5555556b1400, msg=...) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/subscriber_member_function.cpp:24
24	      RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
(gdb) 
```

## 変数の値を見る

`talker`をgdbありで実行する

```sh
$ ros2 run --prefix 'gdb -ex run --args' cpp_pubsub_gdb talker
```

`listner`をgdbなしで実行する

```sh
$ ros2 run cpp_pubsub_gdb listener
```

### ブレークポイントの設定

timer_callback関数にブレークポイントを設定する

関数名を入力するのは大変なので、`TAB`を使って補完しよう。


```sh
(gdb) break timer_callback() 
Breakpoint 1 at 0x55555556254f: file /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp, line 30.
```

### printで変数の値を見る

`continue`でノード再開し、コールバック関数のところで止まるのを確認

```sh
(gdb) continue 
Continuing.

Thread 1 "talker" hit Breakpoint 1, MinimalPublisher::timer_callback (this=0x5555556273e0) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp:30
30	    void timer_callback()
```

nextで1行実行

```sh
(gdb) next
32	      auto message = std_msgs::msg::String();
```

さらにnextで1行実行

```sh
(gdb) next
33	      message.data = "Hello, world! " + std::to_string(count_++);
```

ここで`print`コマンドを実行し、変数`count_`の値を見てみよう。
もちろん`TAB`で補完できる。

変数には`55`がセットされていることがわかる。

```sh
(gdb) next
33	      message.data = "Hello, world! " + std::to_string(count_++);
(gdb) print count_ 
$1 = 55
```

`count_++`というコードは、コード実行後に変数をインクリメントするものなので、
次の行では変数の値が56になっているはず

ここでnext。

```sh
(gdb) next
34	      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
```

そして、print。
`count_`がインクリメントされていることがわかる。

```sh
(gdb) next
33	      message.data = "Hello, world! " + std::to_string(count_++);
(gdb) print count_ 
$1 = 55
(gdb) next
34	      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
(gdb) print count_
$2 = 56
```

### break if で条件付きブレークポイントを設定する

`count_`が20になったときにコールバック関数で停止させる。

すでに20以上カウントされているので、`talker`ノードを再起動してから設定する。

```sh
(gdb) break timer_callback() if count_ == 20
Breakpoint 1 at 0x55555556254f: file /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp, line 30.
(gdb) 
```

`continue`して待機。

```sh
(gdb) continue
Continuing.
[INFO] [1676389550.498862236] [minimal_publisher]: Publishing: 'Hello, world! 3'
[INFO] [1676389550.768500542] [minimal_publisher]: Publishing: 'Hello, world! 4'
...
[INFO] [1676389557.767953423] [minimal_publisher]: Publishing: 'Hello, world! 18'
[INFO] [1676389558.268624670] [minimal_publisher]: Publishing: 'Hello, world! 19'

Thread 1 "talker" hit Breakpoint 1, MinimalPublisher::timer_callback (this=0x5555556273e0) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp:30
30	    void timer_callback()
(gdb) 
```

### setで変数を書き換える

変数`count_`を0にリセットしてもう一度挙動を見る

```sh
Thread 1 "talker" hit Breakpoint 1, MinimalPublisher::timer_callback (this=0x5555556273e0) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp:30
30	    void timer_callback()
(gdb) set count_ = 0
```

`continue`して待機。

```sh
(gdb) continue
Continuing.
[INFO] [1676389677.150930111] [minimal_publisher]: Publishing: 'Hello, world! 0'
[INFO] [1676389677.202999622] [minimal_publisher]: Publishing: 'Hello, world! 1'
[INFO] [1676389677.271087618] [minimal_publisher]: Publishing: 'Hello, world! 2'
...

Thread 1 "talker" hit Breakpoint 1, MinimalPublisher::timer_callback (this=0x5555556273e0) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp:30
30	    void timer_callback()
(gdb) 
```

## ブレークポイントを設定した状態でノードを起動する

`gdb`コマンドに`-ex こまんど` を追記すれば、
`gdb`コマンド起動、`こまんど`実行、のように処理される。

`gdb -ex "break hogehoge"`と書けば、ノード実行時に予めブレークポイントを設定できる。

コールバック関数のブレークポイントを設定した状態で、`talker`ノードを実行する。

```sh
$ ros2 run --prefix 'gdb -ex "break timer_callback()" -ex run --args' cpp_pubsub_gdb talker
...
[New Thread 0x7ffff1f10640 (LWP 12145)]

Thread 1 "talker" hit Breakpoint 1, MinimalPublisher::timer_callback (this=0x5555556273e0) at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/publisher_member_function.cpp:30
30	    void timer_callback()
(gdb) 
```

## Segmentation faultが起こる原因を探る

バグが仕込まれたノード`broken_talker`を実行する。

おそらく、どこかのタイミングで`Segmentation fault`が発生する。

```sh
$ ros2 run cpp_pubsub_gdb broken_talker
[INFO] [1676390765.881666083] [minimal_publisher]: Publishing: 'Hello, world! 0'
[INFO] [1676390766.381698622] [minimal_publisher]: Publishing: 'Hello, world! 1'
[INFO] [1676390766.881696680] [minimal_publisher]: Publishing: 'Hello, world! 2'
[INFO] [1676390767.381669244] [minimal_publisher]: Publishing: 'Hello, world! 3'
[INFO] [1676390767.881720553] [minimal_publisher]: Publishing: 'Hello, world! 4'
[INFO] [1676390768.381688073] [minimal_publisher]: Publishing: 'Hello, world! 5'
[INFO] [1676390768.881683671] [minimal_publisher]: Publishing: 'Hello, world! 6'
[INFO] [1676390769.381689962] [minimal_publisher]: Publishing: 'Hello, world! 7'
[INFO] [1676390769.881732028] [minimal_publisher]: Publishing: 'Hello, world! 8'
[INFO] [1676390770.381692104] [minimal_publisher]: Publishing: 'Hello, world! 9'
[INFO] [1676390770.881748970] [minimal_publisher]: Publishing: 'Hello, world! 10'
[INFO] [1676390771.381712072] [minimal_publisher]: Publishing: 'Hello, world! 11'
[INFO] [1676390771.881716686] [minimal_publisher]: Publishing: 'Hello, world! 12'
[ros2run]: Segmentation fault
```


### バグが仕込まれたノードをgdbありで実行する

Segmentation faultが起こると、ノードの実行が自動で停止される。

```sh
$ ros2 run --prefix 'gdb -ex run --args' cpp_pubsub_gdb broken_talker
...
Thread 1 "broken_talker" received signal SIGSEGV, Segmentation fault.
0x00007ffff7eae833 in rclcpp::Executor::get_next_ready_executable_from_map(rclcpp::AnyExecutable&, std::map<std::weak_ptr<rclcpp::CallbackGroup>, std::weak_ptr<rclcpp::node_interfaces::NodeBaseInterface>, std::owner_less<std::weak_ptr<rclcpp::CallbackGroup> >, std::allocator<std::pair<std::weak_ptr<rclcpp::CallbackGroup> const, std::weak_ptr<rclcpp::node_interfaces::NodeBaseInterface> > > > const&) () from /opt/ros/humble/lib/librclcpp.so
(gdb) 
```

### 【要ヘルプ】backtrace コマンドで異常終了するまでの軌跡をたどる

が、、、マルチスレッドなプログラムなので、原因までたどり着けない。。。

解決方法がわかったら記載する


```sh
(gdb) backtrace
#0  0x00007ffff7eae833 in rclcpp::Executor::get_next_ready_executable_from_map(rclcpp::AnyExecutable&, std::map<std::weak_ptr<rclcpp::CallbackGroup>, std::weak_ptr<rclcpp::node_interfaces::NodeBaseInterface>, std::owner_less<std::weak_ptr<rclcpp::CallbackGroup> >, std::allocator<std::pair<std::weak_ptr<rclcpp::CallbackGroup> const, std::weak_ptr<rclcpp::node_interfaces::NodeBaseInterface> > > > const&) ()
   from /opt/ros/humble/lib/librclcpp.so
#1  0x00007ffff7eaea8d in rclcpp::Executor::get_next_executable(rclcpp::AnyExecutable&, std::chrono::duration<long, std::ratio<1l, 1000000000l> >) () from /opt/ros/humble/lib/librclcpp.so
#2  0x00007ffff7eb5f31 in rclcpp::executors::SingleThreadedExecutor::spin() ()
   from /opt/ros/humble/lib/librclcpp.so
#3  0x00007ffff7eb6155 in rclcpp::spin(std::shared_ptr<rclcpp::node_interfaces::NodeBaseInterface>) ()
   from /opt/ros/humble/lib/librclcpp.so
#4  0x00007ffff7eb624f in rclcpp::spin(std::shared_ptr<rclcpp::Node>) ()
   from /opt/ros/humble/lib/librclcpp.so
#5  0x000055555555e768 in main (argc=1, argv=0x7fffffffdd18)
    at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/broken_publisher_member_function.cpp:50
(gdb) 
(gdb) frame 5
#5  0x000055555555e768 in main (argc=1, argv=0x7fffffffdd18)
    at /home/shotaak/hoge_ws/src/cpp_pubsub_gdb/src/broken_publisher_member_function.cpp:50
50	  rclcpp::spin(std::make_shared<MinimalPublisher>());
(gdb) 

```
