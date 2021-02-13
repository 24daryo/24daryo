using System;
using System.Linq;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Input;

namespace GameEngine2D
{
    //オープンで公開するデータはこちらへ
    static class GameSystem
    {
        public static string key = "";
        public static int frameRate = 60;
    }

    class Internal
    {
        //隠蔽したいデータはこちらに記述する
        private static int keySize = Enum.GetNames(typeof(Keycode)).Length;
        private static bool[] keyPrev = new bool[keySize];
        private static bool[] keyNext = new bool[keySize];
        public class InputCore
        {
            public static bool[] KeyPrev
            {
                get
                {
                    return keyPrev;
                }
            }
            public static bool[] KeyNext
            {
                get
                {
                    return keyNext;
                }
            }

            public static Keycode StrToCode(string text)
            {
                if (text == "A") return Keycode.A;
                else if (text == "B") return Keycode.B;
                else if (text == "C") return Keycode.C;
                else if (text == "D") return Keycode.D;
                else if (text == "E") return Keycode.E;
                else if (text == "F") return Keycode.F;
                else if (text == "G") return Keycode.G;
                else if (text == "H") return Keycode.H;
                else if (text == "I") return Keycode.I;
                else if (text == "J") return Keycode.J;
                else if (text == "K") return Keycode.K;
                else if (text == "L") return Keycode.L;
                else if (text == "M") return Keycode.M;
                else if (text == "N") return Keycode.N;
                else if (text == "O") return Keycode.O;
                else if (text == "P") return Keycode.P;
                else if (text == "Q") return Keycode.Q;
                else if (text == "R") return Keycode.R;
                else if (text == "S") return Keycode.S;
                else if (text == "T") return Keycode.T;
                else if (text == "U") return Keycode.U;
                else if (text == "V") return Keycode.V;
                else if (text == "W") return Keycode.W;
                else if (text == "X") return Keycode.X;
                else if (text == "Y") return Keycode.Y;
                else if (text == "Z") return Keycode.Z;

                return Keycode.Other;

            }

        }

        private static async void InputThread()
        {
            await Task.Run(() =>
            {
                var keyStr = Console.ReadKey().Key.ToString();
                var keyCode = InputCore.StrToCode(keyStr);
                var keyIndex = (int)(keyCode);
                keyNext[keyIndex] = true;
                Console.WriteLine(keyIndex);

                //Console.WriteLine(key + "が入力されました");
                InputThread();
            });
        }

        static void Main(string[] args)
        {
            Console.WriteLine("プログラム開始");
            //スレッド起動
            InputThread();

            int time = (1000 / GameSystem.frameRate);

            //時間幅の無限ループ起動
            while (true)
            {
                Thread.Sleep(time);//フレーム待機
                //Console.WriteLine(count + "回目のループ処理");

                MyMain.Update();//アップデート関数

                //ループ解除
                if (GameSystem.key == "Enter")
                {
                    break;
                }

                Reset();//リセット処理
            }
            Console.WriteLine("プログラム終了");
        }

        private static void Reset()
        {
            //入力を更新
            keyNext = keyPrev;
            keyPrev = new bool[keySize];
        }

    }

    //ここにメイン処理を記述
    static class MyMain
    {
        public static void Update()
        {

        }
    }
}
