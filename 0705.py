비전=모델을 다루는 걸 중점으로 다룬다
딥러닝이라는 도구를 통해 비전이 엄청나게 발전했다.
그래서 비전과 딥러닝은 뗄 수가 없다

딥러닝의 역사 (근래 5년)
    a.자연어 처리(google 번역기):
        ex)한국어 데이터 -> 모델 = 영어
    b.alphago
        딥러닝의 카테고리의 강화학습이 사용
    c.Camera Filter
        ex)인스타 필터

    d.Object Detection
        ex)CCTV -> video,image
            그 이미지 속에서 객체를 인식함(Object를 Detection함)
            보행자를 인식해서 감응신호도 할 수 있다.

연대기
    AI가 발전하기 위해서는 굉장한 연산량이 필요했다.
        ex)사진을 주고 고양이냐 강아지냐 구별하는 것은 데이터가 많이 필요함
            그걸 1초만에 하는 것은 불가능하다고 생각했음
        그렇기 때문에 딥러닝은 점점 미지로 가기 시작했음

    Deep Neural Network의 등장으로 연산이 가능해짐
        GPU가 개발되었기 때문

AI란
    인간의 학습능력, 추론능력, 지각능력, 그 외에 인공적으로 구현한 컴퓨터
    프로그램 또는 컴퓨터 시스템이다.
Machine Learning이란
    경험을 통해 자동으로 개선하는 컴퓨터 알고리즘의 연구이다.
    컴퓨터가 학습할 수 있도록 하는 알고리즘과 기술을 개발하는 분야이다.
Deep Learning이란
    머신러닝 중에서도 특정한 기법이다.
    여러 비선형 변환기법(인공신경망)의 조합을 통해 높은 수준의 추상화를 시
    도하는 기계 학습 알고리즘의 집합.

Deep Learning
    a.머신러닝
        1.최적화!!!
            학습을 위해서는 파라미터(변수)가 필요
            이 변수를 데이터로부터 학습하는데
            어떤 목적을 갖고 학습을 할까 다루는 것 !
        2.회귀 및 분류
            Regression vs Classfication
        3.지도학습 비지도학습
            Supervised Learning
                Data(고양이 이미지), Label(이 사진이 고양이라고 대응되는 것)
                    이 라벨로 이 데이터를 지도한다 !
            Unsupervised Learning
        4.기타

    ****ML,DL프레임워크*****
    data -> 알고리즘을 통과 -> 어떤 목적함수를 통해서 값을 계산 -> 피드백 -> 다시 처음
    

    b.비선형(직선이 아닌 함수)(activation function)
    c.인공신경망(Artificial Neural Network, ANN)
    
    예제: Stock price prediction )
        A라는 회사의 주가를 예축해보자
        x1:of buildings      ->     ->      Company Size
        x2:of employees           ->  ->    Expected Valuation  ->-> y -> Loss(y,y') = 결과값
        x3:Previous price   ->  ->          Market Size 
        x4:경쟁사 가격              ->
            data                  algorithm                                   Loss(목적함수)

    y는 Label이다 
    예측값과 Label(예시로 실제 1월의 회사의 주가)
    의 에러를 줄이는방식(최적화)로 학습을 하다보면 
    근사치의 결과값이 나오지 않을까?

    연산 프레임워크
        x(입력값)는 많으면 많을 수록 좋다
        x를 edge를 통해서 w라는 파라미터를 만들어주고 곱셈과 b(bias)를 더하는
        연산을 이용하여 Node를 만들고 그 안에 Z라는 파라미터를 만든다.
        Node에서는 Z를 이용하여 a(z)를 통과하여(activation function)(비선형)
        y(예측값)을 만들고 y를 y'(원래의 값)과 에러를 줄이는 방식으로
        연산을 하고 피드백을 주면 w와 b가 학습이 된다.
   

    Practice : 의료 데이터 (Regression)
        이 사람이 covid인지 아닌지 예측하는 algorithm 구현
        
        모델 디자인 하기 !!!
            Data   ->            algorithm                      ->          Loss
            x1:성별    x*w+b(선형구조) -> Z->a(z)(비선형구조) = y(ex:양성 1)            Loss(y,y'(ex:음성 0))
            x2:xray     w2                                          loss=|y-y'|  = 1
            x3:나이     w3                                          1을 w와 b에게 전달해서 학습(loss가 0이 나올 때 까지)

    Q) Neural Network가 deep해지면 이점이 무엇일까 ? (Fully Connected Layer)

        input layer -> hidden layer1 -> hidden layer2 -> ouput layer
        hidden layer가 2개 이상이면 어떨까 ???
        2-hidden layer NN

        마냥 좋지만은 않다 왜?
            10개의 layer
            1개의 layer 
            표현력이 똑같다(activation function(활성화 함수)이 없을 때)
            다 선형구조이기 때문에

            그래서 !
                그 hidden layer 사이에 비선형(a(f)) layer를 넣는다
                선형 -> 비선형 -> 선형 -> 비선형 = 성능 UP
                
        비선형 함수들에는
            Sigmoid
            tanh
            **ReLU=0을기준으로 음수는 0 양수는 y=x
            **Leaky ReLU = 0을 기준으로 음수는 0보다 작은 매우 작은 기울기 양수는 y=x1
            Maxout
            ELU

Q1)AI ML DL의 차이점은 ?

Q2)ML의 일반적인 framwork를 서술해보자
    data -> algorithm -> lossㅗ델

Q3)NN(인공신경망)모델은 왜 Practical하고 useful할까 ?
    전문지식이 필요 없다
Q4)activation function(활성화 함수)가 하는 역할 ?
    비선형 함수이다

    Activation function (활성화 함수)

    ex)나선형의 빨간색 점들과 파란색 점들을 분류할 때
    선형 = 무조건 선을 그어서 분류
    비선형 = 고차원으로 그 데이터들을 잘 분류할 수 있게 한다.
    인공신경망은 비선형을 넣게 되면 Decision boundary를 잘 그어준다

Remember!!
    Node:o
    edge:->
    Loss:제일 마지막에 알고리즘을 학습하기 위한 목적 함수
    Hidden layer:위층으로 가기 위한 층
    Forward propagation:data에서 Loss로 가는 것
    Backward propagation:Loss에서 학습을 위해서 algorithm으로 가는 것
    Gradient:Backward를 할 때 파라미터를 학습해주기 위해서 Loss를 기준으로
    미분하는 것