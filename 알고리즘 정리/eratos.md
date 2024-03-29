#### 에라토스테네스의 체
> ##### 이 알고리즘은 에라토스테네스라는 사람이 만들어 낸 `소수를 찾는 방법`이다.
> ##### 찾아내는 방법은 2부터 시작해 n까지의 수중 소수를 잡는다. 그리고 n보다 작은 소수의 배수를 걸러낸다.
> ##### 이 방법을 n 범위 안에있는 모든 소수에 대해 위 방식을 적용하면 소수를 걸러낼 수 있다.
> ##### 아래는 영상으로 보여지는 예시다.
> ##### ![Sieve_of_Eratosthenes_animation](https://user-images.githubusercontent.com/80656788/187200047-1608378c-1d76-4d96-928d-21ebdffeae2c.gif)

> ##### 아래는 c++로 구현한 에라토스테네스 알고리즘이다.
```c++
int arr[1000];

void Eratos(int n)
{
  fill_n(arr+2, n, true); // 처음에 배열을 모두 true로 초기화해줌.
    for(int i=2;i<=n;i++){ // 2부터 시작
        for(int j=i*2;j<=n;j+=i){ // i의 배수
            arr[j]=false;   // 걸러내는 작업
        }
    }
}
```
> ##### 이 알고리즘을 사용하면 시간복잡도 O(NloglogN)을 보장한다.
> ##### 예시문제 [백준 1929 소수구하기](https://www.acmicpc.net/problem/1929)
