# フローチャートについて

## 直列のシーケンス

```
ProcessList = []
void Update(){
    foreach(var p in ProcessList){
        p.InternalUpdate()
    }
}

class Process{
    bool IsEnd

    public void Activate(){
        BaseReset()
        ProcessList.add(this)
        Start()
    }

    public void InternalUpdate(){
        if(!IsEnd){
            Update()
        }
    }

    public void BaseReset(){
        isEnd = False
        Reset()
    }

    public void SetEnd(){

    }

    public virtual void Start(){}
    public virtual void Update(){}
    public virtual void End(){}

}

class Sequence : Process{
    Process[] array
    int index = 0
    Process current

    public init(params Process[] array){
        this.array = array
    }

    public override void Start(){
        index = 0
        current = array[index]
    }

    public override void Update(){
        current.Update()

        if(current.IsEnd){
            current.End()
            index += 1
            if(index < array.size){
                current = array[index]
                current.Start()
            }else{
                End()
            }
        }
    }

    public override void End(){
        SetEnd()
    }

}

class Main{
    Unit seq = sequence(
        Hello(),
        wait(3),
        Goodbye()
    )

    void func(){
        seq.Start()
    }
}
```
