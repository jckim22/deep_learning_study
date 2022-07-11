Optimization(최적화)
    Loss function(손실 함수): 아래로 볼록한 형태
    1/n시그마L(y,y')=L(w1,....wn) 우리가 학습하기 위한 전체 손실함수의 값
    1/n시그마 = 평균

    왜 아래로 볼록한가 ?
        Gradient
        학습법 : w(t+1)=w(t)-scale * lowL/low w(t)
        현재 지점의 노드에서부터 접선을 구하고 점점
        음수로 loss가 점점 0에 수렴하게 되면 잘 학습할 수 있게 되는 것이다.

    Momentum(다차원 공간)
        그 점에 이동하던 델타만큼을 이번 파라미터 학습에
        추가해줌으로써 학습을 가속화함
        이전까지의 방향의 가속을 받아들여서, 그대로
        이어나가는 학습방식 !
        위아래로 가는 건 줄어들고 더 기울어져서 한번에 많이 간다
        (지그재그일때)
        어차피 같은 방향으로 갈 거면 불필요한 움직임을 최대한 줄이고
        관성을 이용해서 더 빠르게 간다

    Adam
        모멘텀 기반
    RMSprop
        모멘텀 기반

Batch SGD
    Loss에서 모든 데이터를 다 넣어주게 되면 너무 많은
    메모리가 사용되고 오히려 계산이 이상하게 되는 경우가 있었다.
    그래서 나온 것이 데이터를 묶어서 나눠서 계산하자는
    Batch SGD이다

    Batch: 데이터 묶음

    Batch Gradient Descent  
    한번에 다
    Mini-batch Gradient Descent
    작은 집합
    Stochastic(확률적인) Gradient Descent
    한개씩
    지금 받은 데이터를 전체 학습하면 확률적인 것은 0
    하지만 한개씩 가져와서 한번씩 트레이닝 해주게 되면
    모든 데이터에 집중되지 않고 보지 않았던 데이터들에
    대해서도 성능을 잘 내게 된다.

Learning rate(학습률) decay(감소)
    Learning rate = w(t+1) = w(t) - scale*low L/low w
    constant value로 하게 되면 최적의 값(극소값)에 도달하지 못하고
    그 인근을 진동할 수 있다
    그렇기 때문에 그 진동하는 거리를 decay해야한다

        1.Step decay
            scale = 0.1*scale

        2.Exponential decay

        3.Cosine decay
            0 근처에서 급진적으로 수렴
