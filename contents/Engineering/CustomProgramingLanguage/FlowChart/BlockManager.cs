using UnityEngine;

namespace UniBlock
{
    //自動的にマネージャが立ち上がり処理が実行し、自動的に終了する
    public class BlockManager : MonoBehaviour
    {
        public FiniteBlock block;
        bool isStart = true;
        private void Update()
        {
            if (block != null)
            {
                //開始
                if (isStart)
                {
                    block.Start();
                    isStart = false;
                }

                //update
                block.Update();

                //終了
                if (block.IsEnd())
                {
                    //自身を破壊する
                    Destroy(this.gameObject);
                }
            }
        }
    }

    //ブロックを継承することで使用可能になる
    [System.Serializable]
    public class BlockBase
    {
        bool isEnd = false;

        protected void SetEnd()
        {
            isEnd = true;
        }

        protected void Reset()
        {
            isEnd = false;
        }

        public bool IsEnd()
        {
            return isEnd;
        }
    }

}