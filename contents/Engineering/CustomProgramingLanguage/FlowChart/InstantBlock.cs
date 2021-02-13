using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

namespace UniBlock
{
    //有限時間かつ一瞬で終了するモノはこちらへ
    public class InstantBlock : FiniteBlock
    {
        public sealed override void Start()
        {
            Reset();
            Action();
            SetEnd();
        }

        public sealed override void Update() { }

        public virtual void Action() { }
    }

    public sealed class Function : InstantBlock
    {
        Action action;

        public Function(Action action)
        {
            this.action = action;
        }

        public override void Action()
        {
            action.Invoke();
        }
    }
}
