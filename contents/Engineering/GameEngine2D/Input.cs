using System;
using System.Linq;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Input;

//インプットクラス
//ユーザの入力はここで管理
namespace GameEngine2D
{
    enum Keycode
    {
        Other = 0,
        A = 1,
        B, C, D, E, F, G, H, I, J, K,
        L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

    }
    static class Input
    {
        public static bool GetKeyDown(Keycode keycode)
        {
            int index = (int)(keycode);
            if ((Internal.InputCore.KeyPrev[index] == false) && (Internal.InputCore.KeyNext[index] == true))
            {
                return true;
            }
            return false;
        }

        public static bool GetKeyUp(Keycode keycode)
        {
            int index = (int)(keycode);
            if ((Internal.InputCore.KeyPrev[index] == true) && (Internal.InputCore.KeyNext[index] == false))
            {
                return true;
            }
            return false;
        }

        public static bool GetKey(Keycode keycode)
        {
            int index = (int)(keycode);
            if ((Internal.InputCore.KeyPrev[index] == true) && (Internal.InputCore.KeyNext[index] == true))
            {
                return true;
            }
            return false;
        }


    }
}