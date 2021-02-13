using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace UniBlock
{

    //有限時間で自動的に終了する物はこちらへ
    public class TimerBlock : FiniteBlock
    {
        protected float intervalMs = 1000f;
        public System.Diagnostics.Stopwatch sw;
        bool endFinished = false;

        public sealed override void Start()
        {
            Reset();
            sw = new System.Diagnostics.Stopwatch();
            sw.Restart();
            TimerStart();
        }

        public sealed override void Update()
        {
            if (sw.ElapsedMilliseconds >= intervalMs)
            {
                if (endFinished == false)
                {
                    TimerEnd();
                    SetEnd();
                    endFinished = true;
                }
            }
            else
            {
                TimerUpdate();
            }
        }

        public virtual void TimerStart() { }

        public virtual void TimerUpdate() { }

        public virtual void TimerEnd() { }
    }

    //n秒間待機する
    public sealed class Wait : TimerBlock
    {
        public Wait(float second)
        {
            this.intervalMs = second * 1000f;
        }
    }

    public sealed class Liner : TimerBlock
    {
        Func<float> func;
        Action<float> action;
        float start;
        float end;

        public Liner(Func<float> func, Action<float> action, float end, float second)
        {
            this.action = action;
            this.func = func;
            this.end = end;
            this.intervalMs = second * 1000f;
        }

        public sealed override void TimerStart()
        {
            start = func();
        }

        public sealed override void TimerUpdate()
        {
            //値
            var y1 = start;
            var y2 = end;
            var x1 = 0;
            var x2 = intervalMs;
            var t = sw.ElapsedMilliseconds;
            //傾き
            var A = (y2 - y1) / (x2 - x1);
            //切片
            var B = y1;
            //出力
            var y = A * t + B;
            //出力する色
            action(y);
            Debug.Log(y);
        }

        public sealed override void TimerEnd()
        {
            action(end);
        }
    }

    public sealed class LinerVector4 : TimerBlock
    {
        Func<Vector4> func;
        Action<Vector4> action;
        Vector4 start;
        Vector4 end;

        public LinerVector4(Func<Vector4> func, Action<Vector4> action, Vector4 end, float second)
        {
            this.action = action;
            this.func = func;
            this.end = end;
            this.intervalMs = second * 1000f;
        }

        public sealed override void TimerStart()
        {
            start = func();
        }

        public sealed override void TimerUpdate()
        {
            //値
            var y1 = start;
            var y2 = end;
            var x1 = 0;
            var x2 = intervalMs;
            var t = sw.ElapsedMilliseconds;
            //傾き
            var A = (y2 - y1) / (x2 - x1);
            //切片
            var B = y1;
            //出力
            var y = A * t + B;
            //出力する色
            action(y);
            Debug.Log(y);
        }

        public sealed override void TimerEnd()
        {
            action(end);
        }
    }

    //n秒間かけて透明→黒になる
    public sealed class FadeOn : TimerBlock
    {
        Image image;
        float initTrans = 1f;

        public FadeOn(Image fadeImage, float second)
        {
            this.image = fadeImage;
            this.intervalMs = second * 1000f;
        }

        public sealed override void TimerStart()
        {
            //this.image = fade.GetImage();
            //操作無効にする
            image.raycastTarget = true;
            //現在の透明度を取得する
            initTrans = image.color.a;
        }

        public sealed override void TimerUpdate()
        {
            //値
            var y1 = initTrans;
            var y2 = 1f;
            var x1 = 0;
            var x2 = intervalMs;
            var t = sw.ElapsedMilliseconds;
            //傾き
            var A = (y2 - y1) / (x2 - x1);
            //切片
            var B = y1;
            //出力
            var y = A * t + B;
            //出力する色
            this.image.color = new Color(0.5f, 0.5f, 0.5f, y);
        }

        public sealed override void TimerEnd()
        {
            this.image.color = new Color(0.5f, 0.5f, 0.5f, 1);
        }
    }

    //n秒間かけて黒→透明になる
    public sealed class FadeOff : TimerBlock
    {
        Image image;
        float initTrans = 1f;
        public FadeOff(Image fadeImage, float second)
        {
            this.image = fadeImage;
            this.intervalMs = second * 1000f;
        }

        public sealed override void TimerStart()
        {
            //現在の透明度を取得する
            initTrans = image.color.a;
        }

        public sealed override void TimerUpdate()
        {
            //値
            var y1 = initTrans;
            var y2 = 0f;
            var x1 = 0;
            var x2 = intervalMs;
            var t = sw.ElapsedMilliseconds;
            //傾き
            var A = (y2 - y1) / (x2 - x1);
            //切片
            var B = y1;
            //出力
            var y = A * t + B;
            //出力する色
            this.image.color = new Color(0.5f, 0.5f, 0.5f, y);
        }

        public sealed override void TimerEnd()
        {
            this.image.color = new Color(0.5f, 0.5f, 0.5f, 0);

            //操作を有効にする
            image.raycastTarget = false;
        }

    }

    //テスト用ブロック
    public sealed class Test : TimerBlock
    {
        string text;
        public Test(string text)
        {
            this.text = text;
        }

        public sealed override void TimerStart()
        {
            Debug.Log("開始：" + text);
        }

        public sealed override void TimerUpdate()
        {
            //Debug.Log("継続：" + text);
        }

        public sealed override void TimerEnd()
        {
            Debug.Log("終了：" + text);
        }

    }
}