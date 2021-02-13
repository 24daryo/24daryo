#　自作のプログラミング言語

##　使い方

```
# テンプレートの宣言
class Vector2{

    public int x = 0, y = 0

    private init(x, y){
        this.x = x
        this.y = y
    }

    private void Manhattan(Vector2 other){
        return abs(x - other.x) + abs(y -other.y)
    }

}

@template{
    +(Vector2 A, Vector2 B){
        return Vector(A.x + B.x, A.y + B.y)
    }
    -(Vector2 A, Vector2 B){
        return Vector(A.x - B.x, A.y - B.y)
    }
    *(number n, Vector2 A){
        return Vector(n * A.x, n * A.y)
    }
}


# 時間軸関数の定義
class Sequence{

    # この場合、タイムレベルはLevel1(一瞬で終了)
    public void Line1(){
        print("Hello World")
    }

    # @waitを付けないと、wait関数はエラーとなる
    # waitは @parallel でないと使用できない
    @wait
    public void Line2(){
        # この場合、タイムレベルはLevel2(有限時間で終了)
        wait(10)
        print("Hello World")
    }

    # 別スレッドで有限時間プログラムを実行する
    # @parallelはどこでも使用できる
    @parallel
    public void Go(){
        Line()
        wait(10)
    }

    #通常で使用する場合
    @wait
    public void main(){
        #シーケンスを定義
        # 順番に実行される
        block = sequence(
            Hello(),
            wait(10),
            Goodbye()
        )

        # シーケンスを実行
        # @singleで同じスレッドで実行
        # 個数が256以上になると警告が出て止まる
        @single core <= block.start() # @parallel属性

        #発動自体はすぐに終了する

        #待機する場合、このように記述
        #なお@asyncがないとエラーになる
        wait(core)
    }

    public void main2(){
        # 並列で実行
        # 全ての中身が終了したら次へ進む
        block = parallelAll(
            wait(10),
            wait(3),
            wait(6)
        )

        #シーケンスを実行
        # @multiで別のスレッドで実行
        # マルチにできる回数以上だと、待機する
        @multi = block.start()

        #この場合、スレッドの終了は10秒後

        #終了をまたない場合は、このように記述
        pass @multi
    }

    public void main3(){
        # 並列で実行
        # 一つでも中身が終了したら次へ進む
        block = parallelOne(
            wait(10),
            wait(3),
            wait(6)
        )

        #シーケンスを実行
        # @coreで別のcpuで実行
        @core = block.start()

        #この場合、スレッドの終了は3秒後
    }

    @wait
    public void main4(){

        block = sequence(
            Hello(),
            wait(10),
            Goodbye()
        )

        @single core <= block.start()

        wait(core)
    }
}

# 時間軸関数の実践例
class UI{
    //フェードインする
    @wait
    void FadeIn(){
        block = sequence(
            print("フェードインします"),
            UI.FadeColor(from=color(1,1,1), to=color(0,0,0), time=0.1),
            print("完了しました")
        )

        @single core = block.start()

        wait(core)
    }

    //フェードアウトする
    @wait
    void FadeOut(){
        block = sequence(
            print("フェードアウトします"),
            UI.FadeColor(from=color(0,0,0), to=color(1,1,1), time=0.1),
            print("完了しました")
        )

        @single core = block.start()

        wait(core)
    }

    #この関数自体は一瞬で抜ける。別のスレッドで走る
    # staticにより重複されず、終了まで次は実行できない
    @parallel
    void Fade(){
        var single = Thread.this
        //var single = Thread.cpu
        //var single = Thread.gpu
        single += FadeIn()
        single += FadeOut()
    }

    void SoundSE(path){

    }

    @single[] thread = @Single()[100]

    void start(){
        thread.add(Sound.mixer[0].play(path))
    }

    void update(){

        string path = "./files/sound1.mp3"
        @parallel se1 = Sound.mixer[0].play(path)     @parallel属性

        if(Input.GetKeyDown(Keycode.A)){

            @overwrite                          #実行中でも上書きして実行する
            se1.start()                         #別スレッドで実行されている

            #これと同じ
            thread[0].stack.clear()
            thread[0].stack.add(parallel)

            #Sound.mixer[1].repeat(path, count=3)
        }
        elif(Input.GetKeyDown(Keycode.B)){
            @onlyidle                           #実行中は発動しない
            se1.start()                         #別スレッドで実行されている

            #これと同じ
            if(thread[0].stack.size == 0){
                thread[0].stack.add(se1)
            }
        }
        elif(Input.GetKeyDown(Keycode.C)){
            @stack                              #スタックされて、終了後に発動
            se1.start()                         #別スレッドで実行されている

            #これと同じ
            thread[0].stack.add(se1)
        }
        elif(Input.GetKeyDown(Keycode.D)){
            @overlay                            #実行中でも重ねて実行する
            se1.start()                         #別スレッドで実行されている

            #これと同じ
            thread.add(se1)
        }
    }
}

#コーディングルール
付属の関数は小文字
自作の関数は大文字
キャメル記法を推奨

```
