using UnityEngine;
using UnityEngine.UI;

namespace UniBlock
{
    //ブロックを拡張させる特殊なものはこちらへ

    //直列に実行する
    [System.Serializable]
    public sealed class Sequence : FiniteBlock
    {
        FiniteBlock[] blocks;

        int index = 0;


        public Sequence(params FiniteBlock[] blocks)
        {
            this.blocks = blocks;
        }

        public sealed override void Start()
        {
            Reset();
            if (blocks != null)
            {
                blocks[index].Start();
            }
            else
            {
                SetEnd();
            }
        }

        public sealed override void Update()
        {
            //例外処理
            if (blocks == null) return;

            //終了条件判定
            if (blocks[index].IsEnd())
            {
                index += 1;
                if (index >= blocks.Length)
                {
                    SetEnd();
                    index = 0;
                }
                else
                {
                    blocks[index].Start();
                    //もう一度検証する(1フレームロスを防ぐ)
                    this.Update();
                }
            }
            else
            {
                //Update
                blocks[index].Update();
            }

        }


    }

    //並行に実行し、どれか一つでも終了すると次へ進む
    [System.Serializable]
    public sealed class ParallelOne : FiniteBlock
    {
        FiniteBlock[] blocks;
        public ParallelOne(params FiniteBlock[] blocks)
        {
            this.blocks = blocks;
        }

        public sealed override void Start()
        {
            Reset();
            if (blocks != null)
            {
                foreach (var block in blocks)
                {
                    block.Start();
                }
            }
            else
            {
                SetEnd();
            }
        }

        public sealed override void Update()
        {
            //例外処理
            if (blocks == null) return;

            //終了条件判定
            foreach (var block in blocks)
            {
                if (block.IsEnd())
                {
                    SetEnd();
                    return;
                }
            }

            //Update
            foreach (var block in blocks)
            {
                block.Update();
            }
        }
    }

    //並行に実行し、全て終了すると次へ進む
    [System.Serializable]
    public sealed class ParallelAll : FiniteBlock
    {
        FiniteBlock[] blocks;
        public ParallelAll(params FiniteBlock[] blocks)
        {
            this.blocks = blocks;
        }

        public sealed override void Start()
        {
            Reset();
            if (blocks != null)
            {
                foreach (var block in blocks)
                {
                    block.Start();
                }
            }
            else
            {
                SetEnd();
            }
        }

        public sealed override void Update()
        {
            //例外処理
            if (blocks == null) return;

            //終了条件判定
            bool isContinue = false;
            foreach (var block in blocks)
            {
                //一つでも終了していないものがあれば、継続する
                if (!block.IsEnd())
                {
                    isContinue = true;
                }
            }

            if (isContinue)
            {
                //Update
                foreach (var block in blocks)
                {
                    block.Update();
                }
            }
            else
            {
                SetEnd();
            }
        }
    }

}