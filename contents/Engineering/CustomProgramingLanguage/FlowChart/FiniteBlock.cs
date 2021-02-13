using UnityEngine;

namespace UniBlock
{
    //終了が確約されているブロック
    [System.Serializable]
    public class FiniteBlock : BlockBase
    {
        public virtual void Start()
        {
            Reset();
        }

        public virtual void Update()
        {
            SetEnd();
        }

        //ブロックを実行する
        public void Activate()
        {
            GameObject obj = new GameObject();
            obj.AddComponent<BlockManager>();
            BlockManager manager = obj.GetComponent<BlockManager>();
            manager.block = (FiniteBlock)this.MemberwiseClone();

            //今後はNotDestroy属性つけるといいかも
        }

    }
}